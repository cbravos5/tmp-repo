import pathlib
import sys
sys.path.append(f'{pathlib.Path().resolve()}/src/')
from database.repo import *
from app.controllers.PacienteController import pacienteController


class SolicitacaoLeitoController:
    def solicitarLeito(self, idPaciente, tipoLeito, urgencia):
        paciente = pacienteController.buscarPaciente(idPaciente)
        solLeito = SolicitacaoLeito(tipoLeito, urgencia)
        pacienteController.associarPacienteSolLeito(paciente, solLeito)
        session.add(solLeito)
        session.commit()
        return solLeito


solicitacaoLeitoController = SolicitacaoLeitoController()
