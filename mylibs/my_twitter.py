# coding: utf-8

import tweepy

# キー情報読み込み
from . import my_key


def auth():
    """認証"""

    # ハンドルセット
    auth = tweepy.OAuthHandler(my_key.consumer_key, my_key.consumer_secret)
    auth.set_access_token(my_key.access_token_key, my_key.access_token_secret)

    #利用制限にひっかかた時に必要時間待機する
    twitter_api = tweepy.API(auth, wait_on_rate_limit = True)

    return twitter_api


def getIds(Api, Id):
    """Idで指定されたユーザの全フォロワーを取得する"""

    # Cursorを使ってフォロワーのidを逐次的に取得
    followers_ids = tweepy.Cursor(Api.followers_ids, id = Id, cursor = -1).items()

    try:
        followers_ids_list = [id for id in followers_ids]
    except tweepy.error.TweepError as e:
        print(e.reason)

    return followers_ids_list


def getFlds(Api, id_list):
    """ユーザー情報をlookupし、主要プロパティを取得する"""

    users = Api.lookup_users(user_ids=id_list)

    follower_list = []
    apend = follower_list.append

    # ヘッダ行の出力
    apend(["id", "screen_name", "location", "description", "followers_count", "following"])

    for user in users:
        apend([user.id, user.screen_name, user.location, user.description, user.followers_count, user.following])

    return follower_list
