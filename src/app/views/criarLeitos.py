import sys
sys.path.append("/home/cbravos/UFPR/DS/src/")
from app.controllers.AlaController import alaController
from app.controllers.SetorController import setorController
from app.controllers.UnidadeController import unidadeController
from app.controllers.LeitoController import leitoController

def criarLeitos():
    print("Insira o id do tipo do leito:")
    leitoController.printTiposLeito()
    idTipo = input()
    print("Insira a quantidade de leitos")
    quantidade = input()
    print("Insira o id da ala:")
    alaController.printAlas()
    idAla = input()

    print("Insira o id do setor:")
    setorController.printSetoresAla(int(idAla))
    idSetor = input()

    print("Insira o id da unidade:")
    unidadeController.printUnidadesSetor(int(idSetor))
    idUnidade = input()

    print("Insira o andar:")
    andar = input()

    leitoController.criarLeitos(int(idTipo), int(quantidade), int(idUnidade))
    print("Leitos criados")


criarLeitos()