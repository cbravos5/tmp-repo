import pathlib
import sys, os
sys.path.append(f'{pathlib.Path().resolve()}/src/')
from app.controllers.EquipeMedicaController import equipeMedicaController
from app.controllers.FuncionarioController import funcionarioController

def criarEquipe():
    print("Insira o nome da nova equipe")
    nomeEquipe = input()
    os.system('clear')
    continuar = 's'
    listaFuncionariosId = []
    while(continuar.lower() == 's'):
        print("Selecione o ID do funcionário a ser insirido na equipe")
        funcionarioController.printFuncionarios()
        idFuncionario = input()
        os.system('clear')
        if int(idFuncionario) not in listaFuncionariosId:
            listaFuncionariosId.append(int(idFuncionario))
        print("Insira 'S' se deseja insirir mais funcionários, senão 'N'")
        continuar = input()
    os.system('clear')
    print("Selecione o ID do funcionário responsável pela equipe")
    for i in listaFuncionariosId:
        funcionario = funcionarioController.buscaFuncionario(i)
        funcionarioController.printFuncionario(funcionario)
    idFuncionario = input()
    responsavel = funcionarioController.buscaFuncionario(int(idFuncionario))
    os.system('clear')
    novaEquipe = equipeMedicaController.criarEquipe(nomeEquipe, listaFuncionariosId, responsavel.nome)
    print("Equipe criada")
    return novaEquipe.id