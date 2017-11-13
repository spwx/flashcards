class Test(object):

    def __init__(self, name):
        print(name)
        self.name_again(name)

    def name_again(self, nameagain):
        print(nameagain)


test = Test('sean')
