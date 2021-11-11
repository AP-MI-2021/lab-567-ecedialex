from Domain.vanzare import get_str, get_id
from Logic.crud import create, delete
def print_menu():
    print('Instructiunile sunt separate prin: [;] iar termenii prin: [,]')
    print("Pentru a adauga o vanzare scrie: 'add','id','titlu','gen','pret','reducere'.")
    print("Pentru a sterge o vanzare scrie: 'del','id'")
    print("Pentru a afisa toate vanzarile scrie: 'sa'")
    print("Pentru a inchide programul scrie: 'x'")

def handle_add(vanzari,option,undo_list,redo_list):
    try:
        print(option)
        id=int(option[1])
        titlu=option[2]
        gen=option[3]
        pret=float(option[4])
        reducere=option[5]
        return create(vanzari,id,titlu,gen,pret,reducere,undo_list,redo_list)
    except ValueError as eroare:
        print('Eroare: ',eroare)

def handle_delete(vanzari,option,undo_list,redo_list):
    try:
            id=int(option[1])
            vanzari=delete(vanzari,id,undo_list,redo_list)
            return vanzari
    except ValueError as eroare:
        print('Eroare: ',eroare)
def handle_show_all(vanzari):
    for vanzare in vanzari:
        print(get_str(vanzare))
def clc(vanzari):

        while True:
            print_menu()
            lista=input()
            undo_list=[]
            redo_list=[]
            comenzi=lista.split(';')
            for comanda in comenzi:
                param=comanda.split(',')
                if param[0] == 'sa' and len(param) == 1:
                    handle_show_all(vanzari)
                elif param[0] == 'del' and len(param) == 2:
                    vanzari = handle_delete(vanzari,param,undo_list,redo_list)
                elif param[0] == 'x' and len(param) == 1:
                    return 0,print("Program inchis")
                elif param[0] == 'add' and len(param) == 6:
                    vanzari = handle_add(vanzari,param,undo_list,redo_list)
                else:
                    print("Optiune invalida.")