# coding: utf-8

from requests_oauthlib import OAuth1Session
import json
import my_key

# タイムライン取得用のURL
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

# とくにパラメータは無い
params = {}

# OAuth で GET
twitter = OAuth1Session(my_key.consumer_key, my_key.consumer_secret, my_key.access_token_key, my_key.access_token_secret)
req = twitter.get(url, params = params)

if req.status_code == 200:
    # print(req.text)

    # レスポンスはJSON形式なので parse する
    timeline = json.loads(req.text)
    # 各ツイートの本文を表示
    for tweet in timeline:
        print(tweet["text"])

else:
    # エラーの場合
    print ("Error: %d" % req.status_code)
