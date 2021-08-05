import pathlib
import sys, os
sys.path.append(f'{pathlib.Path().resolve()}/src/')
from app.controllers.AlaController import alaController
from app.controllers.SetorController import setorController
from app.controllers.UnidadeController import unidadeController
from app.controllers.LeitoController import leitoController
from app.controllers.EquipeMedicaController import equipeMedicaController
from app.views.criarEquipe import criarEquipe

def convertToNumber(turno):
    hour,minute = turno.split(':')
    return int(hour)*60 + int(minute)

def verificarConflitos(idUnidade, iniTurno, fimTurno, escala):
    inicioAtual = convertToNumber(iniTurno)
    fimAtual = convertToNumber(fimTurno)
    escalaAtual = escala.split('-')
    equipes = equipeMedicaController.buscarEquipesPorUnidade(idUnidade)
    for equipe in equipes:
        if(equipe.turno):
            inicioAd = convertToNumber(equipe.turno.horaInicio)
            fimAd = convertToNumber(equipe.turno.horaTermino)
            escalaAd = equipe.turno.escala.split('-')
            if((inicioAd <= inicioAtual < fimAd) or (inicioAd < fimAtual <= fimAd)):
                for dia in escalaAtual:
                    if dia in escalaAd:
                        return [equipe.nome,equipe.id]
    return False


def editarVinculos(idEquipe):
    while(True):
        print("Insira o id da Ala")
        alaController.printAlas()
        idAla = input()
        os.system('clear')
        print("Insira o id do Setor")
        setorController.printSetoresAla(int(idAla))
        idSetor = input()
        os.system('clear')
        print("Insira o id da Unidade")
        unidadeController.printUnidadesSetor(int(idSetor))
        idUnidade = input()
        os.system('clear')
        print("Insira o início do turno")
        print("Formato: HH:MM")
        iniTurno = input()
        os.system('clear')
        print("Insira o término do turno")
        print("Formato: HH:MM")
        fimTurno = input()
        os.system('clear')
        print("Insira a escala")
        print("Formato: seg-ter-dom-...")
        escala = input()
        os.system('clear')
        conflitos = verificarConflitos(idUnidade,iniTurno,fimTurno,escala)
        if(conflitos):
            print(f'Há um conflito de turno/equipe/unidade com a equipe {conflitos[0]}, {conflitos[1]}')
            print("Se deseja editar os vínculos e turnos digite 'S' senão digite 'N' para cancelar")
            if(input().lower() == 's'):
                os.system('clear')
                continue
            os.system('clear')
            return
        equipeMedicaController.vincularEquipe(int(idEquipe), int(idUnidade), iniTurno, fimTurno, escala)
        print("Equipe vinculada")
        break

def vincularEquipeUnidade():
    equipeMedicaController.printTodasEquipes()
    print("Se deseja criar uma nova equipe insira 'S' senão insira o id da equipe")
    idEquipe = input()
    os.system('clear')
    if(idEquipe.lower() != 's'):
        editarVinculos(idEquipe)
    if(idEquipe.lower() == 's'):
        idEquipe = criarEquipe()
        editarVinculos(idEquipe)