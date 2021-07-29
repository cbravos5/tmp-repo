from database.repo import *


class SetorController:
    def index(self):
        setores = session.query(Setor).all()
        return setores

    def addSetor(self, nome, idAla):
        novoSetor = Setor(nome=nome)
        novoSetor.alaId = idAla
        session.add(novoSetor)
        session.commit()

    def getSetor(self, id):
        setor = session.query(Setor).get(id)
        return setor

    def getSetoresAla(self, idAla):
        setores = session.query(Setor).filter(Setor.alaId == idAla).all()
        return setores


setorController = SetorController()
