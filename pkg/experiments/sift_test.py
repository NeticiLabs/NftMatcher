from matplotlib import pyplot as plt
from imagedt.decorator import time_cost
import cv2


#
# def bgr_rgb(img):
#  (r, g, b) = cv2.split(img)
#  return cv2.merge([b, g, r])
#
# @time_cost
# def sift_detect(img1, img2, detector='surf'):
#   if detector.startswith('si'):
#    print("sift detector......")
#    sift = cv2.xfeatures2d.SURF_create()
#  else:

#
# if __name__ == "__main__":
#  # load image
#  image_a = cv2.imread('G:/2018and2019two/qianrushi/wuluo1.jpg')#绝对路径
#  image_b = cv2.imread('G:/2018and2019two/qianrushi/wuluo2.jpg')
#  # ORB
#  # img = orb_detect(image_a, image_b)
#  # SIFT or SURF
#  img = sift_detect(image_a, image_b)
#  plt.imshow(img)
#  plt.show()