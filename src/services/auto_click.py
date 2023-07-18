import pyautogui


class AutoClick:
    @staticmethod
    def start():
        inicial_mouse_position = pyautogui.position()
        print(inicial_mouse_position)
        while True:
            after_mouse_position = pyautogui.position()
            if after_mouse_position != inicial_mouse_position:
                break
            pyautogui.click()
