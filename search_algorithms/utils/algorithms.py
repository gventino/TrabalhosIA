from utils.HrefExtractor import HrefExtractor

# busca em largura:
def bfs(origin:str, max_it:int) -> dict:
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

def bfsSearch(graph, origin:str, destination:str) -> bool:
    queue = []
    visited = set()
    queue.append(origin)
    visited.add(origin)
    
    while queue:
        w = queue.pop(0)
        if w == destination:
            return True
        adj = graph[origin]
        for u in adj:
            if u not in visited:
                visited.add(u)
                queue.append(u)
    return False

