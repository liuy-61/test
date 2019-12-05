class fa:
    def __init__(self):
        self.name = 'father'
    def func_fa(self):
        print('fa fuction {}'.format(self.name ))

class son(fa):
    def __init__(self):
        self.name = 'son'
        super(son, self).__init__()
    def func_son(self):
        self.age = 18
        print('here is a son obj\nage is {}'.format(self.age))

s = son()
s.func_son()