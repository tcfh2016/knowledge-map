list = [1, 2, 3, 4, 5]

def test_scope(start):
    status = start
    def nested():
        #nonlocal status
        print(status)
        status += 1
    return nested

f = test_scope(0)
f()
