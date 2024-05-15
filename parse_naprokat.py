import requests
from bs4 import BeautifulSoup


def get_tools_list(tools_id=None):
    url = 'https://naprokat.kg/'
    response = requests.get(url=url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')



 