from datetime import datetime

from Domain.cheltuiala import get_str, get_numar_apartament, get_suma, get_data, get_tip, creeaza_cheltuiala
from Logic.adaugare_valoare import aduna_valoare
from Logic.afisare_sume_lunare import afisare_sume_lunare
from Logic.cea_mai_mare_cheltuiala import cea_mai_mare_cheltuiala
from Logic.crud import adaugare, read, modificare, stergere
from Logic.ordonare_descrescator import ordonare_descrescator
from Logic.stergere import sterge_cu_nr_ap, stergere_cheltuiala
from Logic.undo_redo import do_undo, do_redo


def show_menu():
    print('1. CRUD')
    print('2. Stergere cheltuieli pentru un apartament dat.')
    print('3. Adunarea unei valori la toate cheltuielile dintr-o dată citită.')
    print('4. Ordonarea cheltuielilor descrescator dupa suma.')
    print('5. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.')
    print('6. Sumele lunare pentru fiecare apartament.')
    print('u. Undo.')
    print('r. Redo.')
    print('x. Exit')

def handle_stergere_cheltuieli(cheltuieli, undo_list, redo_list):
    try:
        numar_apartament = int(input('Introduceti numarul apartamentului pentru care se vor sterge cheltuielile:'))
        cheltuieli = stergere_cheltuiala(cheltuieli, numar_apartament, undo_list, redo_list)
        print('Stergerea a fost efectuata cu succes.')
    except ValueError as ve:
        print('Eroare:', ve)

    return cheltuieli



def handle_add(cheltuieli, undo_list, redo_list):
    try:
        id = int(input('Introduceti id-ul cheltuielii: '))
        numar_apartament = int(input('Introduceti numarul apartamentului: '))
        suma = float(input('Introduceti suma cheltuielii: '))
        data = input('Introduceti data cheltuielii: ')
        tipul= input('Introduceti tipul cheltuielii: ')
        return adaugare(cheltuieli, id, numar_apartament, suma, data, tipul, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)
        return cheltuieli




def handle_show_all(cheltuieli):
    for cheltuiala in cheltuieli:
        print(get_str(cheltuiala))


def handle_show_details(cheltuieli):
    id = int(input('Introduceti id-ul cheltuielii pentru care doriti detalii: '))
    cheltuiala = read(cheltuieli, id)
    print(f'Numar apartament: {get_numar_apartament(cheltuiala)}')
    print(f'Suma: {get_suma(cheltuiala)}')
    print(f'Data: {get_data(cheltuiala)}')
    print(f'Tipul: {get_tip(cheltuiala)}')


def handle_modificare(cheltuieli, undo_list, redo_list):
    try:
        id = int(input('Introduceti id-ul cheltuielii care se actualizeaza: '))
        numar_apartament = int(input('Introduceti noul numar de apartament: '))
        suma = float(input('Introduceti noua suma a cheltuielii: '))
        data = input('Introduceti noua data a cheltuielii: ')
        tipul = input('Introduceti noul tip de cheltuiala: ')
        return modificare(cheltuieli, creeaza_cheltuiala(id, numar_apartament, suma, data, tipul), undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)
        return cheltuieli



def handle_stergere(cheltuieli, undo_list, redo_list):
    try:
        id = int(input('Introduceti id-ul cheltuielii care se va sterge: '))
        cheltuieli = stergere(cheltuieli, id, undo_list, redo_list)
        print('Stergerea a fost efectuata cu succes.')
        return cheltuieli
    except ValueError as ve:
        print('Eroare:', ve)
        return cheltuieli


def handle_crud(cheltuieli, undo_list, redo_list):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii cheltuiala')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli = handle_add(cheltuieli, undo_list, redo_list)
        elif optiune == '2':
            cheltuieli = handle_modificare(cheltuieli, undo_list, redo_list)
        elif optiune == '3':
            cheltuieli = handle_stergere(cheltuieli, undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'd':
            handle_show_details(cheltuieli)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return cheltuieli



def handle_adunare_valoare(cheltuieli, undo_list, redo_list):
    try:
        valoarea = float(input('Introduceti valoarea care doriti sa fie adunata tuturor cheltuielilor:'))
        data = input('Introduceti data cheltuielilor la care se va aduna valoarea(de tip"DD.MM.YYYY"):')
        cheltuieli = aduna_valoare(valoarea, data, cheltuieli, undo_list, redo_list)
        print('Adunarea a fost efectuata cu succes.')
    except ValueError as ve:
        print('Eroare:', ve)

    return cheltuieli


def handle_ordonare_descrescator(cheltuieli, undo_list, redo_list):
    lst_cheltuieli = ordonare_descrescator(cheltuieli, undo_list, redo_list)
    print('Ordonarea s-a realizat cu succes! ')
    return lst_cheltuieli


def handle_cea_mai_mare_cheltuiala(cheltuieli):
    result = cea_mai_mare_cheltuiala(cheltuieli)
    for tip in result:
        print(f'Cea mai mare cheltuiala pentru tipul : {tip} este : {get_str(result[tip])}')


def handle_afisare_sume_lunare(cheltuieli):
    result = afisare_sume_lunare(cheltuieli)
    for luna in result:
        for numar_apartament in result[luna]:
            print(f'Sumele lunare din luna  {luna} pentru apartamentul {numar_apartament} sunt: ',  end = '')
            for suma in result[luna][numar_apartament]:
                print(suma, " ", end = '')
            print("")


def handle_undo(cheltuieli, undo_list, redo_list):
    undo_result = do_undo(undo_list, redo_list, cheltuieli)
    if undo_result is not None:
        return undo_result
    return cheltuieli


def handle_redo(cheltuieli, undo_list, redo_list):
    redo_result = do_redo(undo_list, redo_list, cheltuieli)
    if redo_result is not None:
        return redo_result
    return cheltuieli


def run_ui(cheltuieli, undo_list, redo_list):

    while True:
        handle_show_all(cheltuieli)
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli = handle_crud(cheltuieli, undo_list, redo_list)
        elif optiune == '2':
            cheltuieli = handle_stergere_cheltuieli(cheltuieli, undo_list, redo_list)
        elif optiune == '3':
            cheltuieli = handle_adunare_valoare(cheltuieli, undo_list, redo_list)
        elif optiune == '4':
            cheltuieli = handle_ordonare_descrescator(cheltuieli, undo_list, redo_list)
        elif optiune == '5':
            handle_cea_mai_mare_cheltuiala(cheltuieli)
        elif optiune == '6':
            handle_afisare_sume_lunare(cheltuieli)
        elif optiune == 'u':
            cheltuieli = handle_undo(cheltuieli, undo_list, redo_list)
        elif optiune == 'r':
            cheltuieli = handle_redo(cheltuieli, undo_list, redo_list)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return cheltuieli
