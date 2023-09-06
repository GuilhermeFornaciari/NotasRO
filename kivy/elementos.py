import webbrowser
import hashlib
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox

from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout

from kivy.properties import ObjectProperty, StringProperty, ListProperty, BooleanProperty,DictProperty,NumericProperty
from kivy.uix.widget import Widget
from kivy.config import Config

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.graphics import Rectangle,Color,RoundedRectangle

class BarraAzul(GridLayout):
    pass

class Nada(Widget):
    pass


class Nada1(Widget):
    pass


class PainelSuperior(BoxLayout):
    pass





class Link_EsqueciSenha(Button):
    corbotao = ListProperty([0.35, 0.35, 0.35, 1])
    TamanhoFonte = StringProperty("16")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouseover)
        self.mouse_entrou = False

    def on_mouseover(self, window, pos):
        if self.collide_point(*pos) and App.get_running_app().tela == 1:
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
        if self.collide_point(*pos) and App.get_running_app().tela == 1:
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


class BotaoLogin(Button):
    corbotao = ListProperty([0, .65, 0.89, 0.6])
    corfonte = ListProperty([.2, .2, .2, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouseover)
        self.mouse_entrou = False
        self.PainelLogin = App.get_running_app().PainelLogin

    def on_mouseover(self, window, pos):
        if self.collide_point(*pos) and App.get_running_app().tela == 1:
            Window.set_system_cursor("hand")
            self.mouse_entrou = True

        elif self.mouse_entrou:
            Window.set_system_cursor("arrow")
            self.mouse_entrou = False


class BotaoMateria(Button):
    corbotao = ListProperty([0, .65, 0.89, 0.6])
    corfonte = ListProperty([.2, .2, .2, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouseover)
        self.mouse_entrou = False
        self.PainelLogin = App.get_running_app().PainelLogin

    def on_mouseover(self, window, pos):
        if self.collide_point(*pos) and App.get_running_app().tela == 2:
            Window.set_system_cursor("hand")
            self.mouse_entrou = True

        elif self.mouse_entrou:
            Window.set_system_cursor("arrow")
            self.mouse_entrou = False

    def on_press(self):
        self.corbotao = [.2, .2, 1, 1]
        self.corfonte = [1, 1, 1, 1]

    def on_release(self):
        self.corbotao = [0, .65, 0.89, 0.6]
        self.corfonte = [.2, .2, .2, 1]


class BotaoTurmas(Button):
    corbotao = ListProperty([0, .65, 0.89, 0.6])
    corfonte = ListProperty([.2, .2, .2, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouseover)
        self.mouse_entrou = False
        self.PainelLogin = App.get_running_app().PainelLogin

    def on_mouseover(self, window, pos):
        if self.collide_point(*pos) and App.get_running_app().tela > 3:
            Window.set_system_cursor("hand")
            self.mouse_entrou = True

        elif self.mouse_entrou:
            Window.set_system_cursor("arrow")
            self.mouse_entrou = False

    def on_press(self):
        self.corbotao = [.2, .2, 1, 1]
        self.corfonte = [1, 1, 1, 1]

    def on_release(self):
        self.corbotao = [0, .65, 0.89, 0.6]
        self.corfonte = [.2, .2, .2, 1]


class BotaoConfirma(Button):
    corbotao = ListProperty([0, .65, 0.89, 0.6])
    corfonte = ListProperty([.2, .2, .2, 1])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouseover)
        self.mouse_entrou = False
        self.PainelLogin = App.get_running_app().PainelLogin
        self.text = "Confirmar"
        self.color = self.corfonte
        self.background_color = 0,0,1,0
        self.background_normal =  ""
        self.size_hint = (1,0.08)

    def on_mouseover(self, window, pos):
        if self.collide_point(*pos) and App.get_running_app().tela > 3:
            Window.set_system_cursor("hand")
            self.mouse_entrou = True

        elif self.mouse_entrou:
            Window.set_system_cursor("arrow")
            self.mouse_entrou = False

    def on_press(self):
        self.corbotao = [.2, .2, 1, 1]
        self.corfonte = [1, 1, 1, 1]

    def on_release(self):
        self.corbotao = [0, .65, 0.89, 0.6]
        self.corfonte = [.2, .2, .2, 1]
        print(App.get_running_app().tela)
        App.get_running_app().TelaManager.current = "Final"


class Telaerro(Popup):
    mensagem = StringProperty("")

    def __init__(self, mensagem, **kwargs):
        super().__init__(**kwargs)
        self.mensagem = mensagem

    pass


def mostrar_erro(mensagem):
    telaerro = Telaerro(mensagem)
    telaerro.open()


class TxtInputEmail(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Email = "2"

    def on_text(self, instance, value):
        App.get_running_app().email = value

    txtbox = TextInput()
    txtbox.bind(text=on_text)


class TxtInputSenha(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_text(self, instance, value):
        App.get_running_app().senha = value

    txtbox = TextInput()
    txtbox.bind(text=on_text)


class TabelaMateria(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = 20
        self.spacing = 5
        self.cols = 2
        self.rows = 6
        self.orientation = 'lr-tb'
        self.size_hint = (1, 0.7)
        lista = {101: "Inglês", 102: "Português", 103: "Espanhol", 104: "Matemática", 105: "Ciências", 106: "Artes",
                 107: "História", 108: "Geografia", 109: "Biologia", 110: "Física", 111: "Química", 112: "Sociologia"}
        for id in lista.keys():
            self.add_widget(OpcaoMateria(id, lista[id]))


class TabelaTurmas(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        turmas = "ABCDEFGHIJ"
        anos = ["6º ano ", "7º ano ", "8º ano ", "9º ano "]
        for ano in anos:
            self.add_widget(
                Label(color=(0, 0, 0, 1), text=ano, size_hint=(0.24, 0.01), valign="bottom", halign="center",
                      text_size=(100, 50)))
            self.add_widget(Nada(size_hint=(0.01, 0.01)))
        for ano in anos:
            gd = GridLayout(cols=2, padding=20, size_hint=(0.25, 0.75))
            self.add_widget(gd)
            for letra in turmas:
                gd.add_widget(OpcaoTurmas(ano, letra))

    def checkbox_clicada(self, instance, value):
        pass


class TabelaTurmas2(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        turmas = "ABCDEFGHIJ"
        anos = ["1º ano ", "2º ano ", "3º ano "]
        self.add_widget(Nada(size_hint=(0.15, 0.01)))
        for ano in anos:
            self.add_widget(
                Label(color=(0, 0, 0, 1), text=ano, size_hint=(0.24, 0.01), valign="bottom", halign="center",
                      text_size=(100, 50)))
            self.add_widget(Nada(size_hint=(0.01, 0.01)))
        self.add_widget(Nada(size_hint=(0.15, 0.01)))
        for ano in anos:
            gd = GridLayout(cols=2, padding=20, size_hint=(0.25, 0.75))
            self.add_widget(gd)
            for letra in turmas:
                gd.add_widget(OpcaoTurmas(ano, letra))



class OpcaoMateria(GridLayout):
    nomemateria = StringProperty("")

    def __init__(self, id, nomemateria, **kwargs):
        super().__init__(**kwargs)
        self.nomemateria = nomemateria
        self.id = id

    def checkbox_clicada(self, instance, value):

        if value is False:
            App.get_running_app().materia = False
        else:
            App.get_running_app().materia = {self.id:self.nomemateria}


class OpcaoTurmas(GridLayout):
    Turma = StringProperty("")

    def __init__(self, ano, Turma, **kwargs):
        super().__init__(**kwargs)
        self.Turma = Turma
        self.ano = ano
        self.appturma = App.get_running_app().Turmas

    def checkbox_clicada(self, instance, value):
        if value:
            self.appturma.append(self.ano + self.Turma + " ")
        else:
            self.appturma.pop(self.appturma.index(self.ano + self.Turma + " "))
        print(self.appturma)
