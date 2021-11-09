from Domain.cheltuiala import creeaza_cheltuiala
from Logic.adaugare_valoare import aduna_valoare
from Tests.test_crud import get_data


def test_adunare_valoare():
    lst_cheltuieli = get_data()
    valoarea = 10
    data = '12.08.2015'
    assert aduna_valoare(valoarea, data, lst_cheltuieli, [], []) == [
        creeaza_cheltuiala(1, 1, 355, '12.08.2015', 'canal'),
        creeaza_cheltuiala(2, 2, 764, '23.09.2021', 'intretinere'),
        creeaza_cheltuiala(3, 3, 99.99, '25.05.2020', 'alte cheltuieli'),
        creeaza_cheltuiala(4, 4, 960, '24.02.2019', 'canal'),
        creeaza_cheltuiala(5, 5, 425.43, '04.03.2010', 'intretinere')
    ]
    data = '11.07.2002'
    lst_cheltuieli = get_data()
    try:
        lst_noua = aduna_valoare(valoarea, data, lst_cheltuieli, [], [])
        assert False
    except ValueError:
        assert True

test_adunare_valoare()