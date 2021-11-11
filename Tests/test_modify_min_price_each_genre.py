from Domain.vanzare import creeaza_vanzare
from Logic.find_min_price_each_genre import genres_list, min_price_by_genre


def get_data():
    return [
        creeaza_vanzare(1, 'Harap Alb', 'Basm', 10, 'gold'),
        creeaza_vanzare(2, 'Moara cu noroc', 'Nuvela', 25, 'none'),
        creeaza_vanzare(3, 'Mara', 'Roman', 30, 'gold'),
        creeaza_vanzare(4, 'Enigma Otiliei', 'Roman', 50, 'silver'),
        creeaza_vanzare(5, 'Baltagul', 'Roman', 5, 'gold'),
    ]

def test_modify_min_price_each_genre():
    vanzari=get_data()
    lista_genuri=genres_list(vanzari)
    preturi_minime_fiecare_gen=min_price_by_genre(vanzari)
    assert preturi_minime_fiecare_gen[0] == 10
    assert preturi_minime_fiecare_gen[1] == 25
    assert preturi_minime_fiecare_gen[2] == 5
