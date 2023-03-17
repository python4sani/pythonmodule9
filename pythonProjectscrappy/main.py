import requests
from bs4 import BeautifulSoup as bs

sitemap = input("Enter Sitemap Url: ")
response = requests.get(sitemap)
html_soup = bs(response.text, 'html.parser')
base_urls = html_soup.findAll('loc')

for single_urls in base_urls:
    res = requests.get(single_urls.text)
    html = bs(res .text, 'html.parser')
    urls = html.findAll('loc')
    for url in urls:
        with open('sitemap.txt', 'a+') as file:
            file.writelines(url.text + '\n')
        file.close()