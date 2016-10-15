from bs4 import BeautifulSoup
import urllib.request
def reading(url):
    raw_data = urllib.request.urlopen("https://www.youtube.com/feed/subscriptions")
    data=raw_data.read().decode('utf-8')
    data=BeautifulSoup(data, 'html.parser')
    print(data.text)
reading()