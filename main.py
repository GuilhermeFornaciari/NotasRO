from elementos import *
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


class PainelLogin(GridLayout, CommonElevationBehavior, BackgroundColorBehavior):
    def enviadados(self):
        self.app = App.get_running_app()
        self.email = self.app.email
        self.senha = self.app.senha
        print(self.email, self.senha)
        print("Envia dados ativado")
        Passa = True
        if Passa:
            App.get_running_app().tela = 2
            return True
        else:
            mostrar_erro("Email ou senha informados estão incorretos")
            return False


class PainelSM(StackLayout, CommonElevationBehavior, BackgroundColorBehavior):
    def prox(self):
        if not App.get_running_app().materia:
            mostrar_erro("Por favor, selecione uma matéria")
            return False
        else:
            App.get_running_app().tela = 3
            return True


class PainelTurmas(StackLayout, CommonElevationBehavior, BackgroundColorBehavior):
    pass


class PainelTurmas2(StackLayout, CommonElevationBehavior, BackgroundColorBehavior):
    def prox(self):
        if len(App.get_running_app().Turmas) > 0:
            App.get_running_app().tela = 5
            return True
        else:
            mostrar_erro("Por favor, selecione ao menos uma turma")


class PainelBimestre(BoxLayout, CommonElevationBehavior, BackgroundColorBehavior):
    def checkbox_clicada(self, instance, value, Bm):
        if value:
            App.get_running_app().Bm = str(Bm)
        else:
            App.get_running_app().Bm = None

    def prox(self):
        if App.get_running_app().Bm is not None:
            App.get_running_app().Tela = 6
            pnsf.getturmas()

            return True
        else:
            mostrar_erro("Por favor, selecione um bimestre")
            return False


class PainelConfirma(BoxLayout, CommonElevationBehavior, BackgroundColorBehavior):
    materia = DictProperty()
    Bm = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint = (.5,.5)

    def getturmas(self):
        app = App.get_running_app()
        self.materia = app.materia
        self.Bm = app.Bm
        self.Turmas = app.Turmas
        self.id = "p6"
        turma_exib = {}
        for turma in self.Turmas:
            numero = turma[0]
            if turma_exib.get(numero, False):
                turma_exib[numero].append(turma[len(turma) - 2])
            else:

                turma_exib[numero] = [turma[len(turma) - 2]]
        numeros = list(turma_exib.keys())
        letras_a = (turma_exib.values())
        letras_d = []
        i=0
        for ano in letras_a:
            l_final = ""
            for Letra in ano:
                l_final += Letra
            letras_d.append(l_final)
            i += 1
        self.numeros = numeros
        self.letras = letras_d
        self.add_widget(Label(color=(0,0,0,1),text="Confirmação de Dados",font_size=20,font_name="Fontes/Inter-Regular",size_hint= (1,0.2)))
        self.add_widget(Label(color=(0,0,0,1),text="Matéria: " + list(self.materia.values())[0],font_size=20,font_name="Fontes/Inter-Regular",size_hint= (1,0.2)))
        self.add_widget(Label(color=(0,0,0,1),text="Bimestre " + str(self.Bm) + "°Bimestre"
                              ,font_size=20,font_name="Fontes/Inter-Regular",size_hint= (1,0.2)))
        self.add_widget(Label(color=(0,0,0,1),text="Turmas",font_size=20,font_name="Fontes/Inter-Regular",size_hint= (1,0.2)))
        for i in range(len(numeros)):
            self.add_widget(Label(color=(0,0,0,1),text=numeros[i]+" "+letras_d[i],font_size=12,font_name="Fontes/Inter-Regular",size_hint= (1,0.2)))


        self.add_widget(BotaoConfirma())

class TabelaConfirma(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.rows = 1
        self.size_hint = (1, .8)
        self.add_widget(Nada1())
        self.add_widget(pnsf)
        self.add_widget(Nada1())




class Login(Screen):
    pass


class Smateria(Screen):
    pass


class Turmas(Screen):
    pass


class Turmas2(Screen):
    pass


class Bimestre(Screen):
    pass


class Confirma(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        global pnsf
        pnsf = PainelConfirma()
        self.add_widget(TabelaConfirma())


class Final(Screen):
    pass
class telaManager(ScreenManager):
    pass


class NotasRO(App):
    PainelLogin = PainelLogin()
    PainelSM = PainelSM()
    PainelTurmas2 = PainelTurmas2()

    email = ""
    senha = ""
    tela = 1
    materia = False
    Turmas = []
    Bm = ""
    series = []
    # turmas = []
    def build(self):
        self.TelaManager = telaManager()
        return self.TelaManager


if __name__ == '__main__':
    NotasRO().run()





