from database.repo import *
from app.controllers.SetorController import setorController


class UnidadeController:
    def buscarUnidade(self, idUnidade):
        unidade = session.query(Unidade).get(idUnidade)
        return unidade

    def criarUnidade(self, tipoUnidade, idSetor, andar):
        setor = setorController.buscarSetor(idSetor)
        tipo = session.query(TipoLeito).get(tipoUnidade)
        unidade = Unidade(andar, tipo, setor)
        session.add(unidade)
        session.commit()


unidadeController = UnidadeController()
