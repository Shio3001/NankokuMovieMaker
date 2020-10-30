# coding:utf-8
import sys

"""
import numpy
import os

import cv2
from PIL import Image, ImageDraw, ImageFilter
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
"""

import SelectLayer
#input = sys.stdin.readline

import PrintLayers

# 基本中間点を設定させる


class MakePoints:
    def __init__(self):
        self.SetSelectLayer = SelectLayer.SelectLayer()

    def Main(self, layer, AddOREdit):
        self.AddPoint = [0, 0, 0, 0]  # time(フレーム) , x , y ,透明度
        NumberLayer = self.SetSelectLayer.Main(layer)

        NumberPoint = None

        if NumberLayer == "Det":
            return "Det"

        if AddOREdit == 1:
            NumberPoint = self.SetSelectLayer.Point(layer, NumberLayer)

        if NumberPoint == "Det":
            return "Det"

        print("")

        print("設定するものを入力 [x][y][a] 複数記入も可 例:[xy] [ya]")
        Choices = str(sys.stdin.readline().rstrip())

        print(Choices)

        print("")
        print("設定する時間の入力 [ 数値 ]")

        try:
            self.AddPoint[0] = int(sys.stdin.readline().rstrip())
        except:
            return "Det"

        print("")

        Cho = "x" in Choices
        if Cho == True:
            print("座標：Xの入力 [ 数値 ]")
            try:
                self.AddPoint[1] = int(sys.stdin.readline().rstrip())
            except:
                return "Det"

        print("")

        Cho = "y" in Choices
        if Cho == True:
            print("座標：Yの入力 [ 数値 ]")
            try:
                self.AddPoint[2] = int(sys.stdin.readline().rstrip())
            except:
                return "Det"

        print("")
        Cho = "a" in Choices
        if Cho == True:
            print("透明度 [ 数値 ]")
            try:
                self.AddPoint[3] = int(sys.stdin.readline().rstrip())
            except:
                return "Det"

        if AddOREdit == 0:
            print(layer[NumberLayer].Point)

            layer[NumberLayer].Point.append(self.AddPoint)
            print(layer[NumberLayer].Point)

        elif AddOREdit == 1:
            layer[NumberLayer].Point[NumberPoint] = self.AddPoint

        return layer