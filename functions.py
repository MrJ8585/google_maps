import random

def node(x1, x2, y1, y2):
    si = x2 - x1
    no = abs(y2 - y1)
    aa = random.uniform(0, si)
    bb = random.uniform(0, no)
    a = x1 + aa
    b = y2 + bb
    if in_bounds(x1, x2, y1, y2, a, b):
        print([a,b])
    else:
        node(x1, x2, y1, y2)

def in_bounds(x1, x2, y1, y2, inputx, inputy):
    if (x1 <= inputx <= x2) and (y2 <= inputy <= y1):
        return True
    return False
