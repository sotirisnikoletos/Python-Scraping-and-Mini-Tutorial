import requests
from bs4 import BeautifulSoup

URL = "YOUR HTML TARGET PAGE"

to_scrape = requests.get(f"{URL}")
soup = BeautifulSoup(to_scrape.text,'html-parser')


#in every html we want to parse
#  and scrape we need to open the source so that we know what to look for
#  e.g for div elements,for tr/td elements,h1,p,img,a etc.
for tr in soup.find_all('tr'):
    for td in tr.find_all('td'):
        print(td)
        #if i want text only without elements <> </
        #print (td.text)



data=[]

#class special exists , we found out in source
for tr in soup.find_all('tr',{'class': 'special'}):
    values = [td.text for td in tr.find_all('td')]
    data.append(values)


print(data)


data=[]

div=soup.find('div',{'class':'special_table'})

for tr in div.find_all('tr'):
    values=[ td.text for td in tr.find_all('td')]:
    data.append(values)

print(data)


#good commands , next() , .text , .strip , indexing in find_all('')[0 or 1 or 2..]