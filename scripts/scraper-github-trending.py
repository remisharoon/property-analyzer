import requests
from bs4 import BeautifulSoup
# Collect the github page

page = requests.get('https://github.com/trending')

soup = BeautifulSoup(page.text, 'html.parser')

# get the repo list
repoall = soup.find(class_="explore-pjax-container container-lg p-responsive pt-6")

box = repoall.findAll('div', attrs={"class": "Box"})

print(len(box))

articles = box[0].findAll('article')

print(len(articles))

for repo in articles:
    full_repo_name = repo.find('h1').find('a').find('span').text.split('/')
    print(full_repo_name)
    # extract the developer name at index 0
    #developer = full_repo_name[0].strip()
    # extract the repo name at index 1
    #repo_name = full_repo_name[1].strip()