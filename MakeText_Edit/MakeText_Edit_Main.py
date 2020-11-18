# coding:utf-8
import sys
import numpy
import os

import cv2
from PIL import Image, ImageDraw, ImageFilter
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont

# 2番目にえらい
#import EditData


class MakeEditMain:

    def EditTexts_Main(self, layer, EditSize, ilayerloop, Set_SelectColor, Set_MakeEditText_EditData):

        GetEditTextsMember = [0, 0]
        Main_addfntSize = layer[ilayerloop].Document[:].TextSize

        EditNewText = ""
        print("新しい文字列を入力 変更しないなら空白で [ 文字列 ]")

        try:
            EditNewText = int(sys.stdin.readline().rstrip())
            print(EditNewText)
        except:
            print("空白を検知")

        if int(len(EditNewText)) != 0:
            layer[ilayerloop].UniqueProperty.NewTextString = EditNewText

        print("文字列を取得")
        print(str(layer[ilayerloop].UniqueProperty.NewTextString))
        print("文字数" + str(int(len(layer[ilayerloop].UniqueProperty.NewTextString)) - 1))
        print("選択可能範囲" + " 0 から" + str(int(len(layer[ilayerloop].UniqueProperty.NewTextString))))

        StringCount = int(len(layer[ilayerloop].UniqueProperty.NewTextString))
        EditTexts_fntSize = Main_addfntSize

        # self.GetEditTextsMember = None

        for i in range(2):
            print("変更したいテキスト開始地点を入力[ 数値 ] (もしくは [ ALL ] 全て選択できます)")
            try:
                GetEditTextsMember[i] = str(sys.stdin.readline().rstrip())

                if "ALL" in GetEditTextsMember:
                    GetEditTextsMember = [0, int(len(layer[ilayerloop].UniqueProperty.NewTextString)) - 1]
                    break

            except:
                return "Det"

        # self.GetEditTextsMember = map(lambda x: int(x), self.GetEditTextsMember)

        EditTexts_Status = ""
        while EditTexts_Status != "Det":
            EditTexts_Status, EditTexts_layer = self.EditTexts_Operation(layer, EditSize, ilayerloop, GetEditTextsMember, EditTexts_fntSize, StringCount, Set_SelectColor, Set_MakeEditText_EditData)

            if EditTexts_Status != "exit":
                layer = EditTexts_layer
                break

        return layer

    def EditTexts_Operation(self, layer, EditSize, ilayerloop, GetEditTextsMember, EditTexts_fntSize, StringCount, Set_SelectColor, Set_MakeEditText_EditData):
        print("次の動作を入力 [ 番号 ] もしくは [ 文字列 ]")
        NextChoiceList = {1: "exit", 2: "size", 3: "colour"}
        print(NextChoiceList)

        AskNextAction = str(sys.stdin.readline().rstrip())
        if AskNextAction == NextChoiceList[1] or AskNextAction == "1":
            return "exit", layer

        if AskNextAction == NextChoiceList[2] or AskNextAction == "2":
            AskDi = Set_MakeEditText_EditData.EditDataElement().Import_Size(layer, EditSize, ilayerloop, GetEditTextsMember, EditTexts_fntSize, Set_MakeEditText_EditData)
            if AskDi == "Det":
                print("問題あり")
                return "Det", layer
            else:
                layer = AskDi

        if AskNextAction == NextChoiceList[3] or AskNextAction == "3":
            AskDi = Set_MakeEditText_EditData.EditDataElement().Import_Color(layer, EditSize, ilayerloop, GetEditTextsMember, StringCount, Set_SelectColor, Set_MakeEditText_EditData)
            if AskDi == "Det":
                print("問題あり")
                return "Det", layer
            else:
                layer = AskDi

        return "ok", layer
