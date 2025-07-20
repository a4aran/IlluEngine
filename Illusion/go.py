from Illusion.ui import UI


class GlobalObjects:
    def __init__(self):
        self.__uis = {}

    def add_ui(self,ui: UI):
        self.__uis[ui.id] = ui

    def get_ui(self,ui_name) -> UI:
        return  self.__uis[ui_name]

    def delete_ui(self,ui_name):
        self.__uis.pop(ui_name)