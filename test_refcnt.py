# example code, guess how many reference counted
y="whatever"
message = [y]

def foo(msg=y):
    assert msg == y
foo(*message)

import sys

print(sys.getrefcount(y)) # 6 not 4, guess why?