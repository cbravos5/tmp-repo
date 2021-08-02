import sys
sys.path.append("/home/cbravos/UFPR/DS/src/")
from app.controllers.AlaController import alaController
from app.controllers.SetorController import setorController
from app.controllers.UnidadeController import unidadeController
from app.controllers.LeitoController import leitoController

def alterarEstadoPaciente():
    print("Insira o id da Ala:")
    alaController.printAlas()
    idAla = input()

    print("Insira o id do Setor:")
    setorController.printSetoresAla(int(idAla))
    idSetor = input()

    print("Insira o id da Unidade:")
    unidadeController.printUnidadesSetor(int(idSetor))
    idUnidade = input()

    print("Insira o id do Leito a alterar:")
    leitos = leitoController.consultarLeitos(int(idUnidade))
    for i in leitos:
        if(i.disponibilidade.lower() == 'ocupado'):
            leitoController.printLeito(i)
    idLeito = input()
    leito = leitoController.buscarLeito(int(idLeito))
    pacienteController.printPaciente(leito.internacao.paciente)

    print("Insira o novo estado:")
    estado = input()
    internacaoController.alterarEstadoPaciente(int(idLeito), estado)
    print("Estado alterado")
