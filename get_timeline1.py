# coding: utf-8

'''
python-twitterを利用して、pythonでTwitterを操作する。
https://qiita.com/ti-ginkgo/items/90914db1dc7e229c69c7
'''

import my_key
import twitter
from pandas import DataFrame
from datetime import datetime


def auth():
    """認証"""

    #利用制限にひっかかた時に必要時間待機する
    twitter_api = twitter.Api(my_key.consumer_key, my_key.consumer_secret, my_key.access_token_key, my_key.access_token_secret)

    return twitter_api


def main():
    screen_name = "NobuyukiIoue" # @NobuyukiIoue のフォロワーを検索します。
    
    twitter_api = auth()
    
    statuse = twitter_api.GetUserTimeline(twitter_api.VerifyCredentials().id, count=200)

    # countに指定した個数のタイムラインを取得することができます。
    # 取得できる最大値は200です。

    print("##------------------------------------------------##")
    print("## 直近のTimeLine表示")
    print("##------------------------------------------------##")

    for s in statuse:
        print(s.text)
    # タイムラインの内容が表示されます。

    print("##------------------------------------------------##")
    print("## 直近のtweet表示")
    print("##------------------------------------------------##")

    friends = twitter_api.GetFriends()
    for i,friend in enumerate(friends):
        if i > 5:
            break
        friends_statuse = twitter_api.GetUserTimeline(friend.id, count=5)
        print(friend.name) # ユーザー名
        for f_s in friends_statuse:
            print(f_s.text) # ツイートの内容
        print() # 改行


if __name__ == "__main__":
    main()
