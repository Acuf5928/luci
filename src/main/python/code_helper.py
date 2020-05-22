import time

import serial


class MySerial:
    def __init__(self):
        self.s = None
        self.checkSerial()

    def write(self, message):
        try:
            self.checkSerial()
            self.s.write(reformatString(message))
        except Exception:
            pass

    def read(self):
        self.checkSerial()
        time.sleep(.2)
        return self.s.readline().decode()

    def checkSerial(self):
        if self.s is None:
            try:
                self.s = serial.Serial(port="COM19", baudrate=115200, timeout=.1)
            except Exception:
                self.s = None


def reformatString(message):
    strMessage = str(message)
    if strMessage[-1] != "\n":
        return (strMessage + "\n").encode("utf8")
    else:
        return strMessage.encode("utf8")
