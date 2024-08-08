from utils.HrefExtractor import HrefExtractor
import networkx as nx
import matplotlib.pyplot as plt
test = HrefExtractor('https://ufu.br')
print('ORIGIN:\t' + test.url)
print('HREFs:')
for href in test.hrefs:
    print('\t' + href)

G = nx.Graph()
G.add_node(test)
nx.draw(G)
plt.show()