from Domain.cheltuiala import get_suma, get_id, creeaza_cheltuiala
from Logic.adaugare_valoare import aduna_valoare
from Logic.crud import adaugare, get_cheltuiala_cu_id, get_cheltuiala_cu_numar_apartament, modificare, stergere
from Logic.ordonare_descrescator import ordonare_descrescator
from Logic.stergere import stergere_cheltuiala
from Logic.undo_redo import do_undo, do_redo
from Tests.test_crud import get_data

def test_undo_redo():
    undo_list = []
    redo_list = []
    current_list = []
    #1 lista initiala goala
    assert len(current_list) == 0
    #2 adaugam un obiect
    current_list = adaugare(current_list, 1, 1, 200, 'data1', 'intretinere', undo_list, redo_list)
    #3 adaugam inca un obiect
    current_list = adaugare(current_list, 2, 2, 200, 'data2', 'canal', undo_list, redo_list)
    #4 adaugam inca un obiect
    current_list = adaugare(current_list, 3, 3, 200, 'data3', 'alte cheltuieli', undo_list, redo_list)
    assert len(current_list) == 3
    #5 undo scoate ultimul obiect adaugat
    if len(undo_list) > 0:
        current_list = do_undo(undo_list, redo_list, current_list)
    assert len(current_list) == 2
    assert get_cheltuiala_cu_id(current_list, 1) is not None
    assert get_cheltuiala_cu_id(current_list, 2) is not None
    assert get_cheltuiala_cu_id(current_list, 3) is None
    #6 inca un undo scoate penultimul obiect adaugat
    if len(undo_list) > 0:
        current_list = do_undo(undo_list, redo_list, current_list)
    assert len(current_list) == 1
    assert get_cheltuiala_cu_id(current_list, 1) is not None
    assert get_cheltuiala_cu_id(current_list, 2) is None
    assert get_cheltuiala_cu_id(current_list, 3) is None
    #7 inca un undo scoate si si primul element adaugat
    if len(undo_list) > 0:
        current_list = do_undo(undo_list, redo_list, current_list)
    assert len(current_list) == 0
    assert get_cheltuiala_cu_id(current_list, 1) is None
    assert get_cheltuiala_cu_id(current_list, 2) is None
    assert get_cheltuiala_cu_id(current_list, 3) is None
    #8 inca un undo si nu face nimic
    if len(undo_list) > 0:
        current_list = do_undo(undo_list, redo_list, current_list)
    assert get_cheltuiala_cu_id(current_list, 1) is None
    assert get_cheltuiala_cu_id(current_list, 2) is None
    assert get_cheltuiala_cu_id(current_list, 3) is None

    #9 adaugam trei obiecte
    current_list = adaugare(current_list, 1, 25, 200, 'data1', 'intretinere', undo_list, redo_list)
    current_list = adaugare(current_list, 2, 25, 200, 'data2', 'canal', undo_list, redo_list)
    current_list = adaugare(current_list, 3, 25, 200, 'data3', 'alte cheltuieli', undo_list, redo_list)
    assert len(current_list) == 3
    assert get_cheltuiala_cu_id(current_list, 1) is not None
    assert get_cheltuiala_cu_id(current_list, 2) is not None
    assert get_cheltuiala_cu_id(current_list, 3) is not None
    #10 redo nu face nimic
    if len(redo_list) > 0:
        current_list = do_redo(undo_list, redo_list, current_list)
    assert len(current_list) == 3
    assert get_cheltuiala_cu_id(current_list, 1) is not None
    assert get_cheltuiala_cu_id(current_list, 2) is not None
    assert get_cheltuiala_cu_id(current_list, 3) is not None
    #11 doua undo-uri scot ultimele 2 obiecte
    if len(undo_list) > 0:
        current_list = do_undo(undo_list, redo_list, current_list)
    if len(undo_list) > 0:
        current_list = do_undo(undo_list, redo_list, current_list)
    assert len(current_list) == 1
    assert get_cheltuiala_cu_id(current_list, 1) is not None
    assert get_cheltuiala_cu_id(current_list, 2) is None
    assert get_cheltuiala_cu_id(current_list, 3) is None
    #12 redo anuleaza ultimul undo, daca operatia e undo
    if len(redo_list)>0:
        current_list = do_redo(undo_list, redo_list, current_list)
    assert len(current_list) == 2
    assert get_cheltuiala_cu_id(current_list, 1) is not None
    assert get_cheltuiala_cu_id(current_list, 2) is not None
    assert get_cheltuiala_cu_id(current_list, 3) is None
    #13 redo anuleaza si primul undo
    if len(redo_list) > 0:
        current_list = do_redo(undo_list, redo_list, current_list)
    assert len(current_list) == 3
    assert get_cheltuiala_cu_id(current_list, 1) is not None
    assert get_cheltuiala_cu_id(current_list, 2) is not None
    assert get_cheltuiala_cu_id(current_list, 3) is not None
    #14 doua undo-uri scot ultimele 2 obiecte
    if len(undo_list) > 0:
        current_list = do_undo(undo_list, redo_list, current_list)
    if len(undo_list) > 0:
        current_list = do_undo(undo_list, redo_list, current_list)
    assert len(current_list) == 1
    assert get_cheltuiala_cu_id(current_list, 1) is not None
    assert get_cheltuiala_cu_id(current_list, 2) is None
    assert get_cheltuiala_cu_id(current_list, 3) is None
    #15 adaugam un obiect
    current_list = adaugare(current_list, 4, 25, 200, 'data4', 'intretinere', undo_list, redo_list)
    assert len(current_list) == 2
    assert get_cheltuiala_cu_id(current_list, 1) is not None
    assert get_cheltuiala_cu_id(current_list, 2) is None
    assert get_cheltuiala_cu_id(current_list, 3) is None
    assert get_cheltuiala_cu_id(current_list, 4) is not None
    #16 redo nu face nimic, deoarece ultima operatie nu este un undo
    if len(redo_list) > 0:
        current_list = do_redo(undo_list, redo_list, current_list)
    assert len(current_list) == 2
    assert get_cheltuiala_cu_id(current_list, 1) is not None
    assert get_cheltuiala_cu_id(current_list, 2) is None
    assert get_cheltuiala_cu_id(current_list, 3) is None
    assert get_cheltuiala_cu_id(current_list, 4) is not None
    #17 undo anuleaza adaugarea obiectului cu id-ul 4
    if len(undo_list) > 0:
        current_list = do_undo(undo_list, redo_list, current_list)
    assert len(current_list) == 1
    assert get_cheltuiala_cu_id(current_list, 1) is not None
    assert get_cheltuiala_cu_id(current_list, 2) is None
    assert get_cheltuiala_cu_id(current_list, 3) is None
    assert get_cheltuiala_cu_id(current_list, 4) is None
    #18 undo anuleaza adaugarea obiectului cu id-ul 1
    if len(redo_list) > 0:
        current_list = do_undo(undo_list, redo_list, current_list)
    assert len(current_list) == 0
    assert get_cheltuiala_cu_id(current_list, 1) is None
    assert get_cheltuiala_cu_id(current_list, 2) is None
    assert get_cheltuiala_cu_id(current_list, 3) is None
    assert get_cheltuiala_cu_id(current_list, 4) is None
    #19 se anuleaza ultimele doua undo-uri
    if len(redo_list) > 0:
        current_list = do_redo(undo_list, redo_list, current_list)
    if len(redo_list) > 0:
        current_list = do_redo(undo_list, redo_list, current_list)
    assert len(current_list) == 2
    assert get_cheltuiala_cu_id(current_list, 1) is not None
    assert get_cheltuiala_cu_id(current_list, 2) is None
    assert get_cheltuiala_cu_id(current_list, 3) is None
    assert get_cheltuiala_cu_id(current_list, 4) is not None
    #20 redo nu face nimic
    if len(redo_list) > 0:
        current_list = do_redo(undo_list, redo_list, current_list)
    assert len(current_list) == 2
    assert get_cheltuiala_cu_id(current_list, 1) is not None
    assert get_cheltuiala_cu_id(current_list, 2) is None
    assert get_cheltuiala_cu_id(current_list, 3) is None
    assert get_cheltuiala_cu_id(current_list, 4) is not None

