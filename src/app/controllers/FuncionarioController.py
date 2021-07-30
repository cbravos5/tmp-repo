from database.repo import *


class FuncionarioController:
    def buscaFuncionario(self, funcionarioId):
        funcionario = session.query(Funcionario).get(funcionarioId)
        return funcionario

    def associarFuncionarioEquipe(self, funcionario, eqMed):
        funcionario.equipeMedica = eqMed


funcionarioController = FuncionarioController()
