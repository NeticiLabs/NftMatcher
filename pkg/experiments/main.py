from processor.spec_processor import *
from utils.io_utils import *
from template import Template
import  cv2

if __name__ == '__main__':
    tpl = Template('template2','template2', 'output')
    tpl.combine()
    # im = cv2.imread('template2/leftEye/back.png')
    # print(im.shape)
    # im = cv2.imread('template1/person/main1.jpg')
    # m = Material('animal', im, 1)
    # p = BackgroundRemoveProcessor()
    # p.process(m)
    # cv2.imwrite('Foto.png', m.getImg())

    # bg1 = extend_resize('template1/bg1.jpg')
    # img = cv2.imread('template1/aux1.jpg', cv2.IMREAD_UNCHANGED)
    # m = Material('auxChar', img)
    #
    # bgRemover = BackgroundRemoveProcessor()
    # bgRemover.process(m)


