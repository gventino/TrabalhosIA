from pytermgui import InputField, Checkbox, WindowManager, Window, Container, Label
from utils.Renderer import newGraph
from utils.FinishMenu import FinishMenu

class NewGraphMenu:
    def __init__(self):
        #input fields:
        self.input_url = InputField("https://", prompt="Origin URL: ")
        self.input_max_it = InputField("", prompt="Max It: ")

        #layout checkboxes:
        self.checkbox_spring = Checkbox(callback=None, checked=False)
        self.checkbox_bfs = Checkbox(callback=None, checked=False)
        self.checkbox_kk = Checkbox(callback=None, checked=False)

        #extra checkboxes:
        self.checkbox_json = Checkbox(callback=None, checked=False)
        self.checkbox_labels = Checkbox(callback=None, checked=False)

        with WindowManager() as self.manager:
            self.window = (
                Window(
                    Container(
                        Label("[italic 141 bold]Basics:"),
                        "",
                        self.input_url,
                        self.input_max_it,
                        width=30,
                        box="DOUBLE"
                    ),
                    
                    "",
                    Container(
                        Label("[italic 141 bold]Layouts:"),
                        
                        Container(
                            "Spring Layout:",
                            self.checkbox_spring,
                            box="EMPTY_VERTICAL"
                        ),

                        Container(
                            "BFS Layout:",
                            self.checkbox_bfs,
                            box="EMPTY_VERTICAL"
                        ),
                        
                        Container(
                            "Kamada Kawai Layout:",
                            self.checkbox_kk,
                            box="EMPTY_VERTICAL"
                        ),
                        
                        box="DOUBLE",
                    ),

                    "",
                    Container(
                        Label("[italic 141 bold]Extras:"),
                        
                        Container(
                            "Want to read labels?",
                            self.checkbox_labels,
                            box="EMPTY_VERTICAL"
                        ),

                        Container(
                            "Want to save?",
                            self.checkbox_json,
                            box="EMPTY_VERTICAL"
                        ),

                        box="DOUBLE",
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
        self.manager.stop()
        param = {
                "url": self.input_url.value,
                "max_it": self.input_max_it.value,
                
                "spring_layout": self.checkbox_spring.checked,
                "bfs_layout": self.checkbox_bfs.checked,
                "kk_layout": self.checkbox_kk.checked,

                "json": self.checkbox_json.checked,
                "labels": self.checkbox_labels.checked,
              }
        newGraph(param)
        FinishMenu()