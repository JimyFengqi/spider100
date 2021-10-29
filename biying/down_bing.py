# -*- coding: utf-8 -*-
# @Author  : Fengqi(jmps515@163.com)
# @Time    : 2021/10/29 下午6:18
# @File    : down_biying.py
# @Software: PyCharm
# @Python  : 3.6

import json
import os
import urllib.request
import datetime


def create_dir(dir_path):
    if not os.path.exists(dir_path):
        print('current path not exist[%s]' % dir_path)
        os.makedirs(dir_path)

gallery_name = 'gallery'
bing_name = 'bing'

HOME = os.getcwd()
HOME = os.path.join(HOME, gallery_name)
pic_dir = os.path.join(HOME, bing_name)
create_dir(pic_dir)
bing_json_file = os.path.join(pic_dir, 'bing.json')


date = datetime.datetime.now().strftime('%Y%m%d')
yesterday = pic_dir + str(int(date) - 1)
json_url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=7"  # where to get the json file
bing_url = "https://www.bing.com"  # bing.com main domain


urllib.request.urlretrieve(json_url, bing_json_file)

with open(bing_json_file, "r", encoding='utf-8') as f:
    bing_json = json.load(f)


imges = bing_json['images']
for image in imges:
    imgurl = bing_url + image['url']
    current_pic_date = image['startdate']
    current_pic_year_dir = current_pic_date[0:4]
    current_pic_month_dir = current_pic_date[4:6]
    imgname = os.path.join(pic_dir, current_pic_year_dir)
    imgname = os.path.join(imgname, current_pic_month_dir)
    create_dir(imgname)
    imgname = os.path.join(imgname, image['startdate'] + '.jpg')

    if not os.path.exists(imgname):
        urllib.request.urlretrieve(imgurl, imgname)
