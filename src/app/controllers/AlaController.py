from database.repo import *


class AlaController:
    def criarAla(self,nome):
        novaAla = Ala(nome=nome)
        session.add(novaAla)
        session.commit()

    def buscarAla(self,idAla):
        ala = session.query(Ala).get(idAla)
        return ala

alaController = AlaController()
