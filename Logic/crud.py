from Domain.cheltuiala import get_id, creeaza_cheltuiala


def adaugare(lst_cheltuieli, id: int, numar_apartament, suma, data, tipul):
    '''
    Functia adauga in lista de cheltuieli o noua cheltuiala.
    :param lst_cheltuieli: lista de cheltuieli
    :param id: id-ul cheltuielii
    :param numar_apartament:numarul apartamentului cheltuielii adaugate
    :param suma: suma cheltuielii adaugate
    :param data: data cheltuielii adaugate
    :param tipul: tipul cheltuielii adaugate
    :return: o noua lista formata din lst_cheltuieli si noua cheltuiala adaugata.
    '''
    cheltuiala = creeaza_cheltuiala(id, numar_apartament, suma, data, tipul)
    return lst_cheltuieli + [cheltuiala]

def read(lst_cheltuieli, id_apartament_cheltuiala = None):
    '''
    Citeste o anumita cheltuiala din "baza de date".
    :param lst_cheltuieli: lista de cheltuieli
    :param id_apartament_cheltuiala: numarul apartamentului cheltuielii respective.
    :return: cheltuiala apartamentului cu id id_apartament_cheltuiala sau lista cu toate cheltuielile, daca id_apartament_cheltuiala=None.
    '''
    cheltuiala_cu_numar_apartament = None
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) == id_apartament_cheltuiala:
            cheltuiala_cu_numar_apartament = cheltuiala

    if cheltuiala_cu_numar_apartament:
        return cheltuiala_cu_numar_apartament
    return lst_cheltuieli

def modificare(lst_cheltuieli, new_cheltuiala):
    '''
    Actualizeaza o cheltuiala.
    :param lst_cheltuieli: lista de cheltuieli.
    :param new_cheltuiala: cheltuiala care se va actualiza pentru un numar de apartament
    :return: o lista cu cheltuiala actualizata.
    '''

    new_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != get_id(new_cheltuiala):
            new_cheltuieli.append(cheltuiala)
        else:
            new_cheltuieli.append(new_cheltuiala)
    return new_cheltuieli

def stergere(lst_cheltuieli, id):
    '''
    Sterge din lista cheltuiala cu un id.
    :param lst_prajituri: lista de cheltuieli
    :param id: id-ul cheltuielii
    :return: o lista de cheltuieli fara cheltuiala cu id-ul id.
    '''
    new_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != id:
            new_cheltuieli.append(cheltuiala)

    return new_cheltuieli
