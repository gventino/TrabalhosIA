from utils.HrefExtractor import HrefExtractor
from utils.algorithms import bfs
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import json
from math import sqrt
matplotlib.use('QtAgg')

graph = bfs('https://ufu.br', 20) 
G = nx.DiGraph(graph)
d = dict(G.degree)
k = 100/sqrt(G.order())
#pos = nx.kamada_kawai_layout(G)
#pos = nx.bfs_layout(G, start='https://ufu.br')
pos = nx.spring_layout(G, k=k)
nx.draw(G, pos=pos, with_labels=True)
#nx.draw(G, pos=pos, with_labels=True, node_size=[d[k]*300 for k in d])

#nx.draw(nx.DiGraph(graph), with_labels=True)
jasón = json.dumps(graph)
f = open('graph.json', 'w')
f.write(str(jasón))
f.close()
plt.show()
