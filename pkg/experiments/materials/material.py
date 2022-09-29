import cv2

class Material():

    def __init__(self, name, img, path, priority):
        self.name = name
        self.img = img
        self.path = path
        self.priority = priority

    def getPath(self)->str:
        return self.path

    def getName(self)->str:
        return self.name

    def setImg(self, img):
        self.img = img

    def getImg(self):
        return self.img

    def getPriority(self)->int:
        return self.priority
