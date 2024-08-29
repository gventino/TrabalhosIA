from pytermgui import InputField, WindowManager, Window, Container, Label
from utils.algorithms import bfsSearch
from utils.FinishMenu import FinishMenu
import networkx as nx
import matplotlib.pyplot as plt

class SearchMenu:
    def __init__(self, graph):
        self.input_origin = InputField("https://", prompt="Origin: ")
        self.input_destination = InputField("https://", prompt="Destination: ")
        self.graph = nx.DiGraph(graph)

        with WindowManager() as self.manager:
            self.window = (
                Window(
                    Label("[italic 141 bold]Fill the field:"),
                    Container(
                        Container(
                            self.input_origin,
                            box="DOUBLE"
                        ),
                        Container(
                            self.input_destination,
                            box="DOUBLE"
                        )
                    ),
                    ["Submit", lambda *_: self.__submit()],
                    width=60,
                    box="DOUBLE",
                )
                .set_title("[210 bold]BFS REFERENCES FINDER")
                .center()
            )
            self.manager.add(self.window)
    


    def __submit(self):
        result = bfsSearch(self.graph, self.input_origin.value, self.input_destination.value)
        if result:
            self.__plot_path(result)
        FinishMenu(result.size() > 0)


    def __plot_path(self, result):
        start_node = self.input_origin.value
        end_node = self.input_destination.value
        _, (ax1, ax2) = plt.subplots(1, 2)
        
    
        pos_original = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos_original, ax=ax1, with_labels=True, node_color='lightblue')
        nx.draw_networkx_nodes(result, pos_original, nodelist=[start_node, end_node], node_color='red', node_size=1000, ax=ax1)
        ax1.set_title(f"Original Graph\nNodes: {self.graph.number_of_nodes()}, Edges: {self.graph.number_of_edges()}")

        pos_bfs = nx.bfs_layout(result, start_node)
        nx.draw(result, pos_bfs, ax=ax2, with_labels=True, node_color='lightgreen')
        nx.draw_networkx_nodes(result, pos_bfs, nodelist=[start_node, end_node], node_color='red', node_size=1000, ax=ax2)
        ax2.set_title(f"BFS Tree\nNodes: {result.number_of_nodes()}, Edges: {result.number_of_edges()}")
        
        plt.tight_layout()
        plt.show()
