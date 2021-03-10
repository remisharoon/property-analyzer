from src.reports.base_report import BaseReport
import pprint
from bson.son import SON
import csv
import os
import json
import pandas as pd

class MonthlyAverage(BaseReport):
    year: int
    month: int

    def read_all_recs(self):
        data_dicts = []
        for root, dirs, files in os.walk('../../data'):
            for file in files:
                with open(os.path.join(root, file), "r") as json_data_file:
                    json_lines = json_data_file.readlines()
                    for jsonstr in json_lines:
                        print(jsonstr)
                        json_data = json.loads(jsonstr)
                        data_dict = {}
                        data_dict['source'] = json_data['source'].strip()
                        data_dict['listing_type'] = json_data['listing_type'].strip()
                        data_dict['num_bedrooms'] = json_data['num_bedrooms']
                        data_dict['city'] = json_data['city'].strip()
                        data_dict['year'] = json_data['year']
                        data_dict['month'] = json_data['month']
                        data_dict['price'] = json_data['price']
                        data_dicts.append(data_dict)
        df = pd.DataFrame(data_dicts)
        # print(df.head())
        return df

    def getAverage(self):
        # self.prop_collection
        # pprint.pprint(self.prop_collection.find_one())
        # pipeline = [
        #     { "$match": {"source":"Propertyfinder", "listing_type":"Sale"}},
        #     {"$group": {"_id": {"city":"$city","bedrooms":"$num_bedrooms","year":"$year","month":"$month"}, "avgAmount": {"$avg": "$price"}}},
        #     {"$sort": SON([('year', 1)])}
        #
        # ]
        # cursor = self.prop_collection.aggregate(pipeline)
        # results = list(cursor)
        # pprint.pprint(results)
        df = self.read_all_recs()
        print(df.head(2))
        df_avg = df.groupby(['city', 'num_bedrooms', 'year', 'month', 'source', 'listing_type']).mean().reset_index()
        # print(df_avg.head())

        # df_avg.to_csv('avg_price.csv', sep=",", index=False)
        df_avg = pd.read_csv('avg_price.csv')
        dubai_2br_monthly_avg = df_avg.loc[(df_avg['city'] == 'Dubai') & (df_avg['num_bedrooms'] == 2.0)]
        print(dubai_2br_monthly_avg.head())
        # with open('avg_price.csv', 'w', newline='\n', encoding='utf-8') as csv_file:
        #     fieldnames = ['city', 'bedrooms', 'year', 'month', 'price']
        #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        #     writer.writeheader()
        #     for rec in results:
        #         try:
        #             cols = rec["_id"]
        #             row = dict()
        #             row['city'] = cols["city"].strip()
        #             row['bedrooms'] = cols["bedrooms"]
        #             row['year'] = cols["year"]
        #             row['month'] = cols["month"]
        #             row['price'] = rec["avgAmount"]
        #             writer.writerow(row)
        #         except Exception as e:
        #             pprint.pprint(e)


if __name__ == "__main__":
    ma = MonthlyAverage()
    # ma.getAverage()
    ma.getAverage()




