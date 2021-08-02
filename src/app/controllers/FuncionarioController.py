import sys
sys.path.append("/home/cbravos/UFPR/DS/src/")
from database.repo import *

class FuncionarioController:
    def criarFuncionario(self,nome, cpf, contato, cargo):
        funcionario = Funcionario(nome, cpf, contato, cargo)
        session.add(funcionario)
        session.commit()
        return funcionario

    def buscaFuncionario(self, funcionarioId):
        funcionario = session.query(Funcionario).get(funcionarioId)
        return funcionario

    def associarFuncionarioEquipe(self, funcionario, eqMed):
        funcionario.equipeMedica = eqMed


funcionarioController = FuncionarioController()
