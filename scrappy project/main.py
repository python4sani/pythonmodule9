import requests
from bs4 import BeautifulSoup as bs
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

i=1
while i<845:
    url = "https://www.dreshare.com/page/"+str(i)+"/"
    res= requests.get(url, headers=headers)
    html = bs(res.text, 'html.parser')
    h2s = html.findAll('h2')

    for h2 in h2s:
        link = h2.find('a')['href']
        with open('dreshare.txt', "a+") as file:
            file.writelines(link+"\n")
        file.close()
    i=i+1
