import requests
from bs4 import BeautifulSoup as scrap

github_user = input('Input Github Username: ')
url = 'https://github.com/'+github_user
r = requests.get(url)
bs = scrap(r.content, 'html.parser')
profile_pic = bs.find('img', {'alt' : 'Avatar'})['src'] 
print(profile_pic)
