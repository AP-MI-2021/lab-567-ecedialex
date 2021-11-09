from Tests.test_crud import test_create, test_read, test_crud, get_data
from Tests.test_discount import test_discount
from Tests.test_modificare_gen import test_modificare_gen
from Tests.test_modify_min_price_each_genre import test_modify_min_price_each_genre
from Tests.test_sort_ascending import test_sort_ascending
from Tests.test_titles_count_each_genre import test_titles_count_each_genre
from UserInterface.console import run_ui

def main():
    vanzari=[]
    vanzari=get_data()
    vanzari=run_ui(vanzari)

if __name__ == '__main__':
    test_crud()
    test_discount()
    test_modificare_gen()
    test_modify_min_price_each_genre()
    test_sort_ascending()
    test_titles_count_each_genre()
    main()