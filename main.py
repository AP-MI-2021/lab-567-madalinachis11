from Logic.crud import adaugare
from Tests.test_crud import test_crud
from UserInterface.console import run_ui


def main():
    cheltuieli = []
    cheltuieli = adaugare(cheltuieli, 1, 1, 11.1, '11.07.2002', 'intretinere')
    cheltuieli = run_ui(cheltuieli)


if __name__=='__main__':
    test_crud()
    main()