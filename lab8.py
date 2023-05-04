import requests
from bs4 import BeautifulSoup


def parse_ukd_data():
    url = 'https://ukd.edu.ua/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    menu = soup.find('ul', {'class': 'nav navbar-nav navbar-right'})
    for item in menu.find_all('li'):
        if item.a:
            print(item.a.text)
