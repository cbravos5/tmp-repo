import pathlib
import sys, os
sys.path.append(f'{pathlib.Path().resolve()}/src/')
from app.controllers.AlaController import alaController
from app.controllers.SetorController import setorController
from app.controllers.UnidadeController import unidadeController
from app.controllers.LeitoController import leitoController

def criarLeitos():
    print("Insira o id do tipo do leito:")
    leitoController.printTiposLeito()
    idTipo = input()
    os.system('clear')
    print("Insira a quantidade de leitos")
    quantidade = input()
    os.system('clear')
    print("Insira o id da ala:")
    alaController.printAlas()
    idAla = input()
    os.system('clear')
    print("Insira o id do setor:")
    setorController.printSetoresAla(int(idAla))
    idSetor = input()
    os.system('clear')
    print("Insira o id da unidade:")
    unidadeController.printUnidadesSetor(int(idSetor))
    idUnidade = input()
    os.system('clear')
    leitoController.criarLeitos(int(idTipo), int(quantidade), int(idUnidade))
    print("Leitos criados")