# coding: utf-8

import sys
import os
from mylibs import my_fileList
from mylibs import my_twitter
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

    screen_name = "NobuyukiIoue" # search "@NobuyukiIoue"'s follower.
    
    twitter_api = my_twitter.auth()
    id_list = my_twitter.getIds(Api = twitter_api, Id = screen_name)
    follower_list = my_twitter.getFlds(Api = twitter_api, id_list = id_list)

    lines1 = my_csv.readCSVfile(fileList[len(fileList) - 1])

    print("\n=== Added in Now Follower ===")
    for user in my_csv.getDiff_Now_to_Latest(follower_list, lines1):
        print(user)

    print("\n=== Existed in [%s] ===" %(fileList[len(fileList) - 1]))
    for user in my_csv.getDiff_Latest_to_Now(follower_list, lines1):
        print(user)

    print()

if __name__ == "__main__":
    main()
