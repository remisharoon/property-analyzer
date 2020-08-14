from src.parsers.base_parser import BaseParser
import requests
import time
from bs4 import BeautifulSoup
import json

class PropFndrDetailParser(BaseParser):
    id = None

    def __init__(self, url, id):
        BaseParser.__init__(self, url)
        self.id = id

    def parse(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, 'html.parser')
        scripts = soup.find_all('script')
        parsed_dict = {}
        for s in scripts:
            if 'window.propertyfinder.settings.search' in s.text:
                lines = s.text.split("\n")
                for line in lines:
                    if "payload" in line:
                        jsontstr = line.replace("payload: ", "").rstrip(",")
                        jsondata = json.loads(jsontstr)
                        header = jsondata['data']
                        prop_id = int(header["id"])
                        if prop_id == self.id:
                            attributes = header['attributes']
                            related_info = jsondata['included']
                            parsed_dict["attributes"] = attributes
                            parsed_dict["related_info"] = related_info
                            parsed_dict["date_insert"] = attributes["date_insert"]
                            return parsed_dict
        return None

if __name__ == "__main__":
    url = "https://www.propertyfinder.ae/en/buy/villa-for-sale-abu-dhabi-al-reef-al-reef-villas-mediterranean-style-7623989.html"
    id = 7623989
    pfdetail = PropFndrDetailParser(url, id)
    parsed_dict = pfdetail.parse()
    print(parsed_dict)