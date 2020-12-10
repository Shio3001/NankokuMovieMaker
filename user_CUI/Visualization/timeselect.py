# coding:utf-8
import sys
import numpy
import os
import copy
import re


class CentralRole:
    def __init__(self):
        pass

    def main(self, editor_fps):

        user_select = None
        while user_select != "exit":

            try:
                print("時間を入力してください")
                print("フレームでも時分秒でも可能 ただし時間分秒で入力する時には [ h ](時間) [ m ](分) [ s ](秒) [ ms ](ミリ秒をつけること)")
                print("例: 10分5秒を表したい場合 -> [ 0h10m5s ] 単位未指定はフレーム値扱いになります")

                user_select = str(sys.stdin.readline().rstrip().lower())

                frame_result = 0

                # print(editor_info)

                frame_result = self.conversion(user_select, editor_fps)

                print(str(frame_result) + "フレーム")
                print("")
                print("")
                return frame_result
            except ValueError:
                print("数字と特定の記号だけ入れようね")

            except:
                print("は？" + str(sys.exc_info()))

        return None

    def conversion(self, user_select, editor_fps):
        iflag = 0
        user_select_Wait = ""
        frame_result = 0

        for i in range(len(user_select)):

            if iflag > 0:
                i += iflag

            if iflag > 0 and i == int(len(user_select)):
                break

            try:
                if user_select[i] == "m" and user_select[i + 1] == "s":
                    frame_result += (int(user_select_Wait) / 1000) * int(editor_fps)
                    user_select_Wait = ""
                    print("ミリ秒を検知")
                    iflag += 1
                elif user_select[i] == "h":
                    frame_result += int(user_select_Wait) * 3600 * int(editor_fps)
                    user_select_Wait = ""
                    print("時間を検知")
                elif user_select[i] == "m":
                    frame_result += int(user_select_Wait) * 60 * int(editor_fps)
                    user_select_Wait = ""
                    print("分を検知")
                elif user_select[i] == "s" and user_select[i - 1] != "m":
                    frame_result += int(user_select_Wait) * int(editor_fps)
                    user_select_Wait = ""
                    print("秒を検知")
                else:
                    user_select_Wait += user_select[i]
                    if i == int(len(user_select)) - 1:
                        frame_result += int(user_select_Wait)
            except:
                pass

        return frame_result
