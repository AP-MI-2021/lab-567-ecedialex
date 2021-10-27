from Tests.test_crud import test_create, test_read, test_crud, get_data
from UserInterface.console import run_ui

def main():
    vanzari=[]
    vanzari=get_data()
    vanzari=run_ui(vanzari)

if __name__ == '__main__':
    test_crud()
    main()