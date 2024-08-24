from pytermgui import WindowManager, Window, Container, Label

class FinishMenu:
    def __init__(self):
        with WindowManager() as self.manager:
            self.window = (
                Window(
                    Container(
                    Label("[italic 255 bold green]FINISHED"),
                    box="DOUBLE"
                    ),
                    width=60,
                    box="DOUBLE",
                )
                .center()
            )
            self.manager.add(self.window)