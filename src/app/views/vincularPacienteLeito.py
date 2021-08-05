import pathlib
import sys, os
sys.path.append(f'{pathlib.Path().resolve()}/src/')
from app.controllers.PacienteController import pacienteController
from app.controllers.InternacaoController import internacaoController
from app.controllers.LeitoController import leitoController


def vincularPacienteLeito():
    print("Insira o id do paciente:")
    idPaciente = input()
    os.system('clear')
    print("Insira o id do leito")
    idLeito = input()
    os.system('clear')
    paciente = pacienteController.buscarPaciente(int(idPaciente))
    print("Paciente:")
    pacienteController.printPaciente(paciente)
    print("Leito:")
    leito = leitoController.buscarLeito(int(idLeito))
    leitoController.printLeito(leito)
    print("Insira 'S' para confirmar ou 'N' para cancelar")
    confirma = input()
    os.system('clear')
    if(confirma.lower() == 's'):
        internacaoController.vincularPacienteLeito(int(idPaciente), int(idLeito))
        print("Vinculação confirmada")
