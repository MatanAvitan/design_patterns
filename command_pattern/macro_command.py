from command_pattern.command import Command


class MacroCommand(Command):
    def __init__(self, command_list):
        self.command_list = command_list

    def execute(self):
        for command in self.command_list:
            command.execute()
