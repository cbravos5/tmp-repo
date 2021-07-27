from database.repo import *


class AlaController:
    def index(self):
        alas = session.query(Ala).all()
        return alas

    def addAla(self,nome):
        novaAla = Ala(nome=nome)
        session.add(novaAla)
        session.commit()

    def getAla(self,id):
        ala = session.query(Ala).get(id)
        return ala


alaController = AlaController()
