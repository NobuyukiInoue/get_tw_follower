# coding: utf-8

import os
import pandas


def getDateStr(targetStr):
    """twitter_follower_yyyymmdd_HHmmss.csvから日付時刻の文字列を得る"""
    flds = os.path.basename(targetStr).split("_")

    if len(flds) >= 3:
        dateStrWork = flds[2] + flds[3]
        dateStr = dateStrWork.split(".")
    
        return dateStr[0]

    else:
        return ""


def readCSVfile(fileName):
    """twitter_follower_yyyymmdd_hhMMss.csv を開く"""
    lines = pandas.read_csv(fileName, encoding="utf8")
    return lines


def getDiff_oldversion(lines1, lines2):
    """２つのcsv配列を比較し、２つめの配列にないレコードのidを返す"""
    hit = False
    for i in range(0, len(lines1)):
        for j in range(0, len(lines2)):
            if lines1.id[i] == lines2.id[j]:
                hit = True
                break
        if hit == False:
            yield("%s:%s,%s" %(lines1.id[i], lines1.screen_name[i], lines1.followers_count[i]))


def getDiff(lines1, lines2):
    """２つのcsv配列を比較し、２つめの配列にないレコードのidを返す"""
    hit = False

    targes = [id2 for id2 in lines2.id]
    for i in range(0, len(lines1)):
        if lines1.id[i] in targes:
            hit = True
            break
        if hit == False:
            yield("%s:%s,%s" %(lines1.id[i], lines1.screen_name[i], lines1.followers_count[i]))


def getDiff_Now_to_Latest_oldversion(lines0, lines1):
    """[最新の読み込みデータ]と[読み込んだファイルのcsv配列]を比較し、"""
    """２つめの配列にないレコードのidを返す"""
    result = False
    hit = False

    for i in range(1, len(lines0)):
        for j in range(0, len(lines1)):
            if lines0[i][0] == lines1.id[j]:
                hit = True
                break
        if hit == False:
            result = True
            print("%s:%s,%s" %(lines0[i][0], lines0[i][1], lines0[i][4]))
    if result == False:
        print("All id is existing.")


def getDiff_Latest_to_Now_oldversion(lines0, lines1):
    """[読み込んだファイルのcsv配列]と[最新の読み込みデータ]を比較し、"""
    """２つめの配列にないレコードのidを返す"""
    
    result = False
    hit = False

    for i in range(0, len(lines1)):
        for j in range(1, len(lines0)):
            if lines1.id[i] == lines0[j][0]:
                hit = True
                break
        if hit == False:
            result = True
            print("%s:%s,%s" %(lines1.id[i], lines1.screen_name[i], lines1.followers_count[i]))
    if result == False:
        print("All id was existed.")


def getDiff_Now_to_Latest(lines0, lines1):
    """[最新の読み込みデータ]と[読み込んだファイルのcsv配列]を比較し、"""
    """２つめの配列にないレコードのidを返す"""
    result = False

    targets = [id1 for id1 in lines1.id]
    for user in lines0:
        if user[0] == "id":
            continue
        if user[0] in targets:
            continue
        else:
            result = True
            yield("%s:%s,%s" %(user[0], user[1], user[4]))

    if result == False:
        yield("All id is existing.")


def getDiff_Latest_to_Now(lines0, lines1):
    """[読み込んだファイルのcsv配列]と[最新の読み込みデータ]を比較し、"""
    """２つめの配列にないレコードのidを返す"""
    result = False

    targets = [id0[0] for id0 in lines0]
    for i in range(0, len(lines1)):
        if lines1.id[i] in targets:
            continue
        else:
            result = True
            yield("%s:%s,%s" %(lines1.id[i], lines1.screen_name[i], lines1.followers_count[i]))

    if result == False:
        yield("All id was existed.")
