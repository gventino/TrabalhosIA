from utils.Renderer import loadGraph
from utils.FinishMenu import FinishMenu
from pytermgui import InputField, WindowManager, Window, Container, Label

class LoadGraphMenu:
    def __init__(self):
        self.input_namefile = InputField(".json", prompt="Namefile: ")

        with WindowManager() as self.manager:
            self.window = (
                Window(
                    Label("[italic 141 bold]Fill the field:"),
                    Container(
                        Container(
                            self.input_namefile,
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
        loadGraph(self.input_namefile.value)
        FinishMenu()
