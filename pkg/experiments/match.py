
import string
import numpy as np
import cv2


def feature(img_path=string, vector_size=32):
    # img
    img = cv2.imread(img_path, 1)  # 读取图片

    # SIFT特征提取
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sift = cv2.ORB_create()
    kp = sift.detect(gray, None)
    # 画出特征点并保存
    img = cv2.drawKeypoints(gray, kp, img)
    # 根据关键点的返回值进行排序（越大越好）
    kp = sorted(kp, key=lambda x: -x.response)[:vector_size]
    # 计算描述符向量
    kp, des = sift.compute(gray, kp)
    # 将其放在一个大的向量中，作为我们的特征向量
    des = des.flatten()
    # 使描述符的大小一致
    # 描述符向量的大小为128
    needed_size = (vector_size * 128)
    if des.size < needed_size:
        # 如果少于32个描述符，则在特征向量后面补零
        des = np.concatenate([des, np.zeros(needed_size - des.size)])

    return des

def compare(v1, v2):
    nominator= np.dot(v1,v2)
    denominator = np.linalg.norm(v1) * np.linalg.norm(v2)
    return nominator/denominator

if __name__=='__main__':
    v1 = feature('1.png')
    v2 = feature('400.png')

    similiar = compare(v1, v2)
    print(similiar)