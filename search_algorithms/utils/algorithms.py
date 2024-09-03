from utils.HrefExtractor import HrefExtractor
import networkx as nx

# busca em largura:
def generateGraph(origin:str, max_it:int) -> dict:
    graph = {}
    queue = []
    visited = set()
    queue.append(origin)
    visited.add(origin)
    it = 0
    while queue and it!=max_it:
        w = queue.pop(0)
        node = HrefExtractor(w)
        adj = node.hrefs
        for u in adj:
            if u not in visited:
                visited.add(u)
                queue.append(u)
        it += 1
        graph.update(node.toDict())
    return graph

def bfs(graph, origin:str, destination:str) -> nx.DiGraph:
    queue = []
    visited = set()
    queue.append(origin)
    visited.add(origin)
    
    result_graph = nx.DiGraph()
    result_graph.add_node(origin)
    
    while queue:
        w = queue.pop(0)
        if w == destination:
            return result_graph  # Return the graph if w is the destination (Can't think of case where it happens)
        adj = graph[w]
        for u in adj:
            if u not in visited:
                visited.add(u)
                queue.append(u)
                result_graph.add_edge(w, u)
                if u == destination:
                    return result_graph  # Return immediately when destination is found
    return {} # empty dict = destination not found

