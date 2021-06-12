from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import pandas as pd 
from datetime import date, timedelta, datetime
import requests 

## Date List created with string values for the last 4 days to only pull opinions from that range.
today = date.today()
yesterday = date.today() - timedelta(1)
two_ago = date.today() - timedelta(2)
today_word = today.strftime("%B %d, %Y")
yesterday_word = yesterday.strftime("%B %d, %Y")
two_ago_word = two_ago.strftime("%B %d, %Y")
yesterday_link = yesterday.strftime("%Y-%m-%d")
#print(today_word)
#print(yesterday_word)
#print(two_ago_word)
date_list = [today_word,yesterday_word,two_ago_word]

## Headers is used because a User-Agemt was required by the website
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'}
link = "https://www.congress.gov/search?q=%7b%22congress%22:%22all%22,%22source%22:%22legislation%22,%22search%22:%22chamberActionDateTotal:\%22"+yesterday_link+"|117|passed\%22+AND+billIsReserved:\%22N\%22%22%7d&pageSort=documentNumber:asc&searchResultViewType=expanded"
page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')

## Actual HTML pull
object_list = []
for item in soup.find_all(class_='expanded'):
    
    #if item.find('span').get_text() in date_list:
    title = item.find(class_='result-heading').get_text() + item.find(class_='result-title').get_text()
    ilink = "https://www.congress.gov" + item.find('a').get('href')
    #notes = item.find()
    idate = yesterday_word

    obj_data = {'source':'', 'title': title , 'link': ilink, 'Notes': '', 'date': idate}
    object_list.append(obj_data)

## Final dataframe is defined
congress_df = pd.DataFrame(object_list)
print(congress_df)