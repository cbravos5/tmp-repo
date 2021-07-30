from database.repo import *
from app.controllers.AlaController import alaController


class SetorController:
    def criarSetor(self, nomeSetor, idAla):
        ala = alaController.buscarAla(idAla)
        novoSetor = Setor(nomeSetor, ala)
        session.add(novoSetor)
        session.commit()

    def buscarSetor(self, idSetor):
        setor = session.query(Setor).get(idSetor)
        return setor


setorController = SetorController()
