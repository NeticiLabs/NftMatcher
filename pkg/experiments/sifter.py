import cv2

img1=cv2.imread('1.png')
img2=cv2.imread('2.png')

sift = cv2.xfeatures2d.SURF_create()

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

good = [[m] for m, n in matches if m.distance < 0.5 * n.distance]

img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
