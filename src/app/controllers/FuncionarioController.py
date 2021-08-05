import pathlib
import sys
sys.path.append(f'{pathlib.Path().resolve()}/src/')
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

    def printFuncionarios(self):
        funcionarios = session.query(Funcionario).all()
        for i in funcionarios:
            self.printFuncionario(i)

    def printFuncionario(self, funcionario):
        print("===Funcionário===")
        print(f'ID {funcionario.id}')
        print(f'Nome: {funcionario.nome}')
        print(f'CPF {funcionario.cpf}')
        print(f'Cargo: {funcionario.cargo}')


funcionarioController = FuncionarioController()
