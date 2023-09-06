from difflib import SequenceMatcher
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Class_aluno import padronizarnome
from Class_aluno import aluno
from Leituradedados import lertabelas

#     color: 0.3,0.6,0.7,1
def login(cpf, senha):
    # Auto explicativo
    id_box = driver.find_element(By.NAME, 'cpf')
    id_box.send_keys(cpf)

    psswd_box = driver.find_element(By.NAME, 'password')
    psswd_box.send_keys(senha)

    autenticarbotao = driver.find_element(By.ID, 'LoginButton')
    autenticarbotao.click()


def Procurar_turmas():
    # Acessa a pagina inicial para notas
    notasbotao = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/a')
    notasbotao.click()
    # Seleciona a turma desejada
    elementos = driver.find_element(By.ID, 't')
    turmas = elementos.find_elements(By.TAG_NAME, "option")

    values, series = [], []
    for option in turmas:
        values.append(option.get_attribute("value"))
        series.append(option.get_attribute("text"))
    Series_Values = {}

    for i in range(1, len(values)):
        text = series[i].split("-")
        ano = text[1][1]
        text = ano + "º ano" + text[len(text) - 1] + " "

        Series_Values[text] = values[i]
    return (Series_Values)


def envianotas():
    # Aperta o botão, espera o pop up de confirmação em seguida o aceita
    enviarnotas = driver.find_element(By.XPATH, "/html/body/div[2]/form[2]/div[3]/button[1]")
    enviarnotas.click()
    alert = WebDriverWait(driver, 10).until(ec.alert_is_present())
    alert.accept()


def descobrirvalorcorreto(v_repetido, Aturma):
    for index in v_repetido:
        if Aturma[index].getmatriculado() == "MATRICULADO":
            return index
    else:
        return index
    # A ideia é procurar pela opção matriculada, se caso nenhum for matriculado, podemos entregar qualquer um pois
    # O processo irá parar na verificação de alunos transferidos na função lançarnota


def comparanomes(Aturma, Aarquivo):
    pontuacao = []
    for A in Aturma:
        nomeT = A.getnome()
        nomeA = Aarquivo[0]
        pontos = SequenceMatcher(None, nomeT, nomeA).ratio()
        pontuacao.append(pontos)

    max_valor = max(pontuacao)
    # print(max_valor)

    if max_valor < 0.80:
        return -10

    if pontuacao.count(max_valor) > 1:
        val = pontuacao
        posicao_v_repetido = []
        try:
            while 1:
                posicao_v_repetido.append(pontuacao.index(max_valor) + len(posicao_v_repetido))
                val.pop(pontuacao.index(max_valor))
        except:
            idxvalor = descobrirvalorcorreto(posicao_v_repetido, Aturma)
    else:
        idxvalor = pontuacao.index(max_valor)

    return Aturma[idxvalor]


def lancarnota(alunoS, notaarquivo, nome, sobrepor):
    global erros
    if alunoS == -10:
        print("O aluno %s não está presente nesta turma" % nome)
        return

    nota_site = alunoS.getnota_site().replace(",", "")
    # print(nome, nota_site, notaarquivo)

    url = alunoS.geturl()
    if alunoS.getativo():  # Se o aluno estiver ativo e não foi remanejado/transferido
        print("O aluno %s foi transferido ou remanejado, porém sua tabela indica que está matriculado"
              % alunoS.getnome())
        return

    if alunoS.getlancado():
        erros += 1
        print("Por favor, verifique a nota do aluno %s " % alunoS.getnome())
        url.clear()
        return

    if alunoS.getnota_site() == "":
        url.send_keys(notaarquivo)
        alunoS.setlancado(True)
        return
    elif float(nota_site) == float(notaarquivo):
        return

    if sobrepor is None:
        escolhas = {"1": True, "2": False}
        print(nome, nota_site, notaarquivo)
        print("As notas já lançadas no sistema divergem em relação às notas da planilha")
        sobrepor = escolhas.get(input("Qual deseja manter? 1 para sobrepor 2 para manter as notas do site"))

    if sobrepor:
        url.clear()
        url.send_keys(notaarquivo)


def executarprograma(Bm, usuario, senha):
    global driver
    erros = 0
    sobrepor = None

    # Bm = 4
    lertabelas(Bm)

    # Using Chrome to access web
    driver = webdriver.Chrome()

    # Open the website
    driver.get("https://diario.seduc.ro.gov.br/login.php")
    driver.maximize_window()
    login(usuario, senha)

    Series_Values = Procurar_turmas()
    print(Series_Values)

    primeira = True
    with open("notas.txt", "r") as n:
        for linha in n.readlines():
            if linha[0] == "#":
                if primeira:
                    primeira = False
                else:
                    # envianotas()
                    x = 0
                print()
                linha = linha.replace("#", "")
                linha = linha.replace("\n", "")

                if linha == "":  # Se a lista estiver vazia significa que o txt terminou de ser lido,
                    # Portanto não faz sentido continuar
                    break

                if linha[len(linha) - 1] != " ":  # Caso o arquivo não possua o espaçamento final
                    linha += " "

                id = Series_Values.get(linha)
                print(linha)
                link = "https://diario.seduc.ro.gov.br/professor/nota.php?t=%s&d=187&e=1" % id
                for i in range(2):
                    driver.get(link)
                tabelaalunos = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located((By.XPATH, "/html/body/div[2]/form[2]/div[2]/table")))
                alunos = tabelaalunos.find_elements(By.TAG_NAME, "tr")
                alunos_turma = []

                for i in range(1, len(alunos) - 1):
                    alunos_turma.append(aluno(i, Bm, driver))


            else:
                aluno_arquivo = padronizarnome(linha)
                aluno_arquivo = aluno_arquivo.split(";")

                aluno_arquivo[4] = aluno_arquivo[4].replace("\n", "")
                aluno_arquivo[Bm] = int(float(aluno_arquivo[Bm]) * 10)
                
                alunoS = comparanomes(alunos_turma, aluno_arquivo)
                lancarnota(alunoS, aluno_arquivo[Bm], aluno_arquivo[0], sobrepor)

    print(erros)

# print(alunos_turma[i-1].getposicao(),alunos_turma[i-1].getnome(),alunos_turma[i-1].getmatriculado(),
# alunos_turma[i-1].getnota_site(),alunos_turma[i-1].getativo())
