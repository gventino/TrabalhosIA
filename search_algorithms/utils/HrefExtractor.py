from bs4 import BeautifulSoup
import requests
import re

# classe principal, dado o url de uma pagina web constroi um objeto (vertice do grafo)
# ele baixa o html do url passado, procura pelas tags a com campos href comecando com 
# https:// e bota na lista de adjacencia do vertice (hrefs)
class HrefExtractor:
    def __init__(self, url:str):
        self.url = url
        self.hrefs = self.__getHREFs()

    def __getHTML(self):
        response = requests.get(self.url)
        html = BeautifulSoup(response.text, 'html.parser')
        return html

    def __getHREFs(self) -> list:
        try:
            html = self.__getHTML()
            hrefs = set()
            # sim regex!
            for tag in html.find_all('a', attrs={'href': re.compile("^https://")}):
                href = tag.get('href')
                hrefs.add(href)
            return list(hrefs)
        except:
            return []
    
    def toDict(self) -> dict:
        return {self.url:self.hrefs}