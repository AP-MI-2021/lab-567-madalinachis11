def creeaza_cheltuiala(id: int, numar_apartament, suma, data, tipul):
    '''
    Creeaza o cheltuiala descrisa de numarul apartamentului, suma, data( de tip 'DD.MM.YYYY') si tipul caracterizat de intretinere, canal sau alte cheltuieli.
    :param numar_apartament:numarul apartamentului caruia ii corespunde cheltuiala
    :param suma:suma cheltuielii
    :param data:data la care s-a emis cheltuiala
    :param tipul:tipul cheltuielii(intretinere, canal, alte cheltuieli)
    :return: o cheltuiala
    '''
    return{
        'id': id,
        'numar': numar_apartament,
        'suma': suma,
        'data': data,
        'tip': tipul,
    }

def get_id(cheltuiala):
    '''
    Getter pentru id-ul cheltuielii.
    :param cheltuiala: cheltuiala
    :return: id-ul cheltuielii date ca parametru.
    '''
    return cheltuiala['id']

def get_numar_apartament(cheltuiala):
    '''
    Getter pentru numarul apartamentului.
    :param cheltuiala: cheltuiala
    :return: numarul apartamentului a carui cheltuiala este data ca parametru.
    '''
    return cheltuiala['numar']

def get_suma(cheltuiala):
    '''
    Getter pentru suma cheltuielii.
    :param cheltuiala: cheltuiala
    :return: suma cheltuielii date ca parametru.
    '''
    return cheltuiala['suma']

def get_data(cheltuiala):
    '''
    Getter pentru data cheltuielii.
    :param cheltuiala: cheltuiala
    :return: data emiterii cheltuielii date ca parametru.
    '''
    return cheltuiala['data']

def get_tip(cheltuiala):
    '''
    Getter pentru tipul cheltuielii.
    :param cheltuiala: cheltuiala
    :return: tipul cheltuielii date ca parametru.
    '''
    return cheltuiala['tip']

def get_str(cheltuiala):
    return f'Cheltuiala cu id-ul: {get_id(cheltuiala)}, a numarului de apartament: {get_numar_apartament(cheltuiala)}, avand suma de: {get_suma(cheltuiala)} lei, din data de: {get_data(cheltuiala)}, de tipul: {get_tip(cheltuiala)}'



