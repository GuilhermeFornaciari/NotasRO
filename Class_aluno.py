from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def padronizarnome(linha):  # Trata o nome para remover incoerências oriundas de erros humanos
    caracteresespeciais = "!@#$%¨&*()-=_+,[]{}^~´`/\?°" + "'" + '"'
    nome = linha.upper()

    for caracter in caracteresespeciais:
        if caracter in nome:
            nome = nome.replace(caracter, "")
    while nome[0] == " ":
        nome = nome.replace(" ", "", 1)
    return nome


class aluno:
    def __init__(self, index, bimestre, driver):
        self.url = ""
        self.nome = ""
        self.ativo = False
        self.lancado = False
        self.posicao = 0
        self.nota_site = 0
        self.matriculado = ""
        self.getpropriedades(index, bimestre, driver)

    def geturl(self):
        return self.url

    def seturl(self, url):
        self.url = url

    def getnome(self):
        return self.nome

    def setnome(self, nome):
        self.nome = nome

    def getativo(self):
        return self.ativo

    def setativo(self, ativo):
        self.ativo = ativo

    def getlancado(self):
        return self.lancado

    def setlancado(self,lancado):
        self.lancado = lancado

    def getposicao(self):
        return self.posicao

    def setposicao(self, posicao):
        self.posicao = posicao

    def getnota_site(self):
        return self.nota_site

    def setnota_site(self, nota_site):
        self.nota_site = nota_site

    def getmatriculado(self):
        return self.matriculado

    def setmatriculado(self, matriculado):
        self.matriculado = matriculado

    property(getnome, setnome)
    property(getativo, setativo)
    property(getposicao, setposicao)
    property(getnota_site, setnota_site)
    property(getmatriculado, setmatriculado)

    def getpropriedades(self, index, bimestre, driver):
        url = driver.find_element(By.XPATH, "/html/body/div[2]/form[2]/div[2]/table/tbody/tr[%s]" % index)
        dadosNome = url.get_attribute('outerText').split("\t")
        # Após esta coleta, os nomes obedecem a seguinte formatação:
        # ['16', 'LUAM BRAVO DOS SANTOS', '', '', '', '', 'TRANSFERIDO ESCOLA', '']
        nome = padronizarnome(dadosNome[1])
        url = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, 
             "/html/body/div[2]/form[2]/div[2]/table/tbody/tr[{}]/td[{}]/input".format(dadosNome[0], bimestre + 2))
        ))
        nota = url.get_attribute('value')
        ativo = url.get_attribute('disabled')

        self.seturl(url)
        self.setnome(nome)
        self.setposicao(dadosNome[0])
        self.setmatriculado(dadosNome[len(dadosNome) - 2])
        self.setnota_site(nota)
        self.setativo(ativo)
