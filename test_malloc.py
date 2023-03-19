# import sys

# # Show blocks of each chunk of pool
# sys._debugmallocstats()
# """
# class   size   num pools   blocks in use  avail blocks
# -----   ----   ---------   -------------  ------------
#     0     16           1              73           180
#     1     32           7             867            15
#     2     48          39            3106           170
#     3     64         147            9198            63
#     4     80         116            5775            25
#     ...
# """
import tracemalloc

tracemalloc.start()

def to_celsius(fahrenheit,/,option=None):  # cpython/test_malloc.py:19: size=712 B, count=2, average=356 B
    return (fahrenheit-32)*5/9

values = range(0,100,10)  # cpython/test_malloc.py:22: size=48 B, count=1, average=48 B
for v in values:
    c = to_celsius(v)

after=tracemalloc.take_snapshot()

tracemalloc.stop()
after=after.filter_traces([tracemalloc.Filter(True, "**/test_malloc.py")])
stats=after.statistics("lineno")

for s in stats:
    print(s)