from Domain import cheltuiala
from Domain.cheltuiala import get_numar_apartament, get_id
from Logic.crud import stergere, get_cheltuiala_cu_numar_apartament, sterge_cu_nr_ap


def stergere_cheltuiala(lst_cheltuieli, numar_apartament, undo_list, redo_list):
    '''
    Sterge toate cheltuielile pentru un apartament dat.
    :param lst_cheltuieli:lista de cheltuieli
    :param numar_apartament: int, apartamentul luat in discutie
    :return:lista de cheltuieli obtinuta in urma stergerii cheltuielilor pentru un apartament dat.
    '''
    if get_cheltuiala_cu_numar_apartament(lst_cheltuieli, numar_apartament) is None:
        raise ValueError('Nu exista cheltuieli pentru apartamentul ales.')
    new_lst_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_numar_apartament(cheltuiala) == numar_apartament:
            new_lst_cheltuieli = sterge_cu_nr_ap(lst_cheltuieli, numar_apartament)
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return new_lst_cheltuieli
