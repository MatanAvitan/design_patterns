from command_pattern.command import Command


class PasteCommand(Command):

    def execute(self):
        print('paste command')
