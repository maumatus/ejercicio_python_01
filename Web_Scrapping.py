import requests
from bs4 import BeautifulSoup as bs

github_user = input('input Github User: ')
url = 'https://github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
soup = bs(r.text, 'html.parser')
profile_image = soup.find('img',{'alt' : 'Avatar'})['src']
repositories = soup.find_all(class_="repo")
print(profile_image)
print(repositories)