from Logic.crud import adaugare
from Tests.test_aduna_valoare import test_adunare_valoare
from Tests.test_crud import test_crud
from Tests.test_stergere import test_stergere_cheltuiala
from UserInterface.console import run_ui


def main():
    cheltuieli = []
    cheltuieli = adaugare(cheltuieli, 1, 1, 11.1, '11.07.2002', 'intretinere')
    cheltuieli = adaugare(cheltuieli, 2, 3, 345, '29.08.2020', 'canal')
    cheltuieli = adaugare(cheltuieli, 3, 5, 635.75, '03.06.2021', 'alte cheltuieli')
    cheltuieli = adaugare(cheltuieli, 4, 5, 123.50, '11.07.2002', 'canal')
    cheltuieli = adaugare(cheltuieli, 5, 1, 234, '12.03.2020', 'intretinere')
    cheltuieli = adaugare(cheltuieli, 7, 123, 456, '30.04.2021', 'alte cheltuieli')
    cheltuieli = adaugare(cheltuieli, 8, 12, 355, '23.08.2010', 'canal')
    cheltuieli = adaugare(cheltuieli, 9, 23, 254.65, '31.07.2009', 'alte cheltuieli')
    cheltuieli = adaugare(cheltuieli, 10, 100, 124, '24.02.2019', 'intretinere')
    cheltuieli = adaugare(cheltuieli, 11, 34, 566.99, '14.02.2008', 'canal')
    cheltuieli = run_ui(cheltuieli)


if __name__=='__main__':
    test_crud()
    test_stergere_cheltuiala()
    test_adunare_valoare()
    main()