import requests 
from bs4 import  BeautifulSoup as bs4
url= 'https://jobs.github.com/positions'
def scrap_jobs(url):
    r= requests.get(url)
    soup= bs4(r.content,features="html5lib")
    jobs = [ i for i in soup.find_all('tr',{'class':'job'})]
    links= []
    for i in jobs:
        title = i.find('td',{'class':'title'})
        name = title.find('h4')
        tine = name.find('a')['href']
        sourc = title.find('p',{'class':'source'})
        Source = sourc.find('a')
        newLink = {
            'name':name.text,
            'link':tine,
            'source':Source.text
        }
        links.append(newLink)
    return links
scrap_jobs(url)