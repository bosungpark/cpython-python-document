import multiprocessing as mp

# Queue example
# def foo(input: mp.Queue, output: mp.Queue):
#     input_ = input.get()  # Lock semaphore
#     [ _ for _ in range(10000)]  # some meaningless action
#     output.put(f"Time taking work done, {input_}")

# if __name__ == '__main__':
#     mp.set_start_method('spawn')
#     pool_manager = mp.Manager()
#     with mp.Pool(2) as pool:
#         inputs = pool_manager.Queue()
#         outputs = pool_manager.Queue()
#         for i in range(10):
#             inputs.put(f"{i}th")
#             pool.apply(foo, (inputs, outputs))

#         for f in range(10):
#             print(outputs.get(block=False))

# Pipe example
def foo2(child_pipe: mp.Pipe, child_lock: mp.Lock):
    child_lock.acquire(blocking=False)
    try:
        input_ = child_pipe.recv()
    finally:
        child_lock.release()

    [ _ for _ in range(10000)] # some meaningless action

    child_lock.acquire(blocking=False)
    try:
        child_pipe.send(f"Fin {input_}th req")
    finally:
        child_lock.release()

if __name__ == '__main__':
    mp.set_start_method('spawn')
    pool_manager = mp.Manager()
    with mp.Pool(2) as pool:
        parent_pipe, child_pipe = mp.Pipe()
        child_lock = pool_manager.Lock()
        results = []
        for input in range(10):
            parent_pipe.send(input)
            results.append(pool.apply_async(foo2,
                                            args=(child_pipe, child_lock)))
            print("Got {0:}".format(parent_pipe.recv()))
        parent_pipe.close()
        child_pipe.close()
