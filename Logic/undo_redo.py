def do_undo(undo_list: list, redo_list: list, current_list: list):
    """
    Anuleaza ultima comanda de modificare a listei vanzari
    :param current_list: lista curenta
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :return: lista vanzari inainte de modificare daca se poate face undo
             none daca nu se mai poate face undo
    """
    if undo_list:
        redo_list.append(current_list)
        return undo_list.pop()

    return None


def do_redo(undo_list: list, redo_list: list, current_list: list):
    """
    Anuleaza un undo
    :param current_list: lista curenta
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :return: lista vanzari inainte de undo daca se poate
             none daca nu se poate face redo
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo

    return None
