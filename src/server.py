from database.repo import *
from app.controllers.AlaController import alaController
from app.controllers.SetorController import setorController

out = False

while not out:
    print('escolha umas das opcoes:')
    print('1 - adicionar ala ', '2 - adicionar setor')
    print('3 - listar alas ', '4 - listar setores')
    print('5 - visualizar ala ', '6 - visualizar setor')
    choice = int(input())
    if(choice == 1):
        nome = input('Digite o nome da ala: ')
        alaController.addAla(nome)
    if(choice == 2):
        nome = input('Digite o nome do setor: ')
        idAla = int(input('Digite o id da ala: '))
        setorController.addSetor(nome, idAla)
    if(choice == 3):
        alas = alaController.index()
        for ala in alas:
            print(f'Nome: {ala.nome}')

    if(choice == 4):
        setores = setorController.index()
        for setor in setores:
            print(f'Nome: {setor.nome} - Ala: {setor.ala.nome}')
    if(choice == 0):
        session.close()
        out = True
