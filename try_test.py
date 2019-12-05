try:
    file = open('test.txt', 'r')
except Exception as e:
    print('there is no file named s text.txt')
    response = input('do you want create a new file ?\ny or n')
    if response=='y':
        file = open('test.txt', 'w')
        file.write('created by try...')
    else:
        pass
else:
    content = file.read()
    print(content)

