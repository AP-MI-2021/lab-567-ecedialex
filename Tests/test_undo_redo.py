from Domain.vanzare import get_pret, get_id
from Logic.crud import create
from Logic.discount import aplicare_discount
from Logic.sort_ascending import sort_ascending
from UserInterface.console import handle_undo, handle_redo


def test_undo_redo():
    vanzari=[]
    undo_list=[]
    redo_list=[]
    vanzari = create(vanzari, 1, 'Harap Alb', 'Basm', 15, 'gold', undo_list, redo_list)
    assert len(vanzari) == 1
    vanzari = create(vanzari, 2, 'Moara cu noroc', 'Nuvela', 25, 'none', undo_list, redo_list)
    assert len(vanzari) == 2
    vanzari = create(vanzari, 3, 'Mara', 'Roman', 35, 'gold', undo_list, redo_list)
    assert len(vanzari) == 3
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 1
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 0
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 0
    vanzari = create(vanzari, 1, 'Harap Alb', 'Basm', 15, 'gold', undo_list, redo_list)
    vanzari = create(vanzari, 2, 'Moara cu noroc', 'Nuvela', 25, 'none', undo_list, redo_list)
    vanzari = create(vanzari, 3, 'Mara', 'Roman', 35, 'gold', undo_list, redo_list)
    assert len(vanzari) == 3
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 3
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 1
    vanzari = create(vanzari, 4, 'Enigma Otiliei', 'Roman', 12, 'silver', undo_list, redo_list)
    assert len(vanzari) == 2
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 1
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 0
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 1
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    vanzari = aplicare_discount(vanzari,undo_list,redo_list)
    vanzari = handle_undo(vanzari,undo_list,redo_list)
    assert get_pret(vanzari[0]) == 15
    assert get_pret(vanzari[1]) == 12
    vanzari = sort_ascending(vanzari,undo_list,redo_list)
    assert get_id(vanzari[0]) == 4
    assert get_id(vanzari[1]) == 1
    vanzari = handle_redo(vanzari,undo_list,redo_list)
    assert get_id(vanzari[0]) == 4
    assert get_id(vanzari[1]) == 1
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert get_id(vanzari[0]) == 1
    assert get_id(vanzari[1]) == 4
