from utils.NewGraphMenu import NewGraphMenu
from utils.LoadGraphMenu import LoadGraphMenu
from pytermgui import Checkbox, WindowManager, Window, Container, Label

class StartingMenu:
    def __init__(self):
        #checkboxes:
        self.checkbox_new = Checkbox(callback=self.__newGraph, checked=False)
        self.checkbox_load = Checkbox(callback=self.__loadGraph, checked=False)

        with WindowManager() as self.manager:
            self.window = (
                Window(
                    Label("[italic 141 bold]Choose:"),
                    Container(
                        Container(
                            "New graph:",
                            self.checkbox_new,
                            box="EMPTY_VERTICAL"
                        ),

                        Container(
                            "Load Graph:",
                            self.checkbox_load,
                            box="EMPTY_VERTICAL"
                        ),
                    ),
                    width=60,
                    box="DOUBLE",
                )
                .set_title("[210 bold]BFS REFERENCES FINDER")
                .center()
            )
            self.manager.add(self.window)

    #callback functions:
    def __newGraph(self, *args, **kwargs):
        NewGraphMenu()
        
    def __loadGraph(self, *args, **kwargs):
        LoadGraphMenu()