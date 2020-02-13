# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.utils.project import get_project_settings
settings = get_project_settings()
from scrapy.exceptions import DropItem
import ipdb
import pdb
import logging
import datetime




class StockpricefetcherPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py

        # pdb.set_trace()
        return cls (
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )


    def open_spider(self, spider):
    #     ## initializing spider
    #     ## opening db connection
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
       
    def close_spider(self, spider):
    #     ## clean up when spider is closed
        self.client.close()

    def process_item(self, item, spider):
        ## how to handle each post

        # pdb.set_trace()

        client = pymongo.MongoClient(self.mongo_uri)
        db = client.get_database('stockPrices')
        collection = db.tesla_v1
        self.db['tesla_v1'].insert(dict(item))
        logging.debug("Post added to MongoDB")
        return item



        

        