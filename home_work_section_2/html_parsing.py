import requests
from bs4 import BeautifulSoup

response = requests.get('https://en.wikipedia.org/wiki/List_of_the_most_common_passwords')
soup = BeautifulSoup(response.text, 'html.parser')

#print(response.text)
print(soup)