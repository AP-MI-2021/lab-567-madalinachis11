
def do_undo(undo_list: list, redo_list: list, current_list: list):
    """
    :param undo_list:
    :param redo_list:
    :return:
    """
    if undo_list:
        redo_list.append(current_list)
        return undo_list.pop()

    return current_list


def do_redo(undo_list: list, redo_list: list, current_list: list):
    """
    :param undo_list:
    :param redo_list:
    :return:
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo

    return current_list


