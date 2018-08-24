# coding: utf-8

from datetime import datetime
from pandas import DataFrame
from mylibs import my_twitter

def main():
    screen_name = "NobuyukiIoue" # @NobuyukiIoue のフォロワーを検索します。

    twitter_api = my_twitter.auth()
    id_list = my_twitter.getIds(Api = twitter_api, Id = screen_name)
    follower_list = my_twitter.getFlds(Api = twitter_api, id_list = id_list)

    dtstr = datetime.now().strftime("%Y%m%d_%H%M%S")

    # DataFrame(follower_list).to_csv("twitter_follower_" + dtstr + ".csv" ,header = None, index_label = "id", encoding="sjis")
    # DataFrame(follower_list).to_csv("twitter_follower_" + dtstr + ".csv" ,header = None, index_label = "id", encoding="utf-16")
    DataFrame(follower_list).to_csv("twitter_follower_" + dtstr + ".csv" ,header = None, index_label = "id")

if __name__ == "__main__":
    main()
