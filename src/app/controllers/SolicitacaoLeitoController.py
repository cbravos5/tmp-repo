from database.repo import *
from app.controllers.PacienteController import pacienteController


class SolicitacaoLeitoController:
    def solicitarLeito(self, idPaciente, tipoLeito, urgencia):
        paciente = pacienteController.buscarPaciente(idPaciente)
        urg = session.query(Urgencia).get(urgencia)
        tipo = session.query(TipoLeito).get(tipoLeito)
        solLeito = SolicitacaoLeito(tipo, urgencia)
        pacienteController.associarPacienteSolicitacao(paciente, solLeito)
        session.add(solLeito)
        session.commit()


solicitacaoLeitoController = SolicitacaoLeitoController()
