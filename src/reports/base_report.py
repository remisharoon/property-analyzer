from pymongo import MongoClient

class BaseReport:
    source: str
    listing_type: str
    city: str
    price: float
    num_bedrooms: int

    # client = MongoClient("mongodb+srv://prop_analyzer:prop_analyzer123@cluster-prop-analyzer-0-otjuz.mongodb.net/test?retryWrites=true&w=majority")
    # client = MongoClient('localhost', 27017)
    # db = client.property_analyzer_db
    # prop_collection = db.prop_collection

