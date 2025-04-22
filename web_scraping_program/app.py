import requests
from bs4 import BeautifulSoup as bs


github_username = input('Input Github Username: ')
URL = f'https://github.com/{github_username}'

r = requests.get(URL)
soup = bs(r.content, 'html.parser')
profile_img = soup.find('img', class_='avatar')['src']
print(profile_img)