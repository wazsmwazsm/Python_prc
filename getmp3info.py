#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import os, eyed3
import MySQLdb

# 获取音频信息，构造数据
music = './music';
data = []

for dir_name in os.listdir(music):
    for file_name in os.listdir(music + '/' + dir_name):
        audiofile = eyed3.load(music + '/' + dir_name + '/' + file_name)
        data.append({
            'statue': 2,
            'group': dir_name,
            'group_sort': 0,
            'name':file_name,
            'artist': audiofile.tag.artist,
            'time':audiofile.info.time_secs,
            'url':'music_new_library/'+ dir_name + '/' + file_name,
            'desc': '',
            'app_name': 'all',
            'country_name': 'all',
            'language': 'all',
            'package_name': 'all',
            'channel': 'all',
        })

# 连接数据库
db = MySQLdb.connect(host="localhost",user="homestead",passwd="secret",db="ad_show_control_db" )
cursor = db.cursor()

try:
    # 构建语句
    sql = "insert into material_audio_new_info "+                                   \
          "(`statue`,`group`,`group_sort`,`name`,`artist`,`time`,`url`,"+           \
          "`desc`,`app_name`,`country_name`,`language`,`package_name`,`channel`)"+  \
          " values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)";

    # 构建参数
    param = []
    for row in data:
        param.append([row['statue'],row['group'],row['group_sort'],row['name'],     \
        row['artist'],row['time'],row['url'],row['desc'],row['app_name'],           \
        row['country_name'],row['language'],row['package_name'],row['channel']])
    # 执行语句
    cursor.executemany(sql, param)
    db.commit()

except Exception as e:
    # 回滚事务
    print e
    db.rollback()


# from pathlib import Path
# audiofile = eyed3.load("./Heaven Is Free.mp3")
# # print(dir(audiofile.path))
# print(audiofile.tag.artist)
# print(audiofile.info.time_secs)
# print(audiofile.tag.title)
#
# path = Path(music)
# for dir_name in path.iterdir():
#     for file_name in Path(dir_name).iterdir():
#         print(file_name)
