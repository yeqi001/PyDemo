class coder:
    def __init__(self, name="张三", sex="男", age=30):
        self.age = age
        self.name = name
        self.sex = sex
        self.__phone = 13114445555

    def work(self):
        return self.show_phone()

    def sleep(self):
        pass

    def show_phone(self):
        print(self.__phone)

    def __del__(self):
        print("再见程序猿")

class coder1(coder):
    def __init__(self):
        super().__init__()
        self.name="小王"
        self.__phone=111

    def work(self):
        super(coder1, self).work()
        print(2)
c1 = coder1()
c1.work()