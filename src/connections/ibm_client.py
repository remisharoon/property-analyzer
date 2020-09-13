from ibm_botocore.client import Config
import ibm_boto3

class IBMClient:

    def __init__(self, cfg):
        self.cfg = cfg
        cos_credentials = self.cfg["ibm_credentials"]

        auth_endpoint = cos_credentials['auth_endpoint']
        service_endpoint = cos_credentials['service_endpoint']
        self.cos = ibm_boto3.client('s3',
                               ibm_api_key_id=cos_credentials['apikey'],
                               ibm_service_instance_id=cos_credentials['resource_instance_id'],
                               ibm_auth_endpoint=auth_endpoint,
                               config=Config(signature_version='oauth'),
                               endpoint_url=service_endpoint)
    def list_buckets(self):
        for bucket in self.cos.list_buckets()['Buckets']:
            print(bucket['Name'])

    def upload_file_cos(self,bucket, local_file_name,key):
        try:
            res= self.cos.upload_file(Filename=local_file_name, Bucket=bucket,Key=key)
        except Exception as e:
            print(Exception, e)
        else:
            print('File Uploaded')