from Domain.cheltuiala import get_suma
from Logic.cea_mai_mare_cheltuiala import cea_mai_mare_cheltuiala
from Tests.test_crud import get_data


def test_cea_mai_mare_cheltuiala():
    lst_cheltuieli = get_data()
    result = cea_mai_mare_cheltuiala(lst_cheltuieli)
    assert get_suma(result['alte cheltuieli']) == 99.99
    assert get_suma(result['canal']) == 960
    assert get_suma(result['intretinere']) == 764
    assert len(result) == 3