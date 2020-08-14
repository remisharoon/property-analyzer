import requests
import time
from bs4 import BeautifulSoup
import json


class BaseParser:
    url = ""

    def __init__(self, url):
        self.url = url

    def parse(self):
        pass
