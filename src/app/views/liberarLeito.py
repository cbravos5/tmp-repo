import pathlib
import sys, os
sys.path.append(f'{pathlib.Path().resolve()}/src/')
from app.controllers.PacienteController import pacienteController

def liberarLeito():
    print("Insira o id do paciente:")
    idPaciente = input()
    os.system('clear')
    paciente = pacienteController.buscarPaciente(int(idPaciente))
    pacienteController.printPaciente(paciente)
    print("Insira o motivo da liberação:")
    motivo = input()
    os.system('clear')
    pacienteController.liberarLeito(int(idPaciente), motivo)
    print("Leito liberado")