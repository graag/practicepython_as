


from bs4 import BeautifulSoup
import requests

# response = urllib.request.urlopen('https://www.nytimes.com/')
r=requests.get("https://www.nytimes.com/")
r_html=r.text
soup = BeautifulSoup(r_html, 'lxml')
for heading in soup.find_all('h3'):
    print(heading.get_text())