def test_stergere_cheltuiala_undo_redo():
    undo_list = []
    redo_list = []
    current_list = []
    current_list = adaugare(current_list, 9, 1, 200, 'data1', 'intretinere', undo_list, redo_list)
    current_list = adaugare(current_list, 10, 2, 500.2, 'data2', 'canal', undo_list, redo_list)
    current_list = adaugare(current_list, 100, 3, 123, 'data3', 'alte cheltuieli', undo_list, redo_list)
    current_list = adaugare(current_list, 12, 10, 999, 'data4', 'canal', undo_list, redo_list)

    numar_apartament = 1
    current_list = stergere_cheltuiala(current_list, numar_apartament, undo_list, redo_list)
    assert len(current_list) == 3
    assert get_cheltuiala_cu_numar_apartament(current_list, 1) is None
    assert get_cheltuiala_cu_numar_apartament(current_list, 2) is not None
    assert get_cheltuiala_cu_numar_apartament(current_list, 3) is not None
    assert get_cheltuiala_cu_numar_apartament(current_list, 10) is not None

    if len(undo_list) > 0:
        current_list = do_undo(undo_list, redo_list, current_list)

    assert len(current_list) == 4
    assert get_cheltuiala_cu_numar_apartament(current_list, 1) is not None
    assert get_cheltuiala_cu_numar_apartament(current_list, 2) is not None
    assert get_cheltuiala_cu_numar_apartament(current_list, 3) is not None
    assert get_cheltuiala_cu_numar_apartament(current_list, 10) is not None

    if len(redo_list) > 0:
        current_list = do_redo(undo_list, redo_list, current_list)
    assert len(current_list) == 3
    assert get_cheltuiala_cu_numar_apartament(current_list, 1) is None
    assert get_cheltuiala_cu_numar_apartament(current_list, 2) is not None
    assert get_cheltuiala_cu_numar_apartament(current_list, 3) is not None
    assert get_cheltuiala_cu_numar_apartament(current_list, 10) is not None


