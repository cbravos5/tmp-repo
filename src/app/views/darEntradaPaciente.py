import pathlib
import sys, os
sys.path.append(f'{pathlib.Path().resolve()}/src/')
from app.controllers.PacienteController import pacienteController

def darEntradaPaciente():
    print("Insira o CPF do paciente:")
    cpf = input()
    os.system('clear')
    paciente = pacienteController.entrarPaciente(cpf)
    if(paciente):
        print("Dados recebidos")