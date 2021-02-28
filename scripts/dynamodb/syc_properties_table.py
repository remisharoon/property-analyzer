import os
import json
from src.connections.dynamodb_client import DynamodbClient

ddc = DynamodbClient()
prop_table_local = ddc.dynamodb_local.Table("properties")
prop_table_aws = ddc.dynamodb_aws.Table("properties")

print(prop_table_local.table_status)
print(prop_table_aws.table_status)

for root, dirs, files in os.walk('../../data'):
    for file in files:
        with open(os.path.join(root, file), "r") as json_data_file:
            json_lines = json_data_file.readlines()
            for jsonstr in json_lines:
                json_data = json.loads(jsonstr)
                listing_id = json_data['listing_id'].strip()
                posted_date_ts = json_data['posted_date']['$date']
                print(listing_id, posted_date_ts)
                prop_table_local.put_item(Item={'listing_id': listing_id, 'posted_date_ts':  posted_date_ts})
                prop_table_aws.put_item(Item={'listing_id': listing_id, 'posted_date_ts': posted_date_ts})









