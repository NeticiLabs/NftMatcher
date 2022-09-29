import os
import utils.io_utils as io
from PIL import Image
from materials.material import Material
import cv2
import settings
import numpy as np
from processor import *

class Template:

    def __init__(self, input_base, tpl_name, output_path):
        self.input_base = input_base
        self.tpl_name = tpl_name
        self.output_path = output_path # 素材输出到最后
        self.processors = [SpecCheckProcessor()]
        if os.path.exists(output_path):
            io.remove(output_path)
        os.mkdir(output_path)


    def combine(self):
        # 加载素材
        mg = self._loadMaterials()
        # 对每个素材进行标准化处理(规格处理，背景淡化处理)
        mg = self._normalized(mg)
        # 素材叠加
        all = self._add(mg)
        # 输出到目录

        self._save(all)


    def _loadMaterials(self):
        bgs = self._loadMaterialsFromFolder('bg')
        persons = self._loadMaterialsFromFolder('person')
        animals = self._loadMaterialsFromFolder('animal')
        necks = self._loadMaterialsFromFolder('neck')
        leftEyes = self._loadMaterialsFromFolder('leftEye')
        rightEyes = self._loadMaterialsFromFolder('rightEye')
        mouths = self._loadMaterialsFromFolder('mouth')
        return (bgs, persons, animals, necks, leftEyes, rightEyes, mouths)

    def _normalized(self, materials_group):
        for materials in materials_group:
            for i in range(len(materials)):
                m = materials[i]

                for p in self.processors:
                    m = p.process(m)
                materials[i] = m
        return materials_group

    def _add(self, materials_group):
        # 首先根据优先级，将所有的组件装入到不同的优先级桶中
        priorities = []
        for _ in range(len(settings.materialsConfig)):
            priorities.append([])

        for materials in materials_group:
            for m in materials:
                priorities[m.getPriority()].append(m)
        # 选取第i个优先级，prev，prev * priorities[i]张图片, 并叠加.
        res = []
        for m in priorities[0]:
            res.append(m.getImg().copy())

        for i in range(1, len(priorities)):
            materials = priorities[i]
            l = len(res)
            for j,m in enumerate(materials):
                for k in range(l):
                    base = res[k]
                    newImg = base.copy()
                    newImg = self._draw(newImg, m)
                    if j == 0:
                        res[k] = newImg
                    else:
                        res.append(newImg)
        print(len(res))
        return res

    def _save(self, all):
        for i in range(len(all)):
            all[i].save(os.path.join(self.output_path, str(i)+".png"), format="png")

    def _draw(self, background, m: Material):
        y_offset = settings.templates[self.tpl_name][m.getName()]['pos_h']
        x_offset = settings.templates[self.tpl_name][m.getName()]['pos_w']
        frontImage = m.getImg()
        width = (background.width - frontImage.width) // 2

        # Calculate height to be at the center
        height = (background.height - frontImage.height) // 2

        # Paste the frontImage at (width, height)
        background.paste(frontImage, (x_offset, y_offset), frontImage)
        return background
    def _loadMaterialsFromFolder(self, name):
        folder = os.path.join(self.input_base,  name)
        if not os.path.exists(folder):
            raise FileNotFoundError(folder)

        res = []
        for file_path in io.findAllFile(folder):
            # res.append(Material(name, cv2.imread(file_path,cv2.IMREAD_UNCHANGED), settings.materialsConfig[name]['priority']))
            img = Image.open(file_path)
            img.convert('RGBA')
            res.append(Material(name, img, file_path, settings.materialsConfig[name]['priority']))


        return res

    def overlay_transparent(self, background_img, img_to_overlay_t, y, x, overlay_size=None):
        bg_img = background_img

        if overlay_size is not None:
            img_to_overlay_t = cv2.resize(img_to_overlay_t, overlay_size)

        # Extract the alpha mask of the RGBA image, convert to RGB
        b, g, r, a = cv2.split(img_to_overlay_t)
        overlay_color = cv2.merge((b, g, r))

        # Apply some simple filtering to remove edge noise
        mask = cv2.medianBlur(a, 5)

        h, w, _ = overlay_color.shape
        roi = bg_img[y:y + h, x:x + w]

        # Black-out the area behind the logo in our original ROI
        img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))

        # Mask out the logo from the logo image.
        img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)

        # Update the original image with our new ROI
        print(bg_img)
        bg_img[y:y + h, x:x + w] = cv2.add(img1_bg, img2_fg)

        return bg_img