from datetime import datetime
import os
from src.connections.ibm_client import IBMClient
from src.common.config import cfg

class FileWriter(object):

    def __init__(self):
        self.filename = self._get_file_name()
        self.ibm_client = IBMClient(cfg)

    def _get_file_name(self):
        datestring = datetime.strftime(datetime.now(), '%Y_%m_%d_%H_%M_%S')
        filename = 'pa_raw_data_' + datestring + '.json'
        return filename

    def write_local(self, folder_path, json_str):
        if not os.path.isdir(folder_path):
            print("Folder doesnt exits, lets create")
            os.mkdir(folder_path)
            print("folder created = ", folder_path)
        file_path = os.path.join(folder_path, self.filename)
        print("file_path", file_path)
        f_writer = open(file_path, 'a')
        try:
            f_writer.write(json_str + "\n")
        finally:
            f_writer.close()

        dirs = os.listdir(folder_path)
        print("file written to : ", dirs)

        dirs2 = os.listdir('pa_raw_data')
        print("file in pa_raw_data directory : ", dirs2)


    def move_to_cloud(self, folder_path, bucket_name):
        # cos.upload_file(Filename='wine/wine.csv', Bucket=credentials['BUCKET'], Key='wine_data.csv')
        print(" Is folder path exists? ", folder_path)
        date_dirs = os.listdir(folder_path)
        print(" Got date_dirs = ", date_dirs)

        keys = self.ibm_client.list_keys(bucket_name)
        print(keys)

        for date_dir in date_dirs:
            # self.ibm_client.create_folder(bucket_name, date_dir)
            path_date_dir = os.path.join(folder_path, date_dir)
            files = os.listdir(path_date_dir)
            for filename in files:
                file_path = os.path.join(path_date_dir, filename)
                to_file_path = date_dir + "/" + filename
                if to_file_path not in keys:
                    self.ibm_client.upload_file_cos(bucket_name , file_path, to_file_path)
                else:
                    print("File {} is already in cloud".format(to_file_path))