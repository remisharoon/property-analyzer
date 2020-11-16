from datetime import datetime
import os
from src.connections.ibm_client import IBMClient
from src.common.config import cfg
from src.io.file_client import FileClient
from typing import List

class FileReader(FileClient):

    def __init__(self):
        FileClient.__init__(self)

    def download_from_cloud(self, bucket_name,folder_name, file_name, dest_folder):
        file_key = os.path.join(folder_name, file_name)
        # self.ibm_client.cos.download_file(Bucket=bucket_name, Key='2020_07_17/pa_raw_data_2020_09_26_08_17_50.json', Filename='pa_raw_data_2020_09_26_08_17_50.json')
        # self.ibm_client.cos.download_file(Bucket=bucket_name, Key='2020_07_17/*', Filename='*.json')
        dest_folder_full_path = os.path.join(dest_folder, folder_name)
        if not os.path.exists(dest_folder_full_path):
            os.makedirs(dest_folder_full_path)

        dest_file_full_path = os.path.join(dest_folder_full_path, file_name)

        if os.path.exists(dest_file_full_path):
            print("File already exists in the local system, no need to download")
        else:
            self.ibm_client.cos.download_file(Bucket=bucket_name, Key=file_key, Filename=dest_file_full_path)

    def get_all_files_keys(self, bucket_name: str) -> List[object]:
        # file_keys = self.ibm_client.list_keys(bucket_name)
        file_keys = self.ibm_client.cos.list_objects(Bucket = bucket_name)
        #print(",".join(file_keys.name))
        #return [file.name for file in file_keys]
        return file_keys

    def download_all_files(self):
        bucket_name = 'pa-raw-data'
        keys =  self.get_all_files_keys(bucket_name="pa-raw-data")['Contents']
        for file_key in keys:
            print(file_key)
            key = file_key['Key']
            file_components = key.split("/")
            folder_name = file_components[0]
            file_name = file_components[1]
            self.download_from_cloud(bucket_name=bucket_name, folder_name=folder_name, file_name=file_name, dest_folder= '../../data')

if __name__ == "__main__":
    fr = FileReader()
    # fr.get_all_files('pa-raw-data')
    # fr.download_from_cloud(bucket_name='pa-raw-data', folder_name='2020_07_17', file_name = 'pa_raw_data_2020_09_26_08_17_50.json', dest_folder='../../data')
    fr.download_all_files()