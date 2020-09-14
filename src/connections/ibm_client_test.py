from src.connections.ibm_client import IBMClient
from src.common.config import cfg

ibm_client = IBMClient(cfg)
ibm_client.list_buckets()


ibm_client.upload_file_cos("pa-raw-data", "test.txt", "test.txt")
