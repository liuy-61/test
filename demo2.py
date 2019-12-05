text = 'first line\nsecond line\nlast line\n'
print(text)
file = open('file.txt', 'w')
file.write(text)
file.close()