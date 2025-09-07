import pdb

def test():
    x = 1
    pdb.set_trace()  # Use 'n' to move to next line during debugging
    y = 2
    z = x + y
    print(z)

test()
