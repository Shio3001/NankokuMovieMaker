# coding:utf-8
import sys
import numpy
import os

import cv2
from PIL import Image, ImageDraw, ImageFilter
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont


class ImportImage_Main:
    def Image_Main(self, layer, NumberLayer):
        addNewImgae = None
        print("画像ファイルを入力...")
        os.system("pwd")
        os.system("ls")
        inp_in = str(sys.stdin.readline().rstrip())

        try:
            addNewImgae = cv2.cvtColor(cv2.imread(inp_in), cv2.COLOR_RGB2RGBA)
        except:
            return "EXC"

        #addNewImgae = numpy.array(Image.open(inp_in))

        #addNewImgae = cv2.cvtColor(addNewImgae_pic, cv2.COLOR_RGB2RGBA)

        layer[NumberLayer].ObjectType = "2"

        layer[NumberLayer].Document = addNewImgae

        return layer