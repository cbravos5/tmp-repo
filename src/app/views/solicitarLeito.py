import sys
sys.path.append("/home/cbravos/UFPR/DS/src/")
from app.controllers.SolicitacaoLeitoController import solicitacaoLeitoController

def solicitarLeito():
    print("Insira o id do paciente:")
    id = input()
    print("Insira o tipo do leito:")
    tipo = input()
    print("Insira a urgência:")
    urgencia = input()
    if(solicitacaoLeitoController.solicitarLeito(int(id), int(tipo), int(urgencia))):
        print("Solicitação confirmada")
