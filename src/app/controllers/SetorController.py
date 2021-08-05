import pathlib
import sys
sys.path.append(f'{pathlib.Path().resolve()}/src/')
from database.repo import *
from app.controllers.AlaController import alaController


class SetorController:
    def criarSetor(self, nomeSetor, idAla):
        ala = alaController.buscarAla(idAla)
        setor = Setor(nomeSetor, ala)
        session.add(setor)
        session.commit()
        return setor

    def buscarSetor(self, idSetor):
        setor = session.query(Setor).get(idSetor)
        return setor

    def buscarTodosSetoresAla(self, idAla):
        setoresAla = session.query(Setor).filter(Setor.alaId == idAla).all()
        return setoresAla

    def printSetor(self, setor):
        print("==Setor==")
        print(f'ID {setor.id}')
        print(f'Nome {setor.nome}')
        print(f'ID Ala {setor.alaId}')

    def printSetoresAla(self, idAla):
        setores = self.buscarTodosSetoresAla(int(idAla))
        for i in setores:
            self.printSetor(i)

setorController = SetorController()
