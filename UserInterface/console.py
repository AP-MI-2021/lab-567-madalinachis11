from datetime import datetime

from Domain.cheltuiala import get_str, get_numar_apartament, get_suma, get_data, get_tip, creeaza_cheltuiala
from Logic.adaugare_valoare import aduna_valoare
from Logic.crud import adaugare, read, modificare, stergere
from Logic.stergere import sterge_cu_nr_ap


def show_menu():
    print('1. CRUD')
    print('2. Stergere cheltuieli pentru un apartament dat.')
    print('3. Adunarea unei valori la toate cheltuielile dintr-o dată citită.')
    print('x. Exit')

def handle_stergere_cheltuieli(cheltuieli):
    try:
        numar_apartament = int(input('Introduceti numarul apartamentului pentru care se vor sterge cheltuielile:'))
        cheltuieli = sterge_cu_nr_ap(cheltuieli, numar_apartament)
        print('Stergerea a fost efectuata cu succes.')
    except ValueError as ve:
        print('Eroare:', ve)

    return cheltuieli



def handle_add(cheltuieli):
    try:
        id = int(input('Introduceti id-ul cheltuielii: '))
        numar_apartament = int(input('Introduceti numarul apartamentului: '))
        suma = float(input('Introduceti suma cheltuielii: '))
        data = input('Introduceti data cheltuielii: ')
        tipul= input('Introduceti tipul cheltuielii: ')
        return adaugare(cheltuieli, id, numar_apartament, suma, data, tipul)
    except ValueError as ve:
        print('Eroare:', ve)




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


def handle_modificare(cheltuieli):
    try:
        id = int(input('Introduceti id-ul cheltuielii care se actualizeaza: '))
        numar_apartament = int(input('Introduceti noul numar de apartament: '))
        suma = float(input('Introduceti noua suma a cheltuielii: '))
        data = input('Introduceti noua data a cheltuielii: ')
        tipul = input('Introduceti noul tip de cheltuiala: ')
    except ValueError as ve:
        print('Eroare:', ve)
    return modificare(cheltuieli, creeaza_cheltuiala(id, numar_apartament, suma, data, tipul))


def handle_stergere(cheltuieli):
    try:
        id = int(input('Introduceti id-ul cheltuielii care se va sterge: '))
        cheltuieli = stergere(cheltuieli, id)
        print('Stergerea a fost efectuata cu succes.')
    except ValueError as ve:
        print('Eroare:', ve)
    return cheltuieli


def handle_crud(cheltuieli):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii cheltuiala')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli = handle_add(cheltuieli)
        elif optiune == '2':
            cheltuieli = handle_modificare(cheltuieli)
        elif optiune == '3':
            cheltuieli = handle_stergere(cheltuieli)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'd':
            handle_show_details(cheltuieli)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return cheltuieli



def handle_adunare_valoare(cheltuieli):
    try:
        valoarea = float(input('Introduceti valoarea care doriti sa fie adunata tuturor cheltuielilor:'))
        data = input('Introduceti data cheltuielilor la care se va aduna valoarea(de tip"DD.MM.YYYY"):')
        cheltuieli = aduna_valoare(valoarea, data, cheltuieli)
        print('Adunarea a fost efectuata cu succes.')
    except ValueError as ve:
        print('Eroare:', ve)

    return cheltuieli



def run_ui(cheltuieli):

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli = handle_crud(cheltuieli)
        elif optiune == '2':
            cheltuieli = handle_stergere_cheltuieli(cheltuieli)
        elif optiune == '3':
            cheltuieli = handle_adunare_valoare(cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return cheltuieli
