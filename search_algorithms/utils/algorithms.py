from utils.HrefExtractor import HrefExtractor
import networkx as nx

# eh um bfs que investiga as paginas web e remonta o grafo num dict:
# o max_it eh o maximo de iteracoes que devemos fazer, indica o tamanho do grafo
# sem o max_it ia crescer pra sempre o grafo
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

# eh um bfs propriamente dito, faz a busca no grafo passado pra funcao, dado uma origem e um destino
# e retorna o grafo com caminho feito da origem ao destino
def bfs(graph, origin:str, destination:str) -> nx.DiGraph:
    queue = []
    # conjunto dos vertices visitados:
    visited = set()
    
    # bota a origem na fila
    queue.append(origin)
    # bota a origem nos visitados
    visited.add(origin)
    
    # inicializa o grafo que vai guardar o caminho feito da origem ao destino
    result_graph = nx.DiGraph()
    # adiciona a origem no grafo
    result_graph.add_node(origin)
    
    while queue:
        # extrai o primeiro da fila
        w = queue.pop(0)
        
        # retorna o grafo de resultado se o w for o destino:
        if w == destination:
            return result_graph
        
        # extrai a lista de adjacencia do vertice w:
        adj = graph[w]

        # para cada vertice u na adjacencia de w:
        for u in adj:
            # se u nao foi visitado:
            if u not in visited:
                # visita o u:
                visited.add(u)
                # bota o u na fila:
                queue.append(u)
                # adiciona a aresta w->u no grafo
                result_graph.add_edge(w, u)
                # se o u for o destino, retorna o grafo que guarda o caminho feito pelo bfs:
                if u == destination:
                    return result_graph  # Return immediately when destination is found
    return {} # dict vazio indica que o caminho nao foi encontrado

