import sys

from src.services.auto_click import AutoClick

sys.path.append('../services')


class MainMenu:

    @staticmethod
    def _start_actions(selected_option):
        match selected_option:
            case "1":
                AutoClick.start()
            case "2":
                print("Not implemented")
            case _:
                print("Select a valid option")
                MainMenu.start()

    @staticmethod
    def start():
        print(
            "---------------[[[ AUTO-CLICKER ]]]---------------"
            + "\n( How to use ? )"
            + "\nIts simple ! Place your mouse in the desired position and select 'start' option below."
        )
        selected_option = input(
            "Say: "
            + "\n[1] to start"
            + "\n[2] to view recent click positions"
            + "\n"
        )
        MainMenu._start_actions(selected_option)
