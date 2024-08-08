from bs4 import BeautifulSoup
import requests


class HrefExtractor:
    def __init__(self, url):
        self.url = url
        self.hrefs = self.extractHrefs(self.url)
        self.filteredHrefs = self.filterHrefs()

    def extractHrefs(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        hrefs = [a['href'] for a in soup.find_all('a', href=True)]
        return hrefs
    
    def filterHrefs(self):
        return [href for href in self.hrefs if href.startswith("https")]