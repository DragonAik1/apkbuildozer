import kivy
kivy.require('1.0.5')

from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window
from upload_file_script import send_file_to_server
import yadisk
from config import token

y = yadisk.YaDisk(token=token)
Window.size = (1080, 2376)
class asd(GridLayout):
    def ch_text(self):
        #
        if y.check_token():
            if not y.is_dir("/wwww"):
                y.mkdir("/wwww")
                self.lw.text = "ok!"


class ControllerApp(App):

    def build(self):
        return asd()


if __name__ == '__main__':
    ControllerApp().run()