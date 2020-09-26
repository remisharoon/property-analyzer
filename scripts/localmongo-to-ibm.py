import os
import requests
import time
from bs4 import BeautifulSoup
import json
from src.models.propertyfinder import Propertyfinder
from dataclasses import asdict, astuple, replace
import random
from src.parsers.prop_fndr_detail_parser import PropFndrDetailParser
import datetime
from src.io.file_writer import FileWriter
from bson import json_util
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.property_analyzer_db
prop_collection = db.prop_collection

fw = FileWriter()

docs = prop_collection.find()

path_prefix = "pa_raw_data"
bucket_name = "pa-raw-data"
if not os.path.isdir(path_prefix):
    os.mkdir(path_prefix)

for rec in docs:
    try:
        print(rec)
        date_insert = rec["date_insert"]
        folder_path = os.path.join(path_prefix, datetime.datetime.strftime(date_insert, '%Y_%m_%d')) #path_prefix + '\/' + datetime.datetime.strftime(date_insert, '%Y_%m_%d')
        print("folder path", folder_path)
        data_json = json.dumps(rec, default=json_util.default)
        fw.write_local(str(folder_path), data_json)
    except Exception as e:
        print(e)


fw.move_to_cloud(path_prefix, bucket_name)
