def fetcher(obj, index):
    try:
        return obj[index]
    except IndexError:
        print('wrong index!')

x = 'spam'
fetcher(x, 4)
print('done')
