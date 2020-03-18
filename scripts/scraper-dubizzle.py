import requests
import time
from bs4 import BeautifulSoup
import json
from src.models.dubizzle import Dubizzle
from dataclasses import asdict, astuple, replace
from pymongo import MongoClient
import random


client = MongoClient("mongodb+srv://prop_analyzer:prop_analyzer123@cluster-prop-analyzer-0-otjuz.mongodb.net/test?retryWrites=true&w=majority")
db = client.property_analyzer
prop_collection = db.properties


l_listing_type = "Sale"
url_base_apt_dubai = "https://dubai.dubizzle.com/en/property-for-sale/residential/apartmentflat/?page="
url_base_res_sale_uae = "https://uae.dubizzle.com/en/property-for-sale/residential/?sort=newest&page="
url_base_comm_sale_uae = "https://uae.dubizzle.com/en/property-for-sale/commercial/?sort=newest&page="
url_base_res_rent_uae = "https://uae.dubizzle.com/en/property-for-rent/residential/?sort=newest&page="
url_base_comm_rent_uae = "https://uae.dubizzle.com/en/property-for-rent/commercial/?sort=newest&page="
url_base = url_base_comm_sale_uae

for i in range(0, 500):
    url = url_base + str(i)
    do = True
    while(do):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        try:
            scripts = soup.find_all('script')

            for s in scripts:
                if 'algolia' in s.text:
                    lines = s.text.split("\n")
                    jsontstr = lines[5].replace("window.__INITIAL_STATE__ = JSON.parse(\"","").replace("\\","").replace("\");","")
                    #print(jsontstr)
                    listings = json.loads(jsontstr)['results']['results']['hits']
                    for listing in listings:
                        try:
                            dub = Dubizzle(
                            source = "Dubizzle",
                            listing_name = listing['name']['en'] if 'name' in listing else None,
                            city = listing['city']['name']['en'] if 'city' in listing else None,
                            city_id = listing['city']['id'] if 'city' in listing else None,
                            image_url = listing['photo']['main'] if 'photo' in listing and listing['photo'] is not None else None,
                            price = listing['price'] if 'price' in listing else None,
                            detail_url = listing['absolute_url']['en'] if 'absolute_url' in listing else None,
                            agent_name = listing['agent']['name']['en'] if 'agent' in listing and listing['agent'] is not None else None,
                            agent_id = listing['agent']['id'] if 'agent' in listing and listing['agent'] is not None else None,
                            posted_date = listing['added'] if 'added' in listing else None,
                            categories_ids = listing['categories']['ids'] if 'categories' in listing else None,
                            categories_tags = listing['categories']['slug'] if 'categories' in listing else None,
                            categories_names = listing['categories']['name']['en'] if 'categories' in listing else None,
                            lat = listing['_geoloc']['lat'] if '_geoloc' in listing and listing['_geoloc'] is not None  else None,
                            lng = listing['_geoloc']['lng'] if '_geoloc' in listing and listing['_geoloc'] is not None  else None,
                            promoted = listing['promoted'] if 'promoted' in listing else None,
                            area_sqft = listing['size'] if 'size' in listing else None,
                            num_bathrooms = listing['bathrooms'] if 'bathrooms' in listing else None,
                            num_bedrooms = listing['bedrooms'] if 'bedrooms' in listing else None,
                            neighborhoods_ids = listing['neighborhoods']['ids'] if 'neighborhoods' in listing else None,
                            neighborhoods_names = listing['neighborhoods']['name']['en'] if 'neighborhoods' in listing else None,
                            listing_type = l_listing_type,
                            country = "UAE",
                            developer="",
                            price_currency="AED",
                            furnished= listing['furnished'] if 'furnished' in listing else None,
                            building= listing['building'] if 'building' in listing else None,
                            rent_is_paid_short= listing['rent_is_paid']['short_name']['en'] if 'rent_is_paid' in listing and listing['rent_is_paid'] is not None else None,
                            rent_is_paid_name= listing['rent_is_paid']['name']['en'] if 'rent_is_paid' in listing and listing['rent_is_paid'] is not None else None,
                            listing_id= 'dubizzle_' + str(listing['id'])
                            )
                            data = asdict(dub)
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