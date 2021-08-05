import pathlib
import sys, os, time
sys.path.append(f'{pathlib.Path().resolve()}/src/')
from app.controllers.AlaController import alaController
from app.controllers.SetorController import setorController
from app.controllers.UnidadeController import unidadeController
from app.controllers.LeitoController import leitoController

def consultarMapaLeitos():
    print("Insira o id da Ala:")
    alaController.printAlas()
    idAla = input()
    os.system('clear')
    print("Insira o id do Setor:")
    setorController.printSetoresAla(int(idAla))
    idSetor = input()
    os.system('clear')
    print("Insira o id da Unidade:")
    unidadeController.printUnidadesSetor(int(idSetor))
    idUnidade = input()
    os.system('clear')
    print(f'Leitos da unidade {int(idUnidade)}')
    leitoController.printLeitosUnidade(int(idUnidade))
    input("Aperta qualquer tecla para sair")