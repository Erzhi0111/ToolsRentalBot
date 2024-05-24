import requests
from bs4 import BeautifulSoup



url = 'https://naprokat.kg'
response = requests.get(url=url, verify=False)
soup = BeautifulSoup(response.text, 'html.parser')

div_stroika = soup.find_all('div', {'id': ''}) 
