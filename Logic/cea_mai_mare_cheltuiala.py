from Domain.cheltuiala import get_suma, get_tip


def cea_mai_mare_cheltuiala(lst_cheltuieli):
    '''
    Functia returneaza cea mai mare cheltuiala pentru fiecare tip de cheltuiala.
    :param lst_cheltuieli: lista de cheltuieli
    :return: un dictionar in care cheia este tipul
             si valoarea este cheltuiala cu suma maxima
             de acel tip.

    '''
    result = {}
    for cheltuiala in lst_cheltuieli:
        suma = get_suma(cheltuiala)
        tip = get_tip(cheltuiala)
        if tip not in result:
            result[tip] = cheltuiala
        else:
            if suma > get_suma(result[tip]):
                result[tip] = cheltuiala
    return result