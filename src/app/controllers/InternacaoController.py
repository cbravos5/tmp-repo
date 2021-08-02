from database.repo import *
import app.controllers.LeitoController as LeitoController
import app.controllers.PacienteController as PacienteController


class InternacaoController:
    def setStatus(self, inter, status):
        inter.status = status

    def setMotivoEncerramento(self, inter, motivo):
        inter.motivoEncerramento = motivo

    def alterarStatusPaciente(self, idLeito, status):
        inter = session.query(Internacao).filter(
            Internacao.leitoId == idLeito).first()
        self.setStatus(inter, status)
        session.commit()

    def gerarRecomendacao(self, idLeito, recomendacao):
        inter = session.query(Internacao).filter(
            Internacao.idLeito == idLeito).first()
        action = AcaoRecomendada(recomendacao, inter)
        session.add(action)
        session.commit()
        return action

    def encerrarInternacao(self, internacao, motivo):
        self.setStatus(internacao, 'encerrada')
        self.setMotivoEncerramento(internacao, motivo)
        LeitoController.leitoController.setDisponibilidade(
            internacao.leito, 'desocupado')

    def vincularPacienteLeito(self, idPaciente, idLeito):
        leito = LeitoController.leitoController.buscarLeito(idLeito)
        paciente = PacienteController.pacienteController.buscarPaciente(
            idPaciente)
        inter = Internacao(leito)
        PacienteController.pacienteController.associarPacienteInternacao(
            paciente, inter)
        PacienteController.pacienteController.removerSolicitacao(paciente)
        LeitoController.leitoController.setDisponibilidade(leito, 'ocupado')
        session.add(inter)
        session.commit()


internacaoController = InternacaoController()
