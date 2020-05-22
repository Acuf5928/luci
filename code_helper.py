import time

import serial
import serial.tools.list_ports


class MySerial:
    def __init__(self, responseMessage="", sendMessage=""):
        self.message = ""
        if (responseMessage != "") & (sendMessage != ""):
            self.search(responseMessage, sendMessage)
        try:
            self.s = serial.Serial(port="COM19", baudrate=9600, timeout=.1)
        except Exception:
            print(Exception)

    def write(self, message):
        try:
            self.s.write(reformatString(message))
        except Exception:
            print(Exception)

    def read(self):
        for number in range(0, 5):
            data = self.s.readline().decode()
            print(data)
            if data == "":
                time.sleep(.5)
            else:
                self.message = data
                break

#WIP
    def search(self, responseMessage, sendMessage):
        ports = serial.tools.list_ports.comports(include_links=False)
        for port in ports:
            print(port)
            try:
                with serial.Serial(port="COM13", baudrate=9600, timeout=.5) as s:

                    time.sleep(.5)
                    s.write(reformatString(sendMessage))

                    if self.message == responseMessage:
                        print(port)
                    s.close()
            except Exception as Ex:
                print(Ex)


def reformatString(message):
    strMessage = str(message)
    if strMessage[-1] != "\n":
        return (strMessage + "\n").encode("utf8")
    else:
        return strMessage.encode("utf8")


if __name__ == "__main__":
    s = MySerial("iM HERE", "TROVATO")
