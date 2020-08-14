from pymongo import MongoClient

cloudClient = MongoClient("mongodb+srv://prop_analyzer:prop_analyzer123@cluster-prop-analyzer-0-otjuz.mongodb.net/test?retryWrites=true&w=majority")
localClient = MongoClient('localhost', 27017)

clouddb = cloudClient.property_analyzer
cloud_collection = clouddb.properties

localdb = localClient.property_analyzer_db
local_collection = localdb.prop_collection

cloudcursor = cloud_collection.find({})

numdocs = 0
for doc in cloudcursor:
    numdocs = numdocs + 1
    print(doc['listing_id'], numdocs)
    key = {'listing_id': doc['listing_id']}
    local_collection.replace_one(key, doc, True)