class Invoker(object):
    def __init__(self, command):
        self.command = command

    def execute(self):
        self.command.execute()
