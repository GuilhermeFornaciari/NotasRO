import webbrowser
import hashlib
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout


from kivy.properties import StringProperty,ListProperty,ObjectProperty
from kivy.uix.widget import Widget
from kivy.config import Config

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.core.window import Window

from kivymd.uix.behaviors import (
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
# minimum

Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'minimum_height', '605')
Config.write()


class Link_EsqueciSenha(Button):
    corbotao = ListProperty([0.35, 0.35, 0.35, 1])
    TamanhoFonte = StringProperty("16")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouseover)
        self.mouse_entrou = False

    def on_mouseover(self, window, pos):
        if self.collide_point(*pos):
            self.corbotao = [0, 0, 1, 1]
            self.mouse_entrou = True
            Window.set_system_cursor("hand")

        elif self.mouse_entrou:
            self.corbotao = [0.35, 0.35, 0.35, 1]
            self.mouse_entrou = False
            Window.set_system_cursor("arrow")

    def on_press(self):
        self.TamanhoFonte = "14"

    def on_release(self):
        self.TamanhoFonte = "16"
        webbrowser.open("http://example.com/")  # Go to example.com


class Link_CriarNovaConta(Button):
    corbotao = ListProperty([0.35, 0.35, 0.35, 1])
    TamanhoFonte = StringProperty("16")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouseover)
        self.mouse_entrou = False

    def on_mouseover(self, window, pos):
        if self.collide_point(*pos):
            self.corbotao = [0, 0, 1, 1]
            self.mouse_entrou = True
            Window.set_system_cursor("hand")

        elif self.mouse_entrou:
            self.corbotao = [0.35, 0.35, 0.35, 1]
            self.mouse_entrou = False
            Window.set_system_cursor("arrow")

    def on_press(self):
        self.TamanhoFonte = "14"

    def on_release(self):
        self.TamanhoFonte = "16"
        webbrowser.open("http://example1.com/")  # Go to example.com


class BarraAzul(GridLayout):
    pass


class Nada(Widget):
    pass


class PainelSuperior(BoxLayout):
    pass


class Botaoprox(Button):
    corbotao = ListProperty([0,.65,0.89,0.6])
    corfonte = ListProperty([.2,.2,.2,1])


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouseover)
        self.mouse_entrou = False
        self.PainelLogin = App.get_running_app().PainelLogin

    def on_mouseover(self, window, pos):
        if self.collide_point(*pos):
            Window.set_system_cursor("hand")
            self.mouse_entrou = True

        elif self.mouse_entrou:
            Window.set_system_cursor("arrow")
            self.mouse_entrou = False


    def on_press(self):
        self.corbotao = [.2, .2, 1, 1]
        self.corfonte = [1,1,1,1]


    def on_release(self):
        self.corbotao = [0, .65, 0.89, 0.6]
        self.corfonte = [.2, .2, .2, 1]
        self.PainelLogin.enviadados()







class TxtInputEmail(TextInput):
    def on_text(self,instance ,value):
        self.Email = value
        print(self.Email)


    txtbox = TextInput()
    txtbox.bind(text=on_text)

class TxtInputSenha(TextInput):
    def on_text(instance, value):
        print('The widget', instance, 'have:', value)

    senha = TextInput()
    senha.bind(text=on_text)


class PainelLogin(
    GridLayout,
    CommonElevationBehavior,
    BackgroundColorBehavior,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    pass
    def enviadados(self):
        self.app = App.get_running_app()
        self.email = self.app.email
        self.senha = self.app.senha
        print(self.email,self.senha)
        print("Envia dados ativado")


class Login(Screen):
    pass


class telaManager(ScreenManager):
    pass


class NotasRO(App):
    PainelLogin = PainelLogin()
    email = TxtInputEmail()
    senha = TxtInputSenha()
    def build(self):
        return telaManager()


if __name__ == '__main__':
    NotasRO().run()
