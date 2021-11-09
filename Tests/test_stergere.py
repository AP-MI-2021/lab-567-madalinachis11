from Domain.cheltuiala import  creeaza_cheltuiala
from Logic.stergere import stergere_cheltuiala

from Tests.test_crud import get_data


def test_stergere_cheltuiala():
    lst_cheltuieli = get_data()
    numar_apartament = 4
    assert stergere_cheltuiala(lst_cheltuieli, numar_apartament, [], []) == [
        creeaza_cheltuiala(1, 1, 345, '12.08.2015', 'canal'),
        creeaza_cheltuiala(2, 2, 764, '23.09.2021', 'intretinere'),
        creeaza_cheltuiala(3, 3, 99.99, '25.05.2020', 'alte cheltuieli'),
        creeaza_cheltuiala(5, 5, 425.43, '04.03.2010', 'intretinere')
    ]
    numar_apartament = 6
    lst_cheltuieli = get_data()
    try:
        lst_noua = stergere_cheltuiala(lst_cheltuieli, numar_apartament, [], [])
        assert False
    except ValueError:
        assert True


test_stergere_cheltuiala()
