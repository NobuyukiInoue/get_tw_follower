# coding: utf-8

import sys
import os
from mylibs import my_fileList
from mylibs import my_csv

def main():
    args = sys.argv
    argc = len(args)

    if argc != 3:
        print("Usage: python %s file1 file2" %(args[0]))
        exit(0)

    my_fileList.fileCheck(args[1])
    my_fileList.fileCheck(args[2])

    lines1 = my_csv.readCSVfile(args[1])
    lines2 = my_csv.readCSVfile(args[2])

    print("\n=== Exist in [%s] ===" %(args[1]))
    my_csv.getDiff(lines1, lines2)
    for user in my_csv.getDiff(lines1, lines2):
        print(user)

    print("\n=== Exist in [%s] ===" %(args[2]))
    for user in my_csv.getDiff(lines2, lines1):
        print(user)

    print()

if __name__ == "__main__":
    main()
