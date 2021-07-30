from database.repo import *
import app.controllers.FuncionarioController as FuncionarioController
import app.controllers.UnidadeController as UnidadeController


class EquipeMedicaController:

    def criarEquipe(self, nomeEquipe, listaFuncionarios, chefia):
        eqMed = EquipeMedica(nomeEquipe, chefia)
        for funcionarioId in listaFuncionarios:
            funcionario = FuncionarioController.funcionarioController.buscaFuncionario(
                funcionarioId)
            UnidadeController.funcionarioController.associarFuncionarioEquipe(
                funcionario, eqMed)
        session.add(eqMed)
        session.commit()

    def vincularEquipe(self, idEquipe, idUnidade, iniTurno, fimTurno, escala):
        unidade = UnidadeController.unidadeController.buscarUnidade(idUnidade)
        equipe = session.query(EquipeMedica).get(idEquipe)
        turno = Turno(iniTurno, fimTurno, escala, equipe)
        session.add(turno)
        equipe.unidade = unidade
        session.commit()


equipeMedicaController = EquipeMedicaController()
