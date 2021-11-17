from Logic.crud import create
from UserInterface.console2 import run_ui2


def main():
    vanzari = []
    undo_list = []
    redo_list = []
    vanzari = create(vanzari, 1, 'Harap Alb', 'Basm', 15, 'gold', undo_list, redo_list)
    vanzari = create(vanzari, 2, 'Moara cu noroc', 'Nuvela', 25, 'none', undo_list, redo_list)
    vanzari = create(vanzari, 3, 'Mara', 'Roman', 35, 'gold', undo_list, redo_list)
    vanzari = create(vanzari, 4, 'Enigma Otiliei', 'Roman', 12, 'silver', undo_list, redo_list)
    vanzari = create(vanzari, 5, 'Baltagul', 'Roman', 5, 'none', undo_list, redo_list)
    vanzari = run_ui2(vanzari, undo_list, redo_list)

if __name__ == '__main__':
    main()