# coding:utf-8
import sys
import numpy
import os

import cv2
from PIL import Image, ImageDraw, ImageFilter
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont

# input = sys.stdin.readline
import PrintLayers
import SelectLayer

import SelectColor

from MakeText_Edit import EditData


class MakeTexts:
    def __init__(self):
        # self.SetSelectLayer = SelectLayer.SelectLayer()
        self.Set_SelectColor = SelectColor.SelectColor_Center()

        self.NewTextString = None  # 生成するてきすと
        self.fntSize = None  # Pointスキップ方法に基づきNone
        self.addfntSize = []
        self.GetEditTextsMember = [None, None]

    def Main(self, layer, EditSize, ilayerloop):
        # CUI化で消滅
        # fntSizeは定数 拡大縮小は基本pointのsizeからやること

        layer[ilayerloop].UniqueProperty = TextElements()
        layer[ilayerloop].Document = []
        RGBdata = []

        TextSpacing = 0  # 仮設置 pointクラス化工事が終了した次第に削除するように

        print("生成したいテキストを入力 [ 文字列 ]")
        self.NewTextString = str(sys.stdin.readline().rstrip())  # 入力させる

        print("フォントサイズを入力 [ 数値 ]")
        try:
            # self.fntSize.append(int(sys.stdin.readline().rstrip()))
            self.addfntSize = [int(sys.stdin.readline().rstrip())] * len(self.NewTextString)
        except:
            return "Det"

        print("横書き [ 0 ] 縦書き [ 1 ] を入力 [ 数値 ]")
        try:
            layer[ilayerloop].UniqueProperty.WritingDirection = int(sys.stdin.readline().rstrip())
        except:
            return "Det"

        print("文字間隔 を入力 [ 数値 ]")
        try:
            # layer[ilayerloop].UniqueProperty.TextSpacing = int(sys.stdin.readline().rstrip())
            TextSpacing = int(sys.stdin.readline().rstrip())
        except:
            return "Det"

        print("[左右]揃え位置を入力 左揃え [ 0 ] 中揃え [ 1 ] 右揃え [ 2 ] [ 数値 ]")
        try:
            layer[ilayerloop].UniqueProperty.AlignmentPosition[0] = int(sys.stdin.readline().rstrip())
        except:
            return "Det"

        print("[上下]揃え位置を入力 上揃え [ 0 ] 中揃え [ 1 ] 下揃え [ 2 ] [ 数値 ]")
        try:
            layer[ilayerloop].UniqueProperty.AlignmentPosition[1] = int(sys.stdin.readline().rstrip())
        except:
            return "Det"

        print("個別オブジェクトにするかしないかを入力 しない [ 0 ] する [ 1 ] ")
        try:
            layer[ilayerloop].UniqueProperty.IndividualObject = int(sys.stdin.readline().rstrip())
        except:
            return "Det"

        print(self.addfntSize)
        AskDi = self.Set_SelectColor.RGB_select()
        if AskDi == "Det":
            return "Det"
        else:
            RGBdata = [AskDi] * len(self.NewTextString)

        layer = EditData.EditDataElement().Import_Cal(layer, EditSize, ilayerloop, RGBdata, self.addfntSize, self.NewTextString)

        EditData.EditDataElement().SetElement_Text(self.addfntSize, self.NewTextString, RGBdata)

        for i, ic in enumerate(layer[ilayerloop].Point):
            layer[ilayerloop].Point[i] = {**layer[ilayerloop].Point[i], "TextSetting": {"TextSpace": TextSpacing}}

        return layer


class TextElements:  # (TEXT定数)
    def __init__(self):
        self.TextSpacing = 0  # テキスト間隔 初期値 -で狭める、+で広げる
        self.WritingDirection = 0  # 書字方向 #初期値横書き
        self.AlignmentPosition = [1, 1]  # 揃え位置を図る奴 0が左・上 1が真ん中 2が右・下
        self.IndividualObject = 0  # 個別に管理するか
        self.Maxfnt = 0  # 一番でかい文字サイズ
        self.NewTextString = ""  # 文字列
