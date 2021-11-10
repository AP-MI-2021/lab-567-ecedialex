from Domain.vanzare import get_reducere, get_id, creeaza_vanzare, get_titlu, get_gen, get_pret

def aplicare_discount(vanzari,undo_list,redo_list):
    new_vanzari=[]
    for vanzare in vanzari:
        if get_reducere(vanzare) == 'silver':
            vanzare_noua=creeaza_vanzare(get_id(vanzare),
                                         get_titlu(vanzare),
                                         get_gen(vanzare),
                                         get_pret(vanzare)-get_pret(vanzare)*0.05,
                                         get_reducere(vanzare)
                                         )
            new_vanzari.append(vanzare_noua)
        elif get_reducere(vanzare) == 'gold':
            vanzare_noua=creeaza_vanzare(get_id(vanzare),
                                         get_titlu(vanzare),
                                         get_gen(vanzare),
                                         get_pret(vanzare)-get_pret(vanzare)*0.10,
                                         get_reducere(vanzare)
                                         )
            new_vanzari.append(vanzare_noua)
        else:
            new_vanzari.append(vanzare)

    undo_list.append(vanzari)
    redo_list.clear()
    return new_vanzari