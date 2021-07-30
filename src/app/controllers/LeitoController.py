from database.repo import *
import app.controllers.UnidadeController as UnidadeController


class LeitoController:

    def buscarLeito(self, idLeito):
        leito = session.query(Leito).get(idLeito)
        return leito

    def setTipoLeito(self, leito, tipo):
        leito.tipo = tipo

    def consultarLeitos(self, idUnidade):
        unidade = UnidadeController.unidadeController.buscarUnidade(idUnidade)
        arrLeitos = session.query(Leito).filter(Leito.unidade == unidade).all()
        return arrLeitos

    def criarLeitos(self, tipoLeito, qtdLeito, idUnidade):
        unidade = UnidadeController.unidadeController.buscarUnidade(idUnidade)
        tipo = session.query(TipoLeito).get(tipoLeito)

        for i in range(qtdLeito):
            novoLeito = Leito(tipo, unidade)
            session.add(novoLeito)

        session.commit()

    def setDisponibilidade(self, leito, disponibilidade):
        leito.disponibilidade = disponibilidade

    def modificarLeitos(self, tipoLeito, listaLeitos, idUnidade):
        unidade = UnidadeController.unidadeController.buscarUnidade(idUnidade)
        tipo = session.query(TipoLeito).get(tipoLeito)
        # olha se tem que mudar tipo
        mudaTipo = True if (listaLeitos[0].tipo != tipo) else False
        for leito in listaLeitos:
            if(mudaTipo):
                self.setTipoLeito(leito, tipo)
            leito.unidade = unidade
        session.commit()


leitoController = LeitoController()
