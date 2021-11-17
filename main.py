from Logic.crud import adaugare
from Tests.test_aduna_valoare import test_adunare_valoare
from Tests.test_afisare_sume_lunare import test_afisare_sume_lunare
from Tests.test_cea_mai_mare_cheltuiala import test_cea_mai_mare_cheltuiala
from Tests.test_crud import test_crud
from Tests.test_ordonare import test_ordonare_descrescator
from Tests.test_stergere import test_stergere_cheltuiala
from Tests.test_undo_redo import test_undo_redo, test_adunare_valoare_undo_redo, test_ordonare_descrescator_undo_redo, \
    test_stergere_cheltuiala_undo_redo, test_modificare_undo_redo, test_stergere_undo_redo
from UserInterface.command_line_console import command_console
from UserInterface.console import run_ui, handle_crud


def main():
    cheltuieli = []
    undo_list =[]
    redo_list = []
    cheltuieli = adaugare(cheltuieli, 1, 1, 11.1, '11.07.2002', 'intretinere', undo_list, redo_list)
    cheltuieli = adaugare(cheltuieli, 2, 3, 345, '29.08.2020', 'canal', undo_list, redo_list)
    cheltuieli = adaugare(cheltuieli, 3, 5, 635.75, '03.06.2021', 'alte cheltuieli', undo_list, redo_list)
    cheltuieli = adaugare(cheltuieli, 4, 5, 123.50, '11.07.2002', 'canal', undo_list, redo_list)
    cheltuieli = adaugare(cheltuieli, 5, 1, 234, '12.03.2020', 'intretinere', undo_list, redo_list)
    cheltuieli = adaugare(cheltuieli, 7, 123, 456, '30.04.2021', 'alte cheltuieli', undo_list, redo_list)
    cheltuieli = adaugare(cheltuieli, 8, 12, 355, '23.08.2010', 'canal', undo_list, redo_list)
    cheltuieli = adaugare(cheltuieli, 9, 23, 254.65, '31.07.2009', 'alte cheltuieli', undo_list, redo_list)
    cheltuieli = adaugare(cheltuieli, 10, 100, 124, '24.02.2019', 'intretinere', undo_list, redo_list)
    cheltuieli = adaugare(cheltuieli, 11, 34, 566.99, '14.02.2008', 'canal', undo_list, redo_list)
    print("1. Meniu Vechi")
    print("2. Meniu Nou")
    user_input = input("alegeti meniul dorit: ")
    if user_input == '1':
        cheltuieli = run_ui(cheltuieli, undo_list, redo_list)
    elif user_input == '2':
        command_console()
    else:
        print("Optiune invalida!")
        main()


if __name__=='__main__':
    test_crud()
    test_stergere_cheltuiala()
    test_adunare_valoare()
    test_cea_mai_mare_cheltuiala()
    test_ordonare_descrescator()
    test_afisare_sume_lunare()
    test_undo_redo()
    test_adunare_valoare_undo_redo()
    test_stergere_cheltuiala_undo_redo()
    test_modificare_undo_redo()
    test_stergere_undo_redo()
    test_ordonare_descrescator_undo_redo()
    main()