from bs4 import BeautifulSoup
import requests
import re

class HrefExtractor:
    def __init__(self, url):
        self.url = url
        self.hrefs = self.__getHREFs()

    def __getHTML(self):
        response = requests.get(self.url)
        html = BeautifulSoup(response.text, 'html.parser')
        return html

    def __getHREFs(self):
        html = self.__getHTML()
        hrefs = set()
        # sim regex!
        for tag in html.find_all('a', attrs={'href': re.compile("^https://")}):
            href = tag.get('href')
            hrefs.add(href)
        return hrefs