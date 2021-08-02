import sys
sys.path.append("/home/cbravos/UFPR/DS/src/")
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
        return eqMed

    def vincularEquipe(self, idEquipe, idUnidade, iniTurno, fimTurno, escala):
        unidade = UnidadeController.unidadeController.buscarUnidade(idUnidade)
        equipe = session.query(EquipeMedica).get(idEquipe)
        turno = Turno(iniTurno, fimTurno, escala, equipe)
        session.add(turno)
        equipe.unidade = unidade
        session.commit()

    def buscarEquipe(self, idEquipe):
        equipe = session.query(EquipeMedica).get(idEquipe)
        return equipe
    
    def printEquipe(self, equipe):
        print("==Equipe Médica==")
        print(f'ID {equipe.id}')
        print(f'Nome: {equipe.nome}')
        print(f'Chefia: {equipe.chefia}')
        print(f'ID Unidade {equipe.unidadeId}')
        print(f'Turno {equipe.turno.horaInicio} às {equipe.turno.horaTermino}')
        print(f'Escala: {equipe.turno.escala}')

    def printTodasEquipes(self):
        equipes = session.query(EquipeMedica).all()
        for i in equipes:
            self.printEquipe(i)

equipeMedicaController = EquipeMedicaController()
