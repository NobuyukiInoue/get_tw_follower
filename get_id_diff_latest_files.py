# coding: utf-8

import sys
import os
from mylibs import my_fileList
from mylibs import my_csv


def main():
    args = sys.argv
    argc = len(args)

    if argc <= 1:
        print("Usage: python %s dirPath" %(args[0]))
        exit(0)

    if not os.path.isdir(args[1]):
        print("%s not found." %(args[1]))
        exit(0)

    fileList = my_fileList.get(args[1] + "\*.csv")

    lines1 = my_csv.readCSVfile(fileList[len(fileList) - 1])
    lines2 = my_csv.readCSVfile(fileList[len(fileList) - 2])

    print("\n=== Exist in [%s] ===" %(fileList[len(fileList) - 1]))
    for user in my_csv.getDiff(lines1, lines2):
        print(user)

    print("\n=== Exist in [%s] ===" %(fileList[len(fileList) - 2]))
    for user in my_csv.getDiff(lines2, lines1):
        print(user)

    print()

if __name__ == "__main__":
    main()
