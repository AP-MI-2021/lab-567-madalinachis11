from Domain.cheltuiala import get_data, creeaza_cheltuiala, get_id, get_numar_apartament, get_suma, get_tip
from Logic.crud import get_cheltuiala_cu_data


def aduna_valoare(valoarea, data, lst_cheltuieli, undo_list, redo_list):
    '''
    Aduna o valoare la toate cheltuielile dintr-o dată citită.
    :param valoarea: valoarea care urmeaza sa fie adaugata, de tip float
    :param data: fata luata in discutie
    :param lst_cheltuieli: lista de cheltuieli
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :return: Lista de cheltuieli la care s-a adaugat o valoare la toate cheltuielile din data introdusa.
    '''
    if get_cheltuiala_cu_data(lst_cheltuieli, data) is None:
        raise ValueError("Nu exista o cheltuiala cu data introdusa.")
    result = []
    for cheltuiala in lst_cheltuieli:
        if get_data(cheltuiala) == data:
            suma_noua = get_suma(cheltuiala) + valoarea
            result.append(creeaza_cheltuiala(
                get_id(cheltuiala),
                get_numar_apartament(cheltuiala),
                suma_noua,
                get_data(cheltuiala),
                get_tip(cheltuiala),
            ))
        else:
            result.append(cheltuiala)
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return result
