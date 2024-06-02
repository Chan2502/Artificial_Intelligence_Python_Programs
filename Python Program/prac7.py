from bs4 import BeautifulSoup
import requests
import pandas as pd
URL="https://www.amazon.in/s?k=headphone&crid=9W3NP1H03U0K&sprefix=headphone%2Caps%2C189&ref=nb_sb_noss_2"
HEADER =({'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36','Accept-Language':'en-US'})
webpage=requests.get(URL,headers=HEADER)
print(webpage)
