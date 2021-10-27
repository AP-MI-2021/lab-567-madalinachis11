from Domain.cheltuiala import creeaza_cheltuiala, get_id
from Logic.crud import adaugare, read, modificare, stergere


def get_data():
    return [
        creeaza_cheltuiala(1, 1, 345, '12.08.2015', 'canal'),
        creeaza_cheltuiala(2, 2, 764, '23.09.2021', 'intretinere'),
        creeaza_cheltuiala(3, 3, 99.99, '25.05.2020', 'alte cheltuieli'),
        creeaza_cheltuiala(4, 4, 960, '24.02.2019', 'canal'),
        creeaza_cheltuiala(5, 5, 425.43, '04.03.2010', 'intretinere')
    ]


def test_adaugare():
    cheltuieli = get_data()
    params = (29, 29, 256, '29.08.2020', 'intretinere')
    p_new = creeaza_cheltuiala(*params)
    new_cheltuieli = adaugare(cheltuieli, *params)
    assert len(new_cheltuieli) == len(cheltuieli) + 1

    assert p_new in new_cheltuieli



def test_read():
    cheltuieli = get_data()
    some_p = cheltuieli[2]
    assert read(cheltuieli, get_id(some_p)) == some_p
    assert read(cheltuieli, None) == cheltuieli



def test_modificare():
    cheltuieli = get_data()
    p_updated = creeaza_cheltuiala(5, 5, 234.43, '02.04.2014', 'canal')
    updated = modificare(cheltuieli, p_updated)
    assert p_updated in updated
    assert p_updated not in cheltuieli
    assert len(updated) == len(cheltuieli)



def test_stergere():
    cheltuieli = get_data()
    to_delete = 3
    p_deleted = read(cheltuieli, to_delete)
    deleted = stergere(cheltuieli, to_delete)
    assert p_deleted not in deleted
    assert p_deleted in cheltuieli
    assert len(deleted) == len(cheltuieli) - 1

def test_crud():
    test_adaugare()
    test_read()
    test_modificare()
    test_stergere()