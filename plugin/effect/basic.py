# coding:utf-8
import sys
import numpy
import os
import copy

# 削除厳禁！


class InitialValue:
    def __init__(self):
        pass

    def main(self, elements):
        self.setting_example = elements.effectElements()
        self.setting_example.effectname = str(os.path.basename(__file__))
        self.setting_example.effectPoint = [{"time": 0, "x": 0, "y": 0, " z_angle ": 0, " alpha ": 100, "size": 0}]
        self.setting_example.various_fixed = {}
        self.setting_example.procedurelist = CentralRole()
        self.setting_example.calculation_mode = True

        return self.setting_example


class CentralRole:
    def __init__(self):
        pass

    def main(self):
        pass
