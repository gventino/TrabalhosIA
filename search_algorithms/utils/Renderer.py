from utils.HrefExtractor import HrefExtractor
from utils.algorithms import bfs
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import json
from math import sqrt
matplotlib.use('QtAgg')

def newGraph(param:dict):
    url = param["url"]
    max_it = param["max_it"]
    graph = bfs(url, int(max_it))
    G = nx.DiGraph(graph)
    k = 100/sqrt(G.order()) if G.order != 0 else 10
    labels = param["labels"]

    if param["spring_layout"]:
        pos = nx.spring_layout(G, k=k)
        nx.draw(G, pos=pos, with_labels=labels)
        plt.show()

    if param["bfs_layout"]:
        pos = nx.bfs_layout(G, start=url)
        nx.draw(G, pos=pos, with_labels=labels)
        plt.show()

    if param["kk_layout"]:
        pos = nx.kamada_kawai_layout(G)
        nx.draw(G, pos=pos, with_labels=labels)
        plt.show()

    if param["json"]:
        load_json = {"param":param,"graph":graph}
        jasón = json.dumps(load_json)
        directory = './jsons/'
        filename = url.replace('https://', '') + max_it + '.json'
        f = open( directory + filename, 'w')
        f.write(str(jasón))
        f.close()
    return graph

def loadGraph(filename:str):
    directory = './jsons/'
    try:
        f = open(directory + filename, 'r')
        data = json.load(f)
        f.close()
    except:
        print('Wrong file name, try again!')
        return

    param = data["param"]
    graph = data["graph"]

    url = param["url"]
    labels = param["labels"]
    G = nx.DiGraph(graph)
    k = 100/sqrt(G.order())

    if param["spring_layout"]:
        pos = nx.spring_layout(G, k=k)
        nx.draw(G, with_labels=labels)
        plt.show()

    if param["bfs_layout"]:
        pos = nx.bfs_layout(G, start=url)
        nx.draw(G, with_labels=labels)
        plt.show()

    if param["kk_layout"]:
        pos = nx.kamada_kawai_layout(G)
        nx.draw(G, pos=pos, with_labels=labels)
        plt.show()

    return graph
