import requests
from bs4 import BeautifulSoup
import random

response = requests.get(
    url="https://en.wikipedia.org/wiki/Web_scraping")

# Initalise soup from the response and exctract the article title
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find(id="firstHeading")
print(title.string)

# Getting all the links from the article

allLinks = soup.find(id="bodyContent").find_all("a")
random.shuffle(allLinks)
linkToScraper = 0

for link in allLinks:
    if link['href'].find("/wiki/") == -1:
        continue
    linkToScrape = link
    break

print(linkToScrape)
