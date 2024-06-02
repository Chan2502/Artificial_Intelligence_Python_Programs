from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

url="https://www.flipkart.com/search?q=samsung+mobiles&amp;sid=tyy%2C4io&amp;as=on&amp;as-show=on&amp;otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&amp;otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&amp;as-pos=1&amp;as-type=RECENT&amp;suggestionId=samsung+mobiles%7CMobiles&amp;requestId=18944876-a6ef-44c0-ac67-d31d7b11a548&amp;as-backfill=on"
r=requests.get(url)
htmlContent=r.content
print(htmlContent)
#parse the html
soup=BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)
# travere the tree traversal
title=soup.title
#Commonly used type objects
print(title)
# Get all the paragraph from the pages
paras=soup.find_all('p') 
print(paras)
# Get all the anchors tags from the pages
anchor=soup.find_all('a')
print(anchor)