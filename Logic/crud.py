from Domain.vanzare import creeaza_vanzare, get_id


def create(lst_vanzari,
           id_vanzare, titlu, gen, pret, tip_client):
    """
    Creeaza o lista de vanzari
    :param lst_vanzari: lista de vanzari
    :param id_vanzare:
    :param titlu:
    :param gen:
    :param pret:
    :param tip_client:
    :return: O noua lista formata din lst_vanzari si noua vanzare adaugata
    """
    vanzare = creeaza_vanzare(id_vanzare, titlu, gen, pret, tip_client)
    return lst_vanzari + [vanzare]


def read(lst_vanzari, id_vanzare=None):
    """
    Citeste o vanzare din "baza de date"
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii
    :return: vanzara cu id-ul id_vanzare sau lista cu toate vanzarile daca id_vanzare=None
    """
    vanzare_cu_id = None
    for vanzare in lst_vanzari:
        if get_id(vanzare) == id_vanzare:
            vanzare_cu_id = vanzare
    if vanzare_cu_id:
        return vanzare_cu_id
    return lst_vanzari


def update(lst_vanzari, new_vanzare):
    """
    Actualizeaza o vanzare
    :param lst_vanzari: lista de vanzari
    :param new_vanzare: vanzarea care se va actualiza - id-ul trebuie sa fie unul existent
    :return: o lista cu vanzarea actualizata
    """
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != get_id(new_vanzare):
            new_vanzari.append(vanzare)
        else:
            new_vanzari.append(new_vanzare)
    return new_vanzari


def delete(lst_vanzari, id_vanzare):
    """
    Sterge o vanzare din lst
    :param lst_vanzari: lista cu toate vanzarile
    :param id_vanzare: id-ul vanzarii ce se va sterge
    :return: o lista de vanzari fara vanzara cu id-ul id_vanzare
    """
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != id_vanzare:
            new_vanzari.append(vanzare)
    return new_vanzari
