import os
dir = 'ddd/dd/rr/r'
id = '1'
print(os.path.join(dir,'porject_'+id))

class A():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def set(self,weight):
        self.weight = weight
    def oo(self):
        print(self.name, self.age, self.weight)

a = A('ll',22)
a.set(60)
a.oo()