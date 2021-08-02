import sys
sys.path.append("/home/cbravos/UFPR/DS/src/")
from app.controllers.PacienteController import pacienteController
from app.controllers.InternacaoController import internacaoController
from app.controllers.LeitoController import leitoController


def vincularPacienteLeito():
    print("Insira o id do paciente:")
    idPaciente = input()
    print("Insira o id do leito")
    idLeito = input()

    paciente = pacienteController.buscarPaciente(int(idPaciente))
    print("Paciente:")
    pacienteController.printPaciente(paciente)
    print("Leito:")
    leito = leitoController.buscarLeito(int(idLeito))
    leitoController.printLeito(leito)
    print("Insira 'S' para confirmar ou 'N' para cancelar")
    confirma = input()
    if(confirma.lower() == 's'):
        internacaoController.vincularPacienteLeito(int(idPaciente), int(idLeito))
        print("Vinculação confirmada")
