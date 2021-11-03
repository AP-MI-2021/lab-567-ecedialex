from Domain.vanzare import get_str
from Logic.crud import create, delete

def handle_add(vanzari,option):
    try:
        id=int(option[1])
        titlu=option[2]
        gen=option[3]
        pret=int(option[4])
        reducere=option[5]
        return create(vanzari,id,titlu,gen,pret,reducere)
    except ValueError as eroare:
        print('Eroare',eroare)
def handle_delete(vanzari,option):
    try:
        id=int(option[1])
        vanzari=delete(vanzari,id)
        return vanzari
    except ValueError as eroare:
        print('Eroare ',eroare)
def handle_show_all(vanzari,option):
    try:
        if len(option) != 1:
            print('Eroare!')
        else:
            for vanzare in vanzari:
                print(get_str(vanzare))
    except KeyError as error:
        print('Eroare: ',error)
def clc(vanzari):
    while True:
        print('Scrie menu pentru ajutor.')
        option=input()
        if option == 'menu':
            print('Instructiunile sunt despartite prin , ')
            print("Pentru a adauga o vanzare scrie :  Add ,'id' , 'titlu' , 'gen' , 'pret' , 'reducere'.")
            print("Pentru a sterge o vanzare scrie : Delete , 'id'")
            print("Pentru a afisa toate vanzarile scrie : Show_all ")
            print('Back: b')
        else:
            option=option.split(',')
            if option[0] == 'Add':
                vanzari=handle_add(vanzari,option)
            elif option[0] == 'Delete':
                vanzari=handle_delete(vanzari,option)
            elif option[0] == 'Show_all':
                handle_show_all(vanzari,option)
            elif option[0]=='b':
                break
