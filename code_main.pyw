import gui_systray
from code_helper import MySerial

if __name__ == "__main__":
    serial = MySerial()
    gui_systray.main("led (1).png", serial)
