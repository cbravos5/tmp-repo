import sys
sys.path.append("/home/cbravos/UFPR/DS/src/")
from database.repo import *


class AlaController:
    def criarAla(self,nome):
        ala = Ala(nome=nome)
        session.add(ala)
        session.commit()
        return ala

    def buscarAla(self,idAla):
        ala = session.query(Ala).get(idAla)
        return ala

    def buscarTodasAlas(self):
        alas = session.query(Ala).all()
        return alas

    def printAla(self, ala):
        print("==Ala==")
        print(f'ID {ala.id}')
        print(f'Nome {ala.nome}')

    def printAlas(self):
        alas = self.buscarTodasAlas()
        for i in alas:
            self.printAla(i)

alaController = AlaController()
