from utils.HrefExtractor import HrefExtractor

# busca em largura:
def bfs(origin:str, max_it:int) -> list:
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