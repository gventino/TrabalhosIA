from utils.HrefExtractor import HrefExtractor
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('QtAgg')

test = HrefExtractor('https://ufu.br')
print('ORIGIN:\t' + test.url)
print('HREFs:')
for href in test.hrefs:
    print('\t' + href)

nx.draw(nx.DiGraph(test.toDict()), with_labels=True)
plt.show()