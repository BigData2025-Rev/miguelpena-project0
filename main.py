from implementation.mainmenu import MainMenu
from implementation.mainmenu_state import MainMenuState
from exceptions.invalidlogincredentials import InvalidLoginCredentials

def main() -> None:
    """
        Program entry point, should handle exceptions at the highest level,
        and run the menu logic as needed.  
    """
    menu: MainMenu = MainMenu("BudgetBuddy")
    while (MainMenu.get_state() != MainMenuState.CLOSING):
        try:
            menu.run()
        except (InvalidLoginCredentials) as e:
            print(e.message)

    print(menu.get_parting_message())

if __name__ == "__main__":
    main()