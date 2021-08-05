import pathlib
import sys, os
sys.path.append(f'{pathlib.Path().resolve()}/src/')
from app.controllers.SolicitacaoLeitoController import solicitacaoLeitoController

def solicitarLeito():
    print("Insira o id do paciente:")
    identifier = input()
    os.system('clear')
    print("Insira o tipo do leito:")
    tipo = input()
    os.system('clear')
    print("Insira a urgência:")
    urgencia = input()
    os.system('clear')
    if(solicitacaoLeitoController.solicitarLeito(int(identifier), int(tipo), int(urgencia))):
        print("Solicitação confirmada")
