import sys
sys.path.append("/home/cbravos/UFPR/DS/src/")
from app.controllers.AlaController import alaController
from app.controllers.SetorController import setorController
from app.controllers.UnidadeController import unidadeController
from app.controllers.LeitoController import leitoController
from app.controllers.EquipeMedicaController import equipeMedicaController

def vincularEquipeUnidade():
    print("Insira o id da Ala")
    alaController.printAlas()
    idAla = input()
    print("Insira o id do Setor")
    setorController.printSetoresAla(int(idAla))
    idSetor = input()
    print("Insira o id da Unidade")
    unidadeController.printUnidadesSetor(int(idSetor))
    idUnidade = input()
    equipeMedicaController.printTodasEquipes()
    print("Se deseja criar uma nova equipe insira 'S' senão insira o id da equipe")
    idEquipe = input()
    if(idEquipe.lower() != 's'):
        print("Insira o início do turno")
        iniTurno = input()
        print("Insira o término do turno")
        fimTurno = input()
        print("Insira a escala")
        escala = input()
        # todo: fazer a verificação dos dados
        equipeMedicaController.vincularEquipeUnidade(int(idEquipe), int(idUnidade), int(iniTurno), int(fimTurno), escala)
        print("Equipe vinculada")
    if(idEquipe.lower() == 's'):
        # todo