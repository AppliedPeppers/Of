from bs4 import BeautifulSoup
import urllib.request


def reading(url):
    text = ''
    raw_data = urllib.request.urlopen(url)
    data = raw_data.read().decode('utf-8')
    data = BeautifulSoup(data, 'html.parser')
    data = data.find_all(['b', 'p', 'a', 'body', 'br', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'i'])
    for name in data:
        text = text + name.get_text()
    return text
