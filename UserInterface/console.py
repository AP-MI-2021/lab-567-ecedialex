from Domain.vanzare import get_str, creeaza_vanzare
from Logic.crud import create, update, delete
from Logic.discount import aplicare_discount
from Logic.modificare_gen import modificare_gen
from UserInterface.command_line_console import clc


def show_menu():
    print('1.CRUD')
    print('2.Aplicare discount')
    print('3.Modificare gen pentru un titlu dat')
    print('4.Determinare pret minim pentru fiecare gen')
    print('5.Ordonara vanzarilor crescator dupa pret')
    print('6.Afisarea numarului de titluri distincte pentru fiecare gen')
    print('7.Undo')
    print('8.Command_line_console')
    print('x.Exit')

def show_crud_menu():
    print('1.Adaugare')
    print('2.Modificare')
    print('3.Stergere')
    print('a.Afisare')
    print('b.Revenire')

def handle_add(vanzari):
    try:
        id_vanzare = int(input('Dati id-ul vanzarii:'))
    except ValueError as error:
        print('ID-ul introdus nu este un numar valid!',error)
        id_vanzare = int(input('Dati id-ul vanzarii:'))
    titlu = input('Dati titlul cartii din vanzare:')
    gen = input('Dati genul cartii vandute:')
    try:
        pret = float(input('Dati pretul vanzarii:'))
    except ValueError as error:
        print('Pretul introdus nu este valid!',error)
        pret = float(input('Dati pretul vanzarii:'))
    tip_client = input('Dati tipul de client:')
    return create(vanzari,id_vanzare,titlu,gen,pret,tip_client)

def handle_show_all(vanzari):
    for vanzare in vanzari:
        print(get_str(vanzare))

def handle_update(vanzari):
    try:
        id_vanzare = int(input('Dati id-ul vanzarii care se actualizeaza:'))
        titlu = input('Dati noul titlul al cartii din vanzare:')
        gen = input('Dati noul gen al cartii vandute:')
        pret = float(input('Dati noul pret al vanzarii:'))
        tip_client = input('Dati noul tip de client:')
        return update(vanzari,creeaza_vanzare(id_vanzare,titlu,gen,pret,tip_client))
    except ValueError as error:
        print('Eroare!',error)

def handle_delete(vanzari):
    try:
        id_vanzare = int(input('Dati id-ul vanzarii care se va sterge:'))
        vanzari= delete(vanzari,id_vanzare)
        print('Stergerea a fost efectuata cu succes.')
        return vanzari
    except ValueError as error:
        print('Eroare!',error)

def handle_modif_gen(vanzari):
    titlu = input(f"Introduceti titlul cartii pentru care se va schimba genul:")
    new_gen = input(f"Introduceti noul gen al cartii {titlu}:")
    vanzari=modificare_gen(vanzari,titlu,new_gen)
    return vanzari

def handle_crud(vanzari):
    while True:
        show_crud_menu()
        optiune = input('Optiunea aleasa:')
        if optiune == '1':
            vanzari=handle_add(vanzari)
        elif optiune == '2':
            vanzari=handle_update(vanzari)
        elif optiune == '3':
            vanzari= handle_delete(vanzari)
        elif optiune == 'a':
            handle_show_all(vanzari)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')
    return vanzari
def handle_console(vanzari):
    return clc(vanzari)
def run_ui(vanzari):
    while True:
        show_menu()
        opt = input('Optiunea aleasa:')
        if opt == '1':
            vanzari=handle_crud(vanzari)
        elif opt == '2':
            vanzari=aplicare_discount(vanzari)
        elif opt == '3':
            vanzari=handle_modif_gen(vanzari)
        elif opt == '4':
            vanzari = handle_delete(vanzari)
        elif opt == '8':
            vanzari=handle_console(vanzari)
        elif opt == 'x':
            break
        else:
            print('Optiune invalida.')
    return vanzari