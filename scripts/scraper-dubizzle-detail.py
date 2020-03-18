import requests

from bs4 import BeautifulSoup


page = requests.get('https://dubai.dubizzle.com/property-for-sale/residential/apartment/2019/6/14/park-view-around-heart-touching-studio-apa-2/')

soup = BeautifulSoup(page.text, 'html.parser')

scripts = soup.find_all('script')

print(scripts)