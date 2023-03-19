import gc

gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_SAVEALL)

# def gc_callback(phase, info):  # custom gc
#     print(f"GC phase:{phase} with info:{info}")

# gc.callbacks.append(gc_callback)

x=[0,1,2,3]
x.append(x)
del x
gc.collect() # Can collect specifiic generation > gc.collect(0) ~ gc.collect(3)
print("garbage >> ",gc.garbage)
print("garbage threshold >> ",gc.get_threshold())
print("garbage count >> ",gc.get_count())