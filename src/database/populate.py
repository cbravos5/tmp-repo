import sys
sys.path.append("/home/cbravos/UFPR/DS/src/")
from repo import *
from app.controllers.AlaController import alaController
from app.controllers.SetorController import setorController
from app.controllers.UnidadeController import unidadeController
from app.controllers.FuncionarioController import funcionarioController

# criar alas e setores

# alaAdulto = alaController.criarAla('Adulto')
# alaPediatrico = alaController.criarAla('Pediatrico')
# alaGenObst = alaController.criarAla('Ginecológico/Obstétrico')
# setorCV19Adulto = setorController.criarSetor('Covid-19', alaAdulto.id)
# setorCV19Pediatrico = setorController.criarSetor('Covid-19', alaPediatrico.id)
# setorCV19GenObst = setorController.criarSetor('Covid-19', alaGenObst.id)
# setorNaoCVAdulto = setorController.criarSetor('Não Covid-19', alaAdulto.id)
# setorNaoCVPediatrico = setorController.criarSetor(
#     'Não Covid-19', alaPediatrico.id)
# setorNaoCVGenObst = setorController.criarSetor('Não Covid-19', alaGenObst.id)

# criar tipos

# tipoUTI = TipoLeito('UTI')
# tipoCTSI = TipoLeito('CTSI')
# tipoRegular = TipoLeito('Regular')
# session.add(tipoUTI)
# session.add(tipoCTSI)
# session.add(tipoRegular)

# criar unidades
# unidades UTI em cada setor
# unidadeCV19AdultoUTI = unidadeController.criarUnidade(1, 1, 1)
# unidadeCV19PediatricoUTI = unidadeController.criarUnidade(1, 2, 1)
# unidadeCV19GenObstUTI = unidadeController.criarUnidade(1, 3, 1)
# unidadeNaoCVAdultoUTI = unidadeController.criarUnidade(1, 4, 1)
# unidadeNaoCVPediatricoUTI = unidadeController.criarUnidade(1, 5, 1)
# unidadeNaoCVGenObstUTI = unidadeController.criarUnidade(1, 6, 1)
# # unidades CTSI em cada setor
# unidadeCV19AdultoCTSI = unidadeController.criarUnidade(2, 1, 2)
# unidadeCV19PediatricoCTSI = unidadeController.criarUnidade(2, 2, 2)
# unidadeCV19GenObstCTSI = unidadeController.criarUnidade(2, 3, 2)
# unidadeNaoCVAdultoCTSI = unidadeController.criarUnidade(2, 4, 2)
# unidadeNaoCVPediatricoCTSI = unidadeController.criarUnidade(2, 5, 2)
# unidadeNaoCVGenObstCTSI = unidadeController.criarUnidade(2, 6, 2)
# # unidades Regular em cada setor
# unidadeCV19AdultoRegular = unidadeController.criarUnidade(3, 1, 3)
# unidadeCV19PediatricoRegular = unidadeController.criarUnidade(3, 2, 3)
# unidadeCV19GenObstRegular = unidadeController.criarUnidade(3, 3, 3)
# unidadeNaoCVAdultoRegular = unidadeController.criarUnidade(3, 4, 3)
# unidadeNaoCVPediatricoRegular = unidadeController.criarUnidade(3, 5, 3)
# unidadeNaoCVGenObstRegular = unidadeController.criarUnidade(3, 6, 3)

# criar funcionarios

# funcionarioController.criarFuncionario('Caio','222.254.030-50','(72)97901-4167', 'Médico(a) Adulto')
# funcionarioController.criarFuncionario('Victoria','624.867.350-34','(76)98720-4693', 'Médico(a) Cardiologista')
# funcionarioController.criarFuncionario('Angelo','233.585.270-64','(78)99936-9944', 'Enfermeiro(a)')
# funcionarioController.criarFuncionario('Ethan','157.279.200-77','(56)90021-8249', 'Enfermeiro(a)')
# funcionarioController.criarFuncionario('Jeremias','239.068.100-84','(16)96706-9186','Auxiliar Enf.')
# funcionarioController.criarFuncionario('Vilma','662.693.310-54','(41)99914-3977','Médico(a) Adulto')
# funcionarioController.criarFuncionario('Karen','79.125.270-81','(57)91745-2522','Médico(a) Pediatra')
# funcionarioController.criarFuncionario('Camila','751.402.664-00','(89)91092-4376', 'Enfermeiro(a)')

# criar urgencia

# session.add(Urgencia('Imediata'))
# session.add(Urgencia('Eletiva'))
# session.commit()

session.close()
