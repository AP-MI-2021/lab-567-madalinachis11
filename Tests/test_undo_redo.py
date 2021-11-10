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
    current_list = adaugare(current_list, 1, 1, 200, 'data1', 'intretinere', undo_list, redo_list)
    current_list = adaugare(current_list, 2, 2, 200, 'data2', 'canal', undo_list, redo_list)
    current_list = adaugare(current_list, 3, 3, 200, 'data3', 'alte cheltuieli', undo_list, redo_list)
    current_list = do_undo(undo_list, redo_list, current_list)
    assert len(current_list) == 2
    current_list = do_undo(undo_list, redo_list, current_list)
    assert len(current_list) == 1
    current_list = do_undo(undo_list, redo_list, current_list)
    assert len(current_list) == 0
    current_list = do_undo(undo_list, redo_list, current_list)
    assert len(current_list) == 0

    """
        A Doua adaugare
    """
    current_list = adaugare(current_list, 1, 25, 200, 'data1', 'intretinere', undo_list, redo_list)
    current_list = adaugare(current_list, 2, 25, 200, 'data2', 'canal', undo_list, redo_list)
    current_list = adaugare(current_list, 3, 25, 200, 'data3', 'alte cheltuieli', undo_list, redo_list)
    current_list = do_redo(undo_list, redo_list, current_list)
    assert len(current_list) == 3
    current_list = do_undo(undo_list, redo_list, current_list)
    current_list = do_undo(undo_list, redo_list, current_list)
    assert len(current_list) == 1
    current_list = do_redo(undo_list, redo_list, current_list)
    assert len(current_list) == 2
    current_list = do_redo(undo_list, redo_list, current_list)
    assert len(current_list) == 3
    current_list = do_undo(undo_list, redo_list, current_list)
    current_list = do_undo(undo_list, redo_list, current_list)
    assert len(current_list) == 1
    current_list = adaugare(current_list, 4, 25, 200, 'data4', 'intretinere', undo_list, redo_list)
    current_list = do_redo(undo_list, redo_list, current_list)
    assert len(current_list) == 2
    current_list = do_undo(undo_list, redo_list, current_list)
    assert len(current_list) == 1
    current_list = do_undo(undo_list, redo_list, current_list)
    assert len(current_list) == 0
    current_list = do_redo(undo_list, redo_list, current_list)
    current_list = do_redo(undo_list, redo_list, current_list)
    assert len(current_list) == 2
    current_list = do_redo(undo_list, redo_list, current_list)
    assert len(current_list) == 2



test_undo_redo()