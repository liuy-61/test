import  copy
a = {1:'q', 2:[1,2,3], 3:{'key':'value'}}
b = copy.copy(a)
a[1]='w'
a[2][0]=11
print(a, b)
print(id(a), id(b))
print(id(a[1])==id(b[1]))