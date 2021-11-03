from Domain.cheltuiala import get_id, creeaza_cheltuiala, get_numar_apartament, get_data


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
    if read(lst_cheltuieli, id) is not None:
        raise ValueError(f'Exista deja o cheltuiala cu id-ul {id}')
    cheltuiala = creeaza_cheltuiala(id, numar_apartament, suma, data, tipul)
    return lst_cheltuieli + [cheltuiala]

def get_cheltuiala_cu_numar_apartament(lst_cheltuieli, numar_apartament):
    '''
    Arata cheltuiala cu numarul apartamentului dintr-o lista
    :param lst_cheltuieli: lista de cheltuieli
    :param numar_apartament:int, numarul apartamentului luat in discutie
    :return: cheltuiala cu numarul apartamentului din lista sau None in cazul in care aceasta cu exista
    '''
    for cheltuiala in lst_cheltuieli:
        if get_numar_apartament(cheltuiala) == numar_apartament:
            return cheltuiala
    return None

def get_cheltuiala_cu_data(lst_cheltuieli, data):
    '''
    Arata cheltuiala cu data dintr-o lista.
    :param lst_cheltuieli: lista de cheltuieli
    :param data: data luata in discutie
    :return: cheltuiala cu data data din lista sau None, in cazul in care cheltuiala nu exista
    '''
    for cheltuiala in lst_cheltuieli:
        if get_data(cheltuiala) == data:
            return cheltuiala
    return None






def read(lst_cheltuieli, id_apartament_cheltuiala = None):
    '''
    Citeste o anumita cheltuiala din "baza de date".
    :param lst_cheltuieli: lista de cheltuieli
    :param id_apartament_cheltuiala: numarul apartamentului cheltuielii respective.
    :return: -cheltuiala apartamentului cu id id_apartament_cheltuiala
             -lista cu toate cheltuielile, daca id_apartament_cheltuiala=None
             -None, daca nu exista o cheltuiala cu id_apartament_cheltuiala
    '''
    if not id_apartament_cheltuiala:
        return lst_cheltuieli

    cheltuiala_cu_numar_apartament = None
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) == id_apartament_cheltuiala:
            cheltuiala_cu_numar_apartament = cheltuiala

    if cheltuiala_cu_numar_apartament:
        return cheltuiala_cu_numar_apartament
    return None

def modificare(lst_cheltuieli, new_cheltuiala):
    '''
    Actualizeaza o cheltuiala.
    :param lst_cheltuieli: lista de cheltuieli.
    :param new_cheltuiala: cheltuiala care se va actualiza pentru un numar de apartament
    :return: o lista cu cheltuiala actualizata.
    '''
    if read(lst_cheltuieli, get_id(new_cheltuiala)) is None:
        raise ValueError(f'Nu xista o cheltuiala cu id-ul {get_id(new_cheltuiala)} pe care sa o actualizam.')

    new_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != get_id(new_cheltuiala):
            new_cheltuieli.append(cheltuiala)
        else:
            new_cheltuieli.append(new_cheltuiala)
    return new_cheltuieli

def sterge_cu_nr_ap(lst_cheltuieli, numar_apartament):
    '''
    Sterge din lista cheltuiala cu un numar de apartament.
    :param lst_cheltuieli:  lista de cheltuieli
    :param numar_apartament: numarul apartamentului cu cheltuieli
    :return: o lista de cheltuieli fara cheltuiala cu numarul de apartament numar_apartament.
    '''
    new_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_numar_apartament(cheltuiala) != numar_apartament:
            new_cheltuieli.append(cheltuiala)

    return new_cheltuieli


def stergere(lst_cheltuieli, id):
    '''
    Sterge din lista cheltuiala cu un id.
    :param lst_prajituri: lista de cheltuieli
    :param id: id-ul cheltuielii
    :return: o lista de cheltuieli fara cheltuiala cu id-ul id.
    '''
    if read(lst_cheltuieli, id) is None:
        raise ValueError(f'Nu exista o cheltuiala cu id-ul {id} pe care sa o stergem.')
    new_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != id:
            new_cheltuieli.append(cheltuiala)

    return new_cheltuieli