def test_adunare_valoare_undo_redo():
    undo_list = []
    redo_list = []
    current_list = []
    current_list = adaugare(current_list, 9, 1, 200, '11.07.2002', 'intretinere', undo_list, redo_list)
    current_list = adaugare(current_list, 10, 2, 500.2, '14.12.2000', 'canal', undo_list, redo_list)
    current_list = adaugare(current_list, 100, 3, 123, '12.12.2012', 'alte cheltuieli', undo_list, redo_list)
    current_list = adaugare(current_list, 12, 10, 999, '11.07.2002', 'canal', undo_list, redo_list)

    valoarea = 10
    data = '11.07.2002'
    current_list = aduna_valoare(valoarea, data, current_list, undo_list, redo_list)

    assert get_suma(get_cheltuiala_cu_id(current_list, 9)) == 210
    assert get_suma(get_cheltuiala_cu_id(current_list, 10)) == 500.2
    assert get_suma(get_cheltuiala_cu_id(current_list, 100)) == 123
    assert get_suma(get_cheltuiala_cu_id(current_list, 12)) == 1009

    current_list = do_undo(undo_list, redo_list, current_list)
    assert get_suma(get_cheltuiala_cu_id(current_list, 9)) == 200
    assert get_suma(get_cheltuiala_cu_id(current_list, 10)) == 500.2
    assert get_suma(get_cheltuiala_cu_id(current_list, 100)) == 123
    assert get_suma(get_cheltuiala_cu_id(current_list, 12)) == 999

    current_list = do_redo(undo_list, redo_list, current_list)
    assert get_suma(get_cheltuiala_cu_id(current_list, 9)) == 210
    assert get_suma(get_cheltuiala_cu_id(current_list, 10)) == 500.2
    assert get_suma(get_cheltuiala_cu_id(current_list, 100)) == 123
    assert get_suma(get_cheltuiala_cu_id(current_list, 12)) == 1009



