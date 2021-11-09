from Domain.cheltuiala import get_suma


def ordonare_descrescator(lst_cheltuieli, undo_list, redo_list):
    '''
    Functia returneaza o lista de cheltuieli ordonata descrescator dupa sumele lor.
    :param lst_cheltuieli: lista de cheltuieli
    :return: lista ordonata descrescator
    '''
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return sorted(lst_cheltuieli, key = get_suma, reverse = True)