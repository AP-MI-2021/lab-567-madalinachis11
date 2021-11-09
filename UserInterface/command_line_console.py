from Domain.cheltuiala import get_str
from Logic.crud import adaugare, stergere
from Logic.undo_redo import do_undo, do_redo


def command_menu():
    print('Prin functia "add" puteti adauga cheltuieli noi in lista de cheltuieli, in urma completarii tuturor campurilor necesare: id, numar apartament, suma, data, tip.')
    print('Prin functia "showall" puteti afisa toate cheltuielile din lista de cheltuieli.')
    print('Prin functia "delete" puteti sterge o cheltuiala prin introducerea unui id care doriti sa corespunda cheltuielii care urmeaza sa fie stearsa.')
    print('Comenzile trebuie sa fie apelate pe o singura linie si separate prin ";" iar parametrii prin ",".')
    print('Daca doriti sa va opriti tastati "stop')
    print('')


def command_console():
    """
    command params
    add id, nr_apartament, suma, data, tip
    comanda = add
    parametri = id, nr_apartame, suma, data, tip
    add pram; showall; delete pram;
    :return:
    """
    lst_cheltuieli = lista_initiala()
    undo_list =[]
    redo_list = []
    while True:
        user_input = input('Introduceti comanda: ')
        lista_comenzi = user_input.split("; ")
        for comanda in lista_comenzi:
            try:
                comanda_word, parametri = split_command(comanda)
                if comanda_word == 'add':
                    lst_cheltuieli = add_command(lst_cheltuieli, parametri, undo_list, redo_list)
                elif comanda_word == 'showall':
                    handle_show_all(lst_cheltuieli)
                elif comanda_word == 'delete':
                    lst_cheltuieli = delete_command(lst_cheltuieli, parametri, undo_list, redo_list)
                elif comanda_word == 'undo':
                    lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
                elif comanda_word == 'redo':
                    lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
                elif comanda_word == 'help':
                    command_menu()
                elif comanda_word == 'stop':
                    exit()
            except ValueError as ve:
                print('eroare:', ve)


def split_command(command):
    """
    this splits the command string in a command word and parameters
    :param command: the user input
    :return:
    """
    aux = command.split(" ", maxsplit=1)
    command_word = aux[0]
    command_param = aux[1] if len(aux) == 2 else None
    return command_word, command_param


def add_command(lst_cheltuieli, parametri, undo_list, redo_list):
    if parametri == None:
        raise ValueError("Parametrii incorecti")
    id, numar_apartament, suma, data, tipul = parametri.split(", ")
    return adaugare(lst_cheltuieli, int(id), int(numar_apartament), float(suma), data, tipul, undo_list, redo_list)

def delete_command(lst_cheltuieli, id, undo_list, redo_list):
    return stergere(lst_cheltuieli, int(id), undo_list, redo_list)


def handle_show_all(cheltuieli):
    for cheltuiala in cheltuieli:
        print(get_str(cheltuiala))

def lista_initiala():
    cheltuieli = []
    cheltuieli = adaugare(cheltuieli, 1, 1, 11.1, '11.07.2002', 'intretinere', [], [])
    cheltuieli = adaugare(cheltuieli, 2, 3, 345, '29.08.2020', 'canal', [], [])
    cheltuieli = adaugare(cheltuieli, 3, 5, 635.75, '03.06.2021', 'alte cheltuieli', [], [])
    cheltuieli = adaugare(cheltuieli, 4, 5, 123.50, '11.07.2002', 'canal', [], [])
    cheltuieli = adaugare(cheltuieli, 5, 1, 234, '12.03.2020', 'intretinere', [], [])
    cheltuieli = adaugare(cheltuieli, 7, 123, 456, '30.04.2021', 'alte cheltuieli', [], [])
    cheltuieli = adaugare(cheltuieli, 8, 12, 355, '23.08.2010', 'canal', [], [])
    cheltuieli = adaugare(cheltuieli, 9, 23, 254.65, '31.07.2009', 'alte cheltuieli', [], [])
    cheltuieli = adaugare(cheltuieli, 10, 100, 124, '24.02.2019', 'intretinere', [], [])
    cheltuieli = adaugare(cheltuieli, 11, 34, 566.99, '14.02.2008', 'canal', [], [])
    return cheltuieli

