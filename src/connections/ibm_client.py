from ibm_botocore.client import Config
import ibm_boto3
from src.common.config import cfg

class IBMClient:

    def __init__(self, cfg):
        self.cfg = cfg
        cos_credentials = self.cfg["ibm_credentials"]

        auth_endpoint = cos_credentials['auth_endpoint']
        service_endpoint = cos_credentials['service_endpoint']
        # self.cos = ibm_boto3.resource('s3',
        self.cos = ibm_boto3.client('s3',
                               ibm_api_key_id=cos_credentials['apikey'],
                               ibm_service_instance_id=cos_credentials['resource_instance_id'],
                               ibm_auth_endpoint=auth_endpoint,
                               config=Config(signature_version='oauth'),
                               endpoint_url=service_endpoint)
    def list_buckets(self):
        # LowLevel API :  self.cos.list_buckets()['Buckets']
        buckets = self.cos.buckets.all()
        for bucket in buckets:
            print(bucket.name)

    def list_keys(self, bucket_name):
        """Get a list of all keys in bucket."""
        keys = []
        kwargs = {'Bucket': bucket_name}
        while True:
            resp =  self.cos.list_objects_v2(**kwargs)
            for obj in resp['Contents']:
                keys.append(obj['Key'])
            try:
                kwargs['ContinuationToken'] = resp['NextContinuationToken']
            except KeyError:
                break
        return keys

    def upload_file_cos(self,bucket, local_file_name,key):
        try:
            print('Uploading file {}'.format(local_file_name))
            res= self.cos.upload_file(Filename=local_file_name, Bucket=bucket,Key=key)
        except Exception as e:
            print(Exception, e)
        else:
            print('File Uploaded, file_name = {}'.format(local_file_name))

    def download_file_cos(self,bucket, file_name,key):
        try:
            res= self.cos.upload_file(Filename=file_name, Bucket=bucket,Key=key)
        except Exception as e:
            print(Exception, e)
        else:
            print('File Uploaded')

    #BROKEN
    def create_folder(self,bucket_name, foler_name):
        self.cos.upload_file(Bucket=bucket_name, Body='', Key= foler_name + '/')


if __name__ == "__main__":
    client = IBMClient(cfg)
    # client.list_buckets()
    client.list_keys("pa-raw-data")