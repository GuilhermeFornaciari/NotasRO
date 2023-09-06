import webbrowser
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.uix.widget import Widget
from kivy.config import Config

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.core.window import Window

from kivymd.uix.behaviors import (
    RectangularRippleBehavior,
    BackgroundColorBehavior,
    CommonElevationBehavior,
)

"""
def mapear(x):
    in_min = 0
    in_max = 255

    out_min = 0
    out_max = 1
    return float((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while 1:
    x = float(input())
    print(mapear(x,))
"""
class Botaoprox(Button):
    pass

class Login(Screen):
    pass

class telaManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        return telaManager()



if __name__ == '__main__':
    MyApp().run()