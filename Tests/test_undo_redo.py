from Logic.crud import adaugare
from Logic.undo_redo import do_undo, do_redo
from Tests.test_crud import get_data

def test_undo_redo():
    undo_list = []
    redo_list = []
    current_list = []
    """
        Primele adaugari
    """
    current_list = adaugare(current_list, 1, 25, 200, '26.07.2002', 'intretinere', undo_list, redo_list)
    current_list = adaugare(current_list, 2, 25, 200, '26.07.2002', 'intretinere', undo_list, redo_list)
    current_list = adaugare(current_list, 3, 25, 200, '26.07.2002', 'intretinere', undo_list, redo_list)
    current_list = do_undo(undo_list, redo_list, current_list)
    assert current_list == [[1, 25, 200, '26.07.2002', 'intretinere'], [2, 25, 200, '26.07.2002', 'intretinere']]
    current_list = do_undo(undo_list, redo_list, current_list)
    assert current_list == [[1, 25, 200, '26.07.2002', 'intretinere']]
    current_list = do_undo(undo_list, redo_list, current_list)
    assert current_list == []
    current_list = do_undo(undo_list, redo_list, current_list)
    assert current_list == []

    """
        A Doua adaugare
    """
    current_list = adaugare(current_list, 1, 25, 200, '26.07.2002', 'intretinere', undo_list, redo_list)
    current_list = adaugare(current_list, 2, 25, 200, '26.07.2002', 'intretinere', undo_list, redo_list)
    current_list = adaugare(current_list, 3, 25, 200, '26.07.2002', 'intretinere', undo_list, redo_list)
    current_list = do_redo(undo_list, redo_list, current_list)
    assert current_list == [[1, 25, 200, '26.07.2002', 'intretinere'],
                            [2, 25, 200, '26.07.2002', 'intretinere'],
                            [3, 25, 200, '26.07.2002', 'intretinere']]
    current_list = do_undo(undo_list, redo_list, current_list)
    current_list = do_undo(undo_list, redo_list, current_list)
    assert current_list == [[1, 25, 200, '26.07.2002', 'intretinere']]
    current_list = do_redo(undo_list, redo_list, current_list)
    assert current_list == [[1, 25, 200, '26.07.2002', 'intretinere'], [2, 25, 200, '26.07.2002', 'intretinere']]
    current_list = do_redo(undo_list, redo_list, current_list)
    assert current_list == [[1, 25, 200, '26.07.2002', 'intretinere'],
                            [2, 25, 200, '26.07.2002', 'intretinere'],
                            [3, 25, 200, '26.07.2002', 'intretinere']]
    current_list = do_undo(undo_list, redo_list, current_list)
    current_list = do_undo(undo_list, redo_list, current_list)
    assert current_list == [[1, 25, 200, '26.07.2002', 'intretinere']]
    current_list = adaugare(current_list, 4, 25, 200, '26.07.2002', 'intretinere', undo_list, redo_list)
    current_list = do_redo(undo_list, redo_list, current_list)
    assert current_list == [[1, 25, 200, '26.07.2002', 'intretinere'], [4, 25, 200, '26.07.2002', 'intretinere']]
    current_list = do_undo(undo_list, redo_list, current_list)
    assert current_list == [[1, 25, 200, '26.07.2002', 'intretinere']]
    current_list = do_undo(undo_list, redo_list, current_list)
    assert current_list == []
    current_list = do_redo(undo_list, redo_list, current_list)
    current_list = do_redo(undo_list, redo_list, current_list)
    assert current_list == [[1, 25, 200, '26.07.2002', 'intretinere'], [4, 25, 200, '26.07.2002', 'intretinere']]
    current_list = do_redo(undo_list, redo_list, current_list)
    assert current_list == [[1, 25, 200, '26.07.2002', 'intretinere'], [4, 25, 200, '26.07.2002', 'intretinere']]



test_undo_redo()