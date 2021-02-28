from src.common.config import cfg
import boto3


class DynamodbClient:

    def __init__(self):
        dynamodb_config = cfg["dynamodb"]
        self.dynamodb_local = boto3.resource('dynamodb', endpoint_url=dynamodb_config["endpoint_url"], region_name=dynamodb_config["region_name"])
        self.dynamodb_aws = boto3.resource('dynamodb', region_name=dynamodb_config["region_name"],
                                      aws_access_key_id=dynamodb_config["aws_access_key_id"],
                                      aws_secret_access_key=dynamodb_config["aws_secret_access_key"], )
