import pathlib
import sys, os
sys.path.append(f'{pathlib.Path().resolve()}/src/')
from app.controllers.AlaController import alaController
from app.controllers.SetorController import setorController
from app.controllers.UnidadeController import unidadeController
from app.controllers.LeitoController import leitoController

def modificarLeitos():
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
    listaLeitoModificar = []
    confirma = 's'
    listaLeitos = leitoController.consultarLeitos(int(idUnidade))
    while(confirma.lower() == 's'):
        print("Selecione o id do leito")
        for i in listaLeitos:
            if(i.disponibilidade == 'desocupado'):
                leitoController.printLeito(i)
        idLeito = input()
        os.system('clear')
        leito = leitoController.buscarLeito(int(idLeito))
        if leito not in listaLeitoModificar:
            listaLeitoModificar.append(leito)
        print("Insira 'S' se deseja selecionar mais leitos, senão 'N'")
        confirma = input()
        os.system('clear')
    print("Insira 'S' se deseja alterar o tipo dos leitos, senão 'N'")
    alterar = input()
    os.system('clear')
    idTipo = listaLeitoModificar[0].tipoId
    if(alterar.lower() == 's'):
        print("Selecione o id do novo tipo dos leitos")
        leitoController.printTiposLeito()
        idTipo = input()
        os.system('clear')
    print("*Insira a nova localização dos leitos*")
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
    leitoController.modificarLeitos(int(idTipo), listaLeitoModificar, int(idUnidade))
    print("Leitos modificados")