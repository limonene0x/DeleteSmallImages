# coding:gbk
"""DeleteSmaiiImages
@author:Limonene0x
@version:1.0.1
"""
import os
from PIL import Image
import glob
dir1 = ''  # 图片文件目录（当前文件夹留空）
paths = glob.glob(os.path.join(dir1, '*.png'))+glob.glob(os.path.join(dir1, '*.jpg'))+glob.glob(os.path.join(dir1, '*.jpeg'))
# 识别文件扩展名包含：*.jpg  *.png  *.jpeg
widthLimit = int(input("Please input width limit:"))
heightLimit = int(input("Please input height limit:"))
for file in paths:
    fp = open(file, 'rb')
    img = Image.open(fp)
    fp.close()
    width = img.size[0]
    height = img.size[1]
    if (width <= widthLimit) and (height <= widthLimit):
        os.remove(file)