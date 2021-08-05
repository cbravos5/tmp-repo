import pathlib
import sys
sys.path.append(f'{pathlib.Path().resolve()}/src/')
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
        return unidade

    def buscarTodasUnidadesSetor(self, idSetor):
        unidades = session.query(Unidade).filter(Unidade.setorId == idSetor).all()
        return unidades

    def printUnidade(self, unidade):
        print("==Unidade==")
        print(f'ID {unidade.id}')
        print(f'Andar {unidade.andar}')
        print(f'Tipo {unidade.tipo.tipo}')
        print(f'ID Setor {unidade.setorId}')

    def printUnidadesSetor(self, idSetor):
        unidades = self.buscarTodasUnidadesSetor(int(idSetor))
        for i in unidades:
            self.printUnidade(i)


unidadeController = UnidadeController()
