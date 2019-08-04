from command_pattern.copy_command import CopyCommand
from command_pattern.paste_command import PasteCommand
from command_pattern.macro_command import MacroCommand
from command_pattern.invoker import Invoker

if __name__ == '__main__':
    # Example 1
    copy_command = CopyCommand()
    invoker = Invoker(copy_command)
    invoker.execute()

    # Example 2
    copy_command = CopyCommand()
    paste_command = PasteCommand()
    command_list = [copy_command, paste_command]
    macro_command = MacroCommand(command_list)
    invoker = Invoker(macro_command)
    invoker.execute()
