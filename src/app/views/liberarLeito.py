import sys
sys.path.append("/home/cbravos/UFPR/DS/src/")
from app.controllers.PacienteController import pacienteController

def liberarLeito():
    print("Insira o id do paciente:")
    idPaciente = input()
    paciente = pacienteController.buscarPaciente(int(idPaciente))
    pacienteController.printPaciente(paciente)
    print("Insira o motivo da liberação:")
    motivo = input()
    pacienteController.liberarLeito(int(idPaciente), motivo)
    print("Leito liberado")