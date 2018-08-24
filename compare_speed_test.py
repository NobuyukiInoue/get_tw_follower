# coding: utf-8

import sys
import os
from datetime import datetime
import time
from mylibs import my_fileList
from mylibs import my_csv


def main():
    args = sys.argv
    argc = len(args)

    if argc <= 2:
        print("Usage: python %s file1 file2" %(args[0]))
        exit(0)

    my_fileList.fileCheck(args[1])
    my_fileList.fileCheck(args[2])

    lines1 = my_csv.readCSVfile(args[1])
    lines2 = my_csv.readCSVfile(args[2])

    # ========== 二重ループで比較 ==========

    time0 = time.time()
    print("\n=== 二重ループ(i, j) Exist in [%s] ===" %(args[1]))
    for user in my_csv.getDiff_oldversion(lines1, lines2):
        print(user)
    time1 = time.time()
    print("time : %f[s]" %(time1 - time0))

    # ========== 配列格納後に比較 ==========

    time0 = time.time()
    print("\n=== 配列に格納後にループ Exist in [%s] ===" %(args[1]))
    for user in my_csv.getDiff(lines1, lines2):
        print(user)
    time1 = time.time()
    print("time : %f[s]" %(time1 - time0))

    # =====================================

    # ========== 二重ループで比較 ==========

    time0 = time.time()
    print("\n=== 二重ループ(i, j) Exist in [%s] ===" %(args[2]))
    for user in my_csv.getDiff_oldversion(lines2, lines1):
        print(user)
    time1 = time.time()
    print("time : %f[s]" %(time1 - time0))

    # ========== 配列格納後に比較 ==========

    time0 = time.time()
    print("\n=== 配列に格納後にループ Exist in [%s] ===" %(args[2]))
    for user in my_csv.getDiff(lines2, lines1):
        print(user)
    time1 = time.time()
    print("time : %f[s]" %(time1 - time0))

    # =====================================



    print()

if __name__ == "__main__":
    main()