def test_ordonare_descrescator_undo_redo():
    undo_list = []
    redo_list = []
    current_list = []
    current_list = adaugare(current_list, 1, 25, 200, 'data1', 'intretinere', undo_list, redo_list)
    current_list = adaugare(current_list, 2, 25, 300, 'data2', 'canal', undo_list, redo_list)
    current_list = adaugare(current_list, 3, 25, 400, 'data3', 'alte cheltuieli', undo_list, redo_list)
    current_list = ordonare_descrescator(current_list, undo_list, redo_list)
    assert get_id(current_list[0]) == 3
    assert get_id(current_list[1]) == 2
    assert get_id(current_list[2]) == 1
    current_list = do_undo(undo_list, redo_list, current_list)
    assert get_id(current_list[0]) == 1
    assert get_id(current_list[1]) == 2
    assert get_id(current_list[2]) == 3
    current_list = do_redo(undo_list, redo_list, current_list)
    assert get_id(current_list[0]) == 3
    assert get_id(current_list[1]) == 2
    assert get_id(current_list[2]) == 1




def test_modificare_undo_redo():
    current_list = []
    undo_list = []
    redo_list = []

    current_list = adaugare(current_list, 9, 1, 200, '11.07.2002', 'intretinere', undo_list, redo_list)
    current_list = adaugare(current_list, 10, 2, 500.2, '14.12.2000', 'canal', undo_list, redo_list)
    current_list = adaugare(current_list, 100, 3, 123, '12.12.2012', 'alte cheltuieli', undo_list, redo_list)
    current_list = adaugare(current_list, 12, 10, 999, '11.07.2002', 'canal', undo_list, redo_list)
    c_updated = creeaza_cheltuiala(9, 23, 546, '25.12.2015', 'intretinere')

    updated = modificare(current_list, c_updated, undo_list, redo_list)
    if len(undo_list) > 0:
        updated = do_undo(undo_list, redo_list, updated)
    assert c_updated not in updated
    if len(redo_list) > 0:
        updated = do_redo(undo_list, redo_list, updated)
    assert c_updated in updated


def test_stergere_undo_redo():
    current_list = []
    undo_list = []
    redo_list = []

    current_list = adaugare(current_list, 9, 1, 200, '11.07.2002', 'intretinere', undo_list, redo_list)
    current_list = adaugare(current_list, 10, 2, 500.2, '14.12.2000', 'canal', undo_list, redo_list)
    current_list = adaugare(current_list, 100, 3, 123, '12.12.2012', 'alte cheltuieli', undo_list, redo_list)
    current_list = adaugare(current_list, 12, 10, 999, '11.07.2002', 'canal', undo_list, redo_list)

    stergere_cheltuiala = 9

    c_stearsa = get_cheltuiala_cu_id(current_list, stergere_cheltuiala)
    sters = stergere(current_list, stergere_cheltuiala, undo_list, redo_list)
    if len(undo_list) > 0:
        sters = do_undo(undo_list, redo_list, sters)
    assert c_stearsa in sters
    if len(redo_list) > 0:
        sters = do_redo(undo_list, redo_list, sters)
    assert c_stearsa not in sters



def test_adaugare_undo_redo():
    current_list = []
    undo_list = []
    redo_list = []
    current_list = adaugare(current_list, 9, 1, 200, '11.07.2002', 'intretinere', undo_list, redo_list)
    current_list = adaugare(current_list, 10, 2, 500.2, '14.12.2000', 'canal', undo_list, redo_list)
    current_list = adaugare(current_list, 100, 3, 123, '12.12.2012', 'alte cheltuieli', undo_list, redo_list)
    current_list = adaugare(current_list, 12, 10, 999, '11.07.2002', 'canal', undo_list, redo_list)

    cheltuiala_n = creeaza_cheltuiala(9, 1, 200, '11.07.2002', 'intretinere')
    assert cheltuiala_n in current_list
    current_list = do_undo(undo_list, redo_list, current_list)
    assert cheltuiala_n not in current_list
    current_list = do_redo(undo_list, redo_list, current_list)
    assert cheltuiala_n in current_list






