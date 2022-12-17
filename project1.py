import bs4
import requests
URL = "https://asia2tv.cn/status/live/"
page=requests.get(URL)
obj=bs4.BeautifulSoup(page.content,'html.parser')
films=obj.find_all("div",{"class":"row-movies mt-4"})
"""print(films)"""
for k in range(len(films)):
    l=films[k].text
    print(l)
