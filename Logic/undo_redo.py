def do_undo(undo_list : list ,redo_list : list):
    """

    :param undo_list:
    :param redo_list:
    :return:
    """
    if undo_list:
        top_undo=undo_list.pop()
        redo_list.append(top_undo)
        return top_undo
    else:
        raise ValueError("No more undo.")
def do_redo(undo_list : list ,redo_list : list):
    """

    :param undo_list:
    :param redo_list:
    :return:
    """
    if redo_list:
        top_redo=redo_list.pop()
        undo_list.append(top_redo)
        return top_redo
    else:
        raise ValueError("No more redo.")
