from Illusion.helper import c_helper


class CustomBTNTest(c_helper.button_base()):
    def on_click(self, data:dict):
        super().on_click(data)
        print("custom test btn pressed successfully")