import sys
sys.path.append("/home/cbravos/UFPR/DS/src/")
from app.controllers.PacienteController import pacienteController

def darEntradaPaciente():
    print("Insira o CPF do paciente:")
    cpf = input()
    paciente = pacienteController.entrarPaciente(cpf)
    if(paciente):
        print("Dados recebidos")

