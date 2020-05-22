import _thread
import json

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from code_helper import MySerial


class AppContext(ApplicationContext):
    def __init__(self):
        super().__init__()
        self.status = None
        self.serialOBJ = None
        self.checkStatusBackground()

    def run(self):
        return self.app.exec_()

    def name(self):
        return "Luci"

    def icon(self):
        return self.get_resource("images/led (1).png")

    def serial(self):
        if self.serialOBJ is None:
            self.serialOBJ = MySerial()

        return self.serialOBJ

    def checkStatusBackground(self):
        _thread.start_new_thread(self.checkStatusContinue, ())

    def checkStatusContinue(self):
        while True:
            self.checkStatus()

    def checkStatus(self):
        status = self.serial().read()

        if status is "":
            self.status = None
            return

        self.status = json.loads(status)
