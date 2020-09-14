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
            os.mkdir(folder_path)
        file_path = os.path.join(folder_path, self.filename)
        print("file_path", file_path)
        f_writer = open(file_path, 'a')
        try:
            f_writer.write(json_str + "\n")
        finally:
            f_writer.close()

    def move_to_cloud(self):
        pass