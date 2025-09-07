import cmd

class MyShell(cmd.Cmd):
    def do_greet(self, line):
        print("Hi,", line)

    def do_exit(self, line):
        return True

MyShell().cmdloop()
