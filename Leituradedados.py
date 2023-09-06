import pandas as pd
import os


def e_Numero(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def aluno_Matriculado(serie, bm, i):
    bimestres = {1: "Unnamed: 5", 2: "Unnamed: 9", 3: "Unnamed: 13", 4: "Unnamed: 17"}
    coluna = bimestres.get(bm)
    if e_Numero(serie[coluna][i]):
        return True
    else:
        return False


def lertabelas(bm):
    # Build tuple of (class, file) to turn in
    submission_dir = 'TabelasExcel'
    dir_list = list(os.listdir(submission_dir))
    caminhopasta = os.getcwd() + "\TabelasExcel"
    with open("notas.txt", "w") as n:
        n.write("#")
    for tabela in dir_list:
        caminhotabela = caminhopasta + "\%s" % tabela
        print(caminhotabela)
        planilha = pd.read_excel(caminhotabela, None, skiprows=15, usecols="B,F,J,N,R")
        for serie in planilha.keys():
            with open("notas.txt", "a") as n:
                n.write("%s \n" % serie)
            i = 0
            for Al in planilha[serie]["Unnamed: 1"]:  # Fazer isto para todos os nomes
                if planilha[serie]["Unnamed: 1"].notnull()[i]:  # Se o nome não for nulo, continua
                    if aluno_Matriculado(planilha[serie], bm, i):
                        # Se a informação for no campo da nota bimestral for um numero continua (isto garante que todos
                        # Os casos de Tranferido ou remanejados não sejam exportados para o txt, reduzindo o tempo de
                        # processamento do aplicativo

                        if Al[len(Al) - 3] == "A" and Al[len(Al) - 1] == "E":
                            Al = Al[:len(Al) - 3]
                        while Al[len(Al) - 1] == " ":
                            Al = Al[:len(Al) - 1]
                        with open("notas.txt", "a") as n:
                            n.write(str(Al))
                            n.write(";")
                            n.write(str(planilha[serie]["Unnamed: 5"][i]))
                            n.write(";")
                            n.write(str(planilha[serie]["Unnamed: 9"][i]))
                            n.write(";")
                            n.write(str(planilha[serie]["Unnamed: 13"][i]))
                            n.write(";")
                            n.write(str(planilha[serie]["Unnamed: 17"][i]))
                            n.write("\n")
                    i += 1
                else:
                    break
            with open("notas.txt", "a") as n:
                n.write("#")
