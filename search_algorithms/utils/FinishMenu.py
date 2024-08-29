from pytermgui import WindowManager, Window, Container, Label

class FinishMenu:
    def __init__(self, found):
        if found:
            self.label = Label("[italic 255 bold green] FOUND") 
        else:
            self.label = Label("[italic 255 bold red] NOT FOUND")

        with WindowManager() as self.manager:
            self.window = (
                Window(
                    Container(
                    self.label,
                    box="DOUBLE"
                    ),
                    width=60,
                    box="DOUBLE",
                )
                .center()
            )
            self.manager.add(self.window)