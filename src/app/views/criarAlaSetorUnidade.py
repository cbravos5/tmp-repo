import sys
sys.path.append("/home/cbravos/UFPR/DS/src/")
from app.controllers.AlaController import alaController
from app.controllers.SetorController import setorController
from app.controllers.UnidadeController import unidadeController
from app.controllers.LeitoController import leitoController

def criarAlaSetorUnidade():
    print("Insira 1 se deseja criar uma Ala, 2 para Setor, 3 para Unidade")
    criar = input()
    if(criar == '1'):
        print("Insira o nome da Ala")
        nome = input()
        alaController.criarAla(nome)
        print(f'Ala {nome} criada')
    if(criar == '2'):
        print("Insira o id da Ala")
        alaController.printAlas()
        idAla = input()
        print("Insira o nome do Setor")
        nome = input()
        setorController.criarSetor(nome, int(idAla))
        print(f'Setor {nome} criado na ala id {idAla}')
    if(criar == '3'):
        print("Insira o id da Ala")
        alaController.printAlas()
        idAla = input()
        print("Insira o id do Setor")
        setorController.printSetoresAla(int(idAla))
        idSetor = input()
        print("Insira o id do Tipo")
        leitoController.printTiposLeito()
        idTipo = input()
        print("Insira o andar")
        andar = input()
        unidadeController.criarUnidade(int(idTipo), int(idSetor), int(andar))
        print(f'Unidade tipo id {idTipo} criada no setor id {idSetor} no andar {andar}')

criarAlaSetorUnidade()