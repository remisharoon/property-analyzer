import requests
import time
from bs4 import BeautifulSoup
import json
from src.models.propertyfinder import Propertyfinder
from dataclasses import asdict, astuple, replace
from pymongo import MongoClient
import random


client = MongoClient("mongodb+srv://prop_analyzer:prop_analyzer123@cluster-prop-analyzer-0-otjuz.mongodb.net/test?retryWrites=true&w=majority")
db = client.property_analyzer
prop_collection = db.properties


l_listing_type = "Sale"
url_base_res_sale_uae = "https://www.propertyfinder.ae/en/search?c=1&ob=nd&page="
url_base = url_base_res_sale_uae

for i in range(1500, 1700):
    url = url_base + str(i)
    do = True
    while(do):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        try:
            scripts = soup.find_all('script')

            for s in scripts:
                if 'window.propertyfinder.settings.search' in s.text:
                    lines = s.text.split("\n")
                    for line in lines:
                        if "payload" in line:
                            jsontstr = line.replace("payload: ","").rstrip(",")
                            #print(jsontstr)
                            listings = json.loads(jsontstr)['included']
                            for listing in listings:
                                try:
                                    attributes = listing['attributes']
                                    pf = Propertyfinder(
                                    source = "Propertyfinder",
                                    listing_name = attributes['name'] if 'name' in attributes else None,
                                    city = attributes['location_tree_path'].split(",")[-1] if 'location_tree_path' in attributes else None,
                                    #city_id = listing['city']['id'] if 'city' in listing else None,
                                    city_id = None,
                                    image_url = listing['links']['image_property'] if 'image_property' in listing['links'] and listing['links']['image_property'] is not None else None,
                                    price = attributes['default_price'] if 'default_price' in attributes else None,
                                    detail_url = listing['links']['self'] if 'links' in listing else None,
                                    agent_name = listing['agent']['name']['en'] if 'agent' in listing and listing['agent'] is not None else None,
                                    agent_id = listing['relationships']['agent']['data']['id'] if 'relationships' in listing and listing['relationships'] is not None else None,
                                    posted_date = listing['added'] if 'added' in listing else None,
                                    categories_ids = listing['categories']['ids'] if 'categories' in listing else None,
                                    categories_tags = attributes['type_identifier'] if 'type_identifier' in attributes else None,
                                    categories_names = attributes['type_identifier'] if 'type_identifier' in attributes else None,
                                    lat = listing['geo']['latitude'] if 'geo' in listing and listing['geo'] is not None  else None,
                                    lng = listing['geo']['longitude'] if 'geo' in listing and listing['geo'] is not None  else None,
                                    promoted = attributes['smart_ad'] if 'smart_ad' in attributes else None,
                                    area_sqft = attributes['size'] if 'size' in attributes else None,
                                    size_unit=attributes['size_unit'] if 'size_unit' in attributes else None,
                                    num_bathrooms = attributes['bathroom_value'] if 'bathroom_value' in attributes else None,
                                    num_bedrooms = attributes['bedroom_value'] if 'bedroom_value' in attributes else None,
                                    neighborhoods_ids = listing['neighborhoods']['ids'] if 'neighborhoods' in listing else None,
                                    neighborhoods_names = attributes['location_tree_path'].split(",") if 'location_tree_path' in attributes else None,
                                    completion_status = attributes['completion_status'] if 'completion_status' in attributes else None,
                                    contact_options=listing['meta']['contact_options'] if 'meta' in listing else None,
                                    listing_type = l_listing_type,
                                    country = attributes['price_period_label'] if 'price_period_label' in attributes else None,
                                    developer="",
                                    price_currency="AED",
                                    furnished= attributes['furnished'] if 'furnished' in attributes else None,
                                    building= listing['building'] if 'building' in listing else None,
                                    rent_is_paid_short= listing['rent_is_paid']['short_name']['en'] if 'rent_is_paid' in listing and listing['rent_is_paid'] is not None else None,
                                    rent_is_paid_name= listing['rent_is_paid']['name']['en'] if 'rent_is_paid' in listing and listing['rent_is_paid'] is not None else None,
                                    listing_id= 'propertyfinder_' + str(listing['id'])
                                    )
                                    data = asdict(pf)
                                    print(data)
                                    key = {'listing_id': data['listing_id']}
                                    prop_collection.replace_one(key, data, True)
                                except Exception as e:
                                    print(e)
                                do = False
        except Exception as e:
            print(e)
            do = True
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