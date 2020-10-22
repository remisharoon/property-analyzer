from datetime import datetime
import os
from src.connections.ibm_client import IBMClient
from src.common.config import cfg
from src.io.file_client import FileClient


class FileReader(FileClient):

    def __init__(self):
        FileClient.__init__(self)

    def download_from_cloud(self, folder_path, bucket_name):
        self.cos.download_file(Bucket=bucket_name, Key='wine.csv', Filename='data/wine1.csv')

    def get_all_files(self, bucket_name):
        file_keys = self.ibm_client.list_keys(bucket_name)
        for key in file_keys:
            print(key.name)

if __name__ == "__main__":
    fr = FileReader()
    # fr.get_all_files('pa-raw-data')
    fr.download_from_cloud('pa-raw-data', '2020_07_17/pa_raw_data_2020_09_26_08_17_50.json')