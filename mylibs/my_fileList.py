# coding: utf-8

import sys
import glob
import os


def fileCheck(filePath):
    """ファイルの存在をチェックする"""
    if not os.path.exists(filePath):
        print("%s not found." %filePath)
        exit(0)


def get(dirPath):
    """指定したパスのファイル一覧を取得する"""

    if sys.version_info.major != 3:
        print("Error!!\nPython 3.x is required.")
        exit()

    if sys.version_info.minor >= 5:
        # python 3.5以降
        fileList = []
        fileList = glob.glob(dirPath, recursive=True)
        return fileList

    else:
        # python3.4以前
        fileList = []
        for root, dirs, files in os.walk(dirPath):
            for filename in files:
                fileList.append(os.path.join(root, filename))   # ファイルのみ再帰でいい場合はここまででOK
            for dirname in dirs:
                fileList.append(os.path.join(root, dirname))    # サブディレクトリまでリストに含めたい場合はこれも書く
        print(fileList)
        return fileList
