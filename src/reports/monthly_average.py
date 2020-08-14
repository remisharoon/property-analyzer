from src.reports.base_report import BaseReport
import pprint

class MonthlyAverage(BaseReport):
    year: int
    month: int

    def getAverage(self):
        self.prop_collection
        # pprint.pprint(self.prop_collection.find_one())
        pipeline = [
            { "$match": {"source":"Propertyfinder", "listing_type":"Sale", "city": " Dubai"}},
            {"$group": {"_id": {"city":"$city","bedrooms":"$num_bedrooms","year":"$year","month":"$month"}, "avgAmount": {"$avg": "$price"}}}

        ]
        cursor = self.prop_collection.aggregate(pipeline)
        result = list(cursor)
        pprint.pprint(result)


if __name__ == "__main__":
    ma = MonthlyAverage()
    print(ma.client.server_info())
    ma.getAverage()




