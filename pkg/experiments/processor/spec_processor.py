from processor.abstract_processor import *
import settings
import cv2
# 图片规格检查器
class SpecCheckProcessor(AbstractProcessor):

    def process(self, m: Material)->Material:
        materialConfig = settings.materialsConfig[m.getName()]
        expect_width = materialConfig['width']
        expect_height = materialConfig['height']
        width, height = m.getImg().size

        # if expect_width != width or expect_height != height:
        #     raise ValueError(m.getName(), m.getPath(), (expect_height, expect_width), (height, width))

        if m.getImg().mode != 'RGBA':
            raise ValueError(m.getName(), m.getPath(), m.getImg().mode)
        return m



