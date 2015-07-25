
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import os
import urllib
import scrapy
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log
from scrapy.http import Request

FILE_NAME = 'meizi_images'

class MongoPipline(object):

    collection_name = 'scrapy_items'

    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]


    def process_item(self, item, spider):
        abs_path = get_abs_path(item)
        save_to_folder(item, abs_path)
        self.collection.insert(dict(item))

        return item

def get_abs_path(item):
    abs_path = os.path.join(os.getcwd(), FILE_NAME)
    print ("DDDDDDDDDDD")
    print (item['title'])
    print ("DDDDDDDDDDD")
    if not os.path.exists(abs_path):
        os.mkdir(abs_path)
    for uri in item['title']:
        abs_paths = os.path.join(abs_path, uri)

        if not os.path.exists(abs_paths):
            os.mkdir(abs_paths)
            yield abs_paths

def save_to_folder(item, abs_path):

    m = []

    for url in item['image']:
        img_name ='1.jpg'
        img_abs_path = os.path.join(abs_path.next(), img_name)
        m.append(img_abs_path)
        print(m)
        item['localImage'] = m
        urllib.urlretrieve(url, img_abs_path)


