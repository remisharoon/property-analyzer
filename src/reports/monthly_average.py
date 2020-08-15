from src.reports.base_report import BaseReport
import pprint
from bson.son import SON
import csv
class MonthlyAverage(BaseReport):
    year: int
    month: int

    def getAverage(self):
        self.prop_collection
        # pprint.pprint(self.prop_collection.find_one())
        pipeline = [
            { "$match": {"source":"Propertyfinder", "listing_type":"Sale"}},
            {"$group": {"_id": {"city":"$city","bedrooms":"$num_bedrooms","year":"$year","month":"$month"}, "avgAmount": {"$avg": "$price"}}},
            {"$sort": SON([('year', 1)])}

        ]
        cursor = self.prop_collection.aggregate(pipeline)
        results = list(cursor)
        # pprint.pprint(results)
        with open('avg_price.csv', 'w', newline='\n', encoding='utf-8') as csv_file:
            fieldnames = ['city', 'bedrooms', 'year', 'month', 'price']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for rec in results:
                try:
                    cols = rec["_id"]
                    row = dict()
                    row['city'] = cols["city"].strip()
                    row['bedrooms'] = cols["bedrooms"]
                    row['year'] = cols["year"]
                    row['month'] = cols["month"]
                    row['price'] = rec["avgAmount"]
                    writer.writerow(row)
                except Exception as e:
                    pprint.pprint(e)


if __name__ == "__main__":
    ma = MonthlyAverage()
    print(ma.client.server_info())
    ma.getAverage()




