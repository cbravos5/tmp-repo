import os, time
from app.views.alterarEstadoPaciente import alterarEstadoPaciente
from app.views.consultarMapaLeitos import consultarMapaLeitos
from app.views.criarAlaSetorUnidade import criarAlaSetorUnidade
from app.views.criarEquipe import criarEquipe
from app.views.criarLeitos import criarLeitos
from app.views.darEntradaPaciente import darEntradaPaciente
from app.views.liberarLeito import liberarLeito
from app.views.modificarLeitos import modificarLeitos
from app.views.solicitarLeito import solicitarLeito
from app.views.vincularEquipeUnidade import vincularEquipeUnidade
from app.views.vincularPacienteLeito import vincularPacienteLeito

while(True):
    print("Insira: ")
    print("     1 para dar entrada no paciente")
    print("     2 para alterar o estado de um paciente")
    print("     3 para solicitar um leito")
    print("     4 para vincular um paciente a um leito")
    print("     5 para liberar um leito")
    print("     6 para consultar o mapa de leitos de uma unidade")
    print("     7 para criar uma ala, setor ou unidade")
    print("     8 para criar leitos em uma unidade")
    print("     9 para modificar o tipo e/ou a localização de leitos")
    print("     10 para criar uma nova equipe médica")
    print("     11 para vincular uma equipe a uma unidade")
    print("     Ou insira 0 para sair")

    escolha = int(input())
    os.system("clear")
    if(escolha == 1):
        darEntradaPaciente()
    elif(escolha == 2):
        alterarEstadoPaciente()
    elif(escolha == 3):
        solicitarLeito()
    elif(escolha == 4):
        vincularPacienteLeito()
    elif(escolha == 5):
        liberarLeito()
    elif(escolha == 6):
        consultarMapaLeitos()
    elif(escolha == 7):
        criarAlaSetorUnidade()
    elif(escolha == 8):
        criarLeitos()
    elif(escolha == 9):
        modificarLeitos()
    elif(escolha == 10):
        criarEquipe()
    elif(escolha == 11):
        vincularEquipeUnidade()
    elif(escolha == 0):
        os.system("clear")
        break
    else:
        print("Escolha inválida")
    time.sleep(3)
    os.system("clear")
