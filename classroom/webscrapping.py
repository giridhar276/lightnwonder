
#step1: read the webpage(html) ---> requests library
#step2: extract all the URLs from the web page -->beautisoup

from bs4 import BeautifulSoup
import requests
#step1
response = requests.get("https://www.google.com/",verify=False)

if response.status_code == 200:
    #print(response.text)
    #step2
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))
        print("-----------------")

