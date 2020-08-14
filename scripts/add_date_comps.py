from pymongo import MongoClient
import datetime

# client = MongoClient("mongodb+srv://prop_analyzer:prop_analyzer123@cluster-prop-analyzer-0-otjuz.mongodb.net/test?retryWrites=true&w=majority")
client = MongoClient('localhost', 27017)
db = client.property_analyzer_db
prop_collection = db.prop_collection


cursor = prop_collection.find({"source":"Propertyfinder", "listing_type":"Sale"},no_cursor_timeout=True).batch_size(50)
for doc in cursor:
    try:
        dt = doc["posted_date"]
        # doc["date_time"] = dt
        doc["year"] = dt.year
        doc["month"] = dt.month
        doc["day"] = dt.day
        print("year", doc["year"])
        print("month", doc["month"])
        print("day", doc["day"])
        key = {'listing_id': doc['listing_id']}
        prop_collection.replace_one(key, doc, True)

    except Exception as e:
        print(str(e))
        print(doc)

cursor.close()