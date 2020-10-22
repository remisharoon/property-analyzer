from datetime import datetime
import os
from src.connections.ibm_client import IBMClient
from src.common.config import cfg

class FileClient(object):

    def __init__(self):
        # self.filename = self._get_file_name()
        self.ibm_client = IBMClient(cfg)

if __name__ == "__main__":
    fc = FileClient()
