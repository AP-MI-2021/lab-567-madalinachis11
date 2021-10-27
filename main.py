from Logic.crud import adaugare
from Tests.test_crud import test_crud
from UserInterface.console import run_ui


def main():
    cheltuieli = []
    cheltuieli = adaugare(cheltuieli, 1, 1, 11.1, '11.07.2002', 'intretinere')
    cheltuieli = adaugare(cheltuieli, 2, 3, 345, '29.08.2020', 'canal')
    cheltuieli = adaugare(cheltuieli, 3, 5, 635.75, '03.06.2021', 'alte cheltuieli')
    cheltuieli = run_ui(cheltuieli)


if __name__=='__main__':
    test_crud()
    main()