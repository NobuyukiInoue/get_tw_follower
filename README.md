# get_follower

This program acquires follower information of Twitter.
  

## system
*Python 3.6 or Later
*pandas 1.4.1
*tweepy 4.5.0

## Download

```
>git clone https://github.com/gx3n-inue/get_follower
```

## Run
  
```
>python get_follower.py
```
  

## LICENSE
  
get_follower ver1.02
This project is licensed under the terms of the MIT license, see LICENSE.  


## 注意

### 2020/10/27

pyhon 3.7.0 では、"async"予約語となっており、

```
File "(途中省略)/site-packages/tweepy/streaming.py", line 358
    def _start(self, async):
```
が発生します。

上記のエラーが表示される場合は、site-packages/tweepy/streaming.pyの async を
別の変数名に置き換えるなどしてください。


### 2020/12/23

Python 3.9.1 では、Windows10 2004 環境において下記のようなエラーが発生するようです。

```
timeError: The current Numpy installation ('C:\\Programs\\Python\\Python39\\lib\\site-packages\\numpy\\__init__.py') fails to pass a sanity check due to a bug in the windows runtime. See this issue for more information: https://tinyurl.com/y3dm3h86
```

ucrtbase.dll10.0.19041.488 の不具合のようです。
