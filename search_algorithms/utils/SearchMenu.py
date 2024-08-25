from pytermgui import InputField, WindowManager, Window, Container, Label
from utils.algorithms import bfsSearch
from utils.FinishMenu import FinishMenu

class SearchMenu:
    def __init__(self, graph):
        self.input_origin = InputField("https://", prompt="Origin: ")
        self.input_destination = InputField("https://", prompt="Destination: ")
        self.graph = graph

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
        FinishMenu(result)
