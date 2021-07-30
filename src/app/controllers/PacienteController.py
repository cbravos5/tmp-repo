from database.repo import *
from app.api.CHCapi import api
import app.controllers.InternacaoController as InternacaoController


class PacienteController:
    def entrarPaciente(self, id):
        info = api.buscarPaciente(id)
        paciente = Paciente(info[0], info[1], info[2])
        session.add(paciente)
        session.commit()

    def liberarLeito(self, idPaciente, motivo):
        paciente = session.query(Paciente).get(idPaciente)
        InternacaoController.internacaoController.encerrarInternacao(
            paciente.internacao)
        session.commit()

    def buscarPaciente(self, idPaciente):
        paciente = session.query(Paciente).get(idPaciente)
        return paciente

    def associarPacienteLeito(self, paciente, solLeito):
        paciente.solicitacaoLeito = solLeito

    def associarPacienteInternacao(self, paciente, inter):
        paciente.internacao = inter

    def removerSolicitacao(self, paciente):
        id = paciente.solicitacaoLeito.id
        session.query(SolicitacaoLeito).filter(SolicitacaoLeito.id == id).delete(
            synchronize_session='evaluate')


pacienteController = PacienteController()
