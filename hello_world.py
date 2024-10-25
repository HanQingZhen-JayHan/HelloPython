class HelloWorld:
    def __init__(self) -> None:
        self.msg = 'Hello World!'

    def print_msg(self) -> None:
        print(self.msg)

    def set_msg(self, new_msg) -> None:
        self.msg = new_msg

    def get_msg(self):
        return self.msg

if __name__ == '__main__':
    h = HelloWorld()
    h.print_msg()
