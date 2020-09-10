from ibm_botocore.client import Config
import ibm_boto3

class IBMClient(object):

    def __init__(self, config):
        self.config = config
        self.credentials = self.config["ibm_credentials"]
    def connect(self):
        self.cos = ibm_boto3.client(service_name='s3',
                               ibm_api_key_id=self.credentials['IBM_API_KEY_ID'],
                               ibm_service_instance_id=self.credentials['IAM_SERVICE_ID'],
                               ibm_auth_endpoint=self.credentials['IBM_AUTH_ENDPOINT'],
                               config=Config(signature_version='oauth'),
                               endpoint_url=self.credentials['ENDPOINT'])

    def upload_file(self, filename, key):
        self.cos.upload_file(Filename='wine/wine.csv', Bucket=self.credentials['BUCKET'], Key='wine_data.csv')


    def list_buckets(self):
        for bucket in self.cos.list_buckets()['Buckets']:
            print(bucket['Name'])

# if __name__ == "__main__":
#
#     ibm_client = IBMClient()
#     ibm_client.list_buckets()