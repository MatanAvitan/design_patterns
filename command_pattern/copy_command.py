from command_pattern.command import Command


class CopyCommand(Command):

    def execute(self):
        print('copy command')
