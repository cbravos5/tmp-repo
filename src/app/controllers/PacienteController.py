import pathlib
import sys
sys.path.append(f'{pathlib.Path().resolve()}/src/')
import app.controllers.InternacaoController as InternacaoController
from database.repo import *
from app.api.CHCapi import api

class PacienteController:
    def entrarPaciente(self, cpf):
        info = api.buscarPaciente(cpf)
        paciente = Paciente(info[1], info[2], info[3])
        session.add(paciente)
        session.commit()
        return paciente

    def liberarLeito(self, idPaciente, motivo):
        paciente = session.query(Paciente).get(idPaciente)
        InternacaoController.internacaoController.encerrarInternacao(
            paciente.internacao, motivo)
        session.commit()

    def buscarPaciente(self, idPaciente):
        paciente = session.query(Paciente).get(idPaciente)
        return paciente

    def associarPacienteSolLeito(self, paciente, solLeito):
        paciente.solicitacaoLeito = solLeito

    def associarPacienteInternacao(self, paciente, inter):
        paciente.internacao = inter

    def removerSolicitacao(self, paciente):
        id = paciente.solicitacaoLeito.id
        paciente.solicitacaoLeito = None
        session.query(SolicitacaoLeito).filter(SolicitacaoLeito.id == id).delete(
            synchronize_session='evaluate')

    def printPaciente(self, paciente):
        print("==Paciente==")
        print(f'ID {paciente.id}')
        print(f'Nome {paciente.nome}')
        print(f'CPF {paciente.cpf}')
        print(f'Contato {paciente.contato}')


pacienteController = PacienteController()
