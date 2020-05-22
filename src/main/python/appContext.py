from fbs_runtime.application_context.PyQt5 import ApplicationContext

from code_helper import MySerial


class AppContext(ApplicationContext):
    def __init__(self):
        super().__init__()
        self.serialOBJ = None

    def run(self):
        return self.app.exec_()

    def icon(self):
        return self.get_resource("images/led (1).png")

    def serial(self):
        if self.serialOBJ is None:
            self.serialOBJ = MySerial()

        return self.serialOBJ
