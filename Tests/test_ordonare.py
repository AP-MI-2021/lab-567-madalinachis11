from Domain.cheltuiala import get_suma, get_id, creeaza_cheltuiala
from Logic.ordonare_descrescator import ordonare_descrescator
from Tests.test_crud import get_data


def test_ordonare_descrescator():
    lst_cheltuieli = get_data()
    noua_lista = ordonare_descrescator(lst_cheltuieli, [], [])
    assert get_id(noua_lista[0]) == 4
    assert get_id(noua_lista[1]) == 2
    assert get_id(noua_lista[2]) == 5
    assert get_id(noua_lista[3]) == 1
    assert get_id(noua_lista[4]) == 3
    assert ordonare_descrescator(lst_cheltuieli, [], []) == sorted(lst_cheltuieli, key = get_suma, reverse = True)



