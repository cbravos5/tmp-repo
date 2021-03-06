import pathlib
import sys, os
sys.path.append(f'{pathlib.Path().resolve()}/src/')
from app.controllers.AlaController import alaController
from app.controllers.SetorController import setorController
from app.controllers.UnidadeController import unidadeController
from app.controllers.LeitoController import leitoController
from app.controllers.PacienteController import pacienteController
from app.controllers.InternacaoController import internacaoController

def alterarEstadoPaciente():
    print("Insira o id da Ala:")
    alaController.printAlas()
    idAla = input()
    os.system('clear')
    print("Insira o id do Setor:")
    setorController.printSetoresAla(int(idAla))
    idSetor = input()
    os.system('clear')
    print("Insira o id da Unidade:")
    unidadeController.printUnidadesSetor(int(idSetor))
    idUnidade = input()
    os.system('clear')
    print("Insira o id do Leito a alterar:")
    leitoController.printLeitosUnidade(int(idUnidade))
    idLeito = input()
    os.system('clear')
    leito = leitoController.buscarLeito(int(idLeito))
    if(leito.internacao):
        pacienteController.printPaciente(leito.internacao.paciente)

        print("Insira o novo estado:")
        estado = input()
        os.system('clear')
        internacaoController.alterarStatusPaciente(int(idLeito), estado)
        print("Estado alterado")
    else:
        print("Não há paciente nesse leito")