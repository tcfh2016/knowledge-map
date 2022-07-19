with open('test.txt', 'r') as f:
    first_line = f.readline()
    if (len(first_line) == 0) :
        print('empty file!')
