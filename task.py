from RPA.Browser.Selenium import Selenium
from RPA.Dialogs import Dialogs
import time


sel = Selenium()
dia = Dialogs()


def minimal_task():
    dia.add_text_input("search", label="Website")
    response = dia.run_dialog()
    sel.open_available_browser(f'https://www.{response.search}')
    sel.maximize_browser_window()
    time.sleep(5)


if __name__ == "__main__":
    minimal_task()
