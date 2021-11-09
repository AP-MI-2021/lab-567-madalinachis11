from Domain.cheltuiala import get_suma, get_data, get_numar_apartament


def afisare_sume_lunare(lst_cheltuieli):
    '''
    Determina sumele lunare pentru fiecare apartament.
    :param lst_cheltuieli: lista de cheltuieli
    :return: un dictionar in care cheia este numarul apartamentului
             si valoarea este lista de cheltuieli
             a caror suma se gaseste intr-o anumita luna.
    '''
    result = {}
    for cheltuiala in lst_cheltuieli:
        numar_apartament = get_numar_apartament(cheltuiala)
        data = get_data(cheltuiala)
        luna = int(data.split('.')[1])
        if luna not in result:
            result[luna] = {}
        if numar_apartament not in result[luna]:
            suma = get_suma(cheltuiala)
            result[luna][numar_apartament] = []
            result[luna][numar_apartament].append(suma)
        else:
            suma = get_suma(cheltuiala)
            result[luna][numar_apartament].append(suma)
    return result
