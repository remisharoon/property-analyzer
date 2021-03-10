import os
import requests
import time
import sys
from bs4 import BeautifulSoup
import json
from src.models.propertyfinder import Propertyfinder
from dataclasses import asdict, astuple, replace
from src.parsers.prop_fndr_detail_parser import PropFndrDetailParser
import datetime
from bson import json_util
from src.connections.dynamodb_client import DynamodbClient
from src.io.file_writer import FileWriter

class MyException(Exception):
    pass

def write_to_local(data):
    date_insert = data['date_insert']
    path_prefix = "pa_raw_data"
    if not os.path.isdir(path_prefix):
        os.mkdir(path_prefix)
    folder_path = os.path.join(path_prefix, datetime.datetime.strftime(date_insert, '%Y_%m_%d'))  # path_prefix + '\/' + datetime.datetime.strftime(date_insert, '%Y_%m_%d')
    print("page = ", pagenum, "folder path ::: ", folder_path)
    data_json = json.dumps(data, default=json_util.default)
    fw.write_local(str(folder_path), data_json)

def parse_listing(listing):
    data = {}
    try:
        attributes = listing['attributes']
        pf = Propertyfinder(
            source="Propertyfinder",
            listing_name=attributes['name'] if 'name' in attributes else None,
            city=attributes['location_tree_path'].split(",")[-1] if 'location_tree_path' in attributes else None,
            # city_id = listing['city']['id'] if 'city' in listing else None,
            city_id=None,
            image_url=listing['links']['image_property'] if 'image_property' in listing['links'] and listing['links'][
                'image_property'] is not None else None,
            price=attributes['default_price'] if 'default_price' in attributes else None,
            detail_url=listing['links']['self'] if 'links' in listing else None,
            agent_name=listing['agent']['name']['en'] if 'agent' in listing and listing['agent'] is not None else None,
            agent_id=listing['relationships']['agent']['data']['id'] if 'relationships' in listing and listing[
                'relationships'] is not None else None,
            posted_date=listing['added'] if 'added' in listing else None,
            date_insert=listing['date_insert'] if 'date_insert' in listing else None,
            categories_ids=listing['categories']['ids'] if 'categories' in listing else None,
            categories_tags=attributes['type_identifier'] if 'type_identifier' in attributes else None,
            categories_names=attributes['type_identifier'] if 'type_identifier' in attributes else None,
            lat=listing['geo']['latitude'] if 'geo' in listing and listing['geo'] is not None else None,
            lng=listing['geo']['longitude'] if 'geo' in listing and listing['geo'] is not None else None,
            promoted=attributes['smart_ad'] if 'smart_ad' in attributes else None,
            area_sqft=attributes['size'] if 'size' in attributes else None,
            size_unit=attributes['size_unit'] if 'size_unit' in attributes else None,
            num_bathrooms=attributes['bathroom_value'] if 'bathroom_value' in attributes else None,
            num_bedrooms=attributes['bedroom_value'] if 'bedroom_value' in attributes else None,
            neighborhoods_ids=listing['neighborhoods']['ids'] if 'neighborhoods' in listing else None,
            neighborhoods_names=attributes['location_tree_path'].split(
                ",") if 'location_tree_path' in attributes else None,
            completion_status=attributes['completion_status'] if 'completion_status' in attributes else None,
            contact_options=listing['meta']['contact_options'] if 'meta' in listing else None,
            listing_type=l_listing_type,
            country=attributes['price_period_label'] if 'price_period_label' in attributes else None,
            developer="",
            price_currency="AED",
            furnished=attributes['furnished'] if 'furnished' in attributes else None,
            building=listing['building'] if 'building' in listing else None,
            rent_is_paid_short=listing['rent_is_paid']['short_name']['en'] if 'rent_is_paid' in listing and listing[
                'rent_is_paid'] is not None else None,
            rent_is_paid_name=listing['rent_is_paid']['name']['en'] if 'rent_is_paid' in listing and listing[
                'rent_is_paid'] is not None else None,
            listing_id='propertyfinder_' + str(listing['id'])
        )
        data = asdict(pf)
        pf_listing_id = int(listing['id'])
        listing_url = data['detail_url']
        pfdetail = PropFndrDetailParser(listing_url, pf_listing_id)
        parsed_dict = pfdetail.parse()
        # print("page = ", pagenum, "parsed_dict = ", parsed_dict)
        print("page = ", pagenum)
        # data['posted_date'] = parsed_dict['date_insert']

        # "date_insert": "2020-07-20T22:36:32+00:00"

        date_insert = datetime.datetime.strptime(parsed_dict['date_insert'], "%Y-%m-%dT%H:%M:%S+00:00")
        posted_date_ts = int(date_insert.timestamp())
        data['posted_date_ts'] = posted_date_ts
        data['posted_date'] = date_insert
        data['date_insert'] = date_insert
        data["year"] = date_insert.year
        data["month"] = date_insert.month
        data["day"] = date_insert.day
        data['attributes'] = parsed_dict['attributes']
        data['related_info'] = parsed_dict['related_info']
        print("page = ", pagenum, data['date_insert'])
        key = {'listing_id': data['listing_id'], 'posted_date_ts': posted_date_ts}
        res = prop_table.get_item(Key={'listing_id': data['listing_id'], 'posted_date_ts': posted_date_ts})
        if 'Item' in res:
            item = res['Item']
            print("Item exists in dynamo :", item)
            move_to_cloud()
            # for ikey in keys:
            #     prop_table.put_item(Item={'listing_id': ikey['listing_id'], 'posted_date_ts': ikey['posted_date_ts']})
            # break
            sys.exit()
            raise MyException('stopppppp!')
        else:
            prop_table.put_item(Item={'listing_id': key['listing_id'], 'posted_date_ts': key['posted_date_ts']})
            # keys.append(key)
        # prop_collection.replace_one(key, data, True)

        # path_prefix = "pa_raw_data"
        # if not os.path.isdir(path_prefix):
        #     os.mkdir(path_prefix)
        # folder_path = os.path.join(path_prefix, datetime.datetime.strftime(date_insert,
        #                                                                    '%Y_%m_%d'))  # path_prefix + '\/' + datetime.datetime.strftime(date_insert, '%Y_%m_%d')
        # print("page = ", pagenum, "folder path ::: ", folder_path)
        # data_json = json.dumps(data, default=json_util.default)
        # fw.write_local(str(folder_path), data_json)
    except MyException as e:
        print(e)
        raise MyException("sdkhk")
    except Exception as e:
        print(e)
    return data

def process_listing(listing):
    data = parse_listing(listing)
    write_to_local(data=data)

def process_line(line):
    if "payload" in line:
        jsontstr = line.replace("payload: ", "").rstrip(",")
        listings = json.loads(jsontstr)['included']
        for listing in listings:
            process_listing(listing)

def process_scripts(scripts):
    for s in scripts:
        if 'window.propertyfinder.settings.search' in s.text:
            lines = s.text.split("\n")
            for line in lines:
                process_line(line)

def move_to_cloud():
    fw = FileWriter()
    path_prefix = "pa_raw_data"
    bucket_name = "pa-raw-data"
    fw.move_to_cloud(path_prefix, bucket_name)

ddc = DynamodbClient()
prop_table = ddc.dynamodb_aws.Table("properties")
print(prop_table.table_status)

l_listing_type = "Sale"
url_base_res_sale_uae = "https://www.propertyfinder.ae/en/search?c=1&ob=nd&page="
url_base = url_base_res_sale_uae
fw = FileWriter()
keys = []
start = 1
end = 2000
for pagenum in range(start, end):
    url = url_base + str(pagenum)
    print(url)
    do = True
    while(do):
        try:
            page = requests.get(url, timeout=10)
            soup = BeautifulSoup(page.text, 'html.parser')
            scripts = soup.find_all('script')
            process_scripts(scripts)
        except Exception as e:
            print(e)
            do = False
            #time.sleep(random.randint(1,3))
    #time.sleep(random.randint(1,3))
            





#print(len(scripts))
#print(scripts[7].text)



# # get the repo list
# res_apts_featured = soup.find(class_="featured-list-listings")
#
# res_apts_listings = soup.find(class_="list-listings")
#
# print(len(res_apts_listings))
# print(len(res_apts_featured))
#
# for apt in res_apts_featured:
#     parse_listing(apt)
#
# for apt in res_apts_listings:
#     parse_listing(apt)