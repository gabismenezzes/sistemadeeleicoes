import pandas as pd
import PySimpleGUI as sg
import os
from validate_docbr import CPF
import math
from openpyxl import Workbook, load_workbook

funcionarios_ativos = []
listaAtivos = pd.read_excel('Candidatos.xlsx')

for k,v in enumerate(listaAtivos['Nome do Funcionario']):
    if len(v) > 1:
        funcionarios_ativos.append(v)

working_directory = os.getcwd()
font = ("Arial", 7)

cabecalho = [  
    [sg.Text("Selecione a planilha de dados:"),
    sg.InputText(key="-FILE_PATH-"),sg.FileBrowse(initial_folder=working_directory)],
    [sg.HorizontalSeparator()],
]

esquerda = [
    [sg.Text("Nome Completo:"), sg.InputText(key='nome', size=28)],
    [sg.Text("CPF:"), sg.InputText(key='cpf', size=13)],
    [sg.Text("Obs.: Somente números", text_color='black', font=font)],
]

areavotacao = [
    [sg.Text("Em quem gostaria de votar?")],
    [sg.Listbox(funcionarios_ativos, size=(max(map(len, funcionarios_ativos))+2, 10), key='LISTBOX')]
]

checkbox = [
    [sg.Checkbox('Declaro ter certeza da votação e que não será possível votar novamente.', key='Checkbox', default=False)]
]

submit = [
    [sg.Button('Votar', border_width=2)]
]

layout = [
    [sg.Column(esquerda, vertical_alignment='left', element_justification='left')],
    [sg.Column(areavotacao, vertical_alignment='left', element_justification='left')],
    [sg.Column(checkbox, vertical_alignment='left', element_justification='left')],
    [sg.Column(submit, vertical_alignment='center', justification='center')],
]

window = sg.Window("Sistema de Voto", layout)

def isNan(value):
    try:
        return math.isnan(float(value))
    except:
        return False


def checkRepetido(cpf):
    blacklist = pd.read_excel('CPF Que ja votaram.xlsx', dtype=str)
    for k,v in enumerate(blacklist["CPFs"]):
        print(v)
        if cpf == v:
            return False
    
    return True

def colocarEmBlackList(cpf):
    blacklist = load_workbook('CPF Que ja votaram.xlsx')
    aba = blacklist.active

    for n in aba["A"]:
        linha = n.row
        if n.value == "*":
            aba[f"A{linha}"] = cpf
            break
    blacklist.save('CPF Que ja votaram.xlsx')

def computarVoto(nome, cpf, voto):
    computar = pd.read_excel('contador de votos.xlsx', dtype=str)
    checar = checkRepetido(cpf)
    if not checar:
        return sg.popup("Este CPF ja votou")
    
    for k,v in enumerate(computar['Quantidade de Votos']):
        canditatos = computar.loc[k, "Candidatos"]
        if voto == canditatos:
            votos = computar.loc[k, "Quantidade de Votos"]
            novoValor = int(votos) + 1
            computar.loc[k, "Quantidade de Votos"] = str(novoValor)
            computar.to_excel("contador de votos.xlsx", index=False)
            colocarEmBlackList(cpf)


def validadorCPF(cpfrecebido):
    cpf = CPF()
    if cpf.validate(cpfrecebido):
        return True
    else:
        return False


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == "Votar":
        nome = values["nome"]
        cpf = values["cpf"]
        LISTBOX = values["LISTBOX"]
        Checkbox = values["Checkbox"]
        if len(nome) >= 7:
            if validadorCPF(cpf):
                if LISTBOX:
                    for voto in LISTBOX:
                        meuVoto = voto
                    if Checkbox:
                        if checkRepetido(cpf):
                            computarVoto(nome, cpf, meuVoto)
                        else:
                            sg.popup("Esse CPF já voltou.")
                    else:
                        sg.popup("Concorde com os termos de votação.")
                else:
                    sg.popup("Selecione qual seu voto.")
            else:
                sg.popup("CPF invalido")
        else:
            sg.popup("Coloque seu nome completo")
        

window.close()