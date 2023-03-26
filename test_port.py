from queue import Queue  # thread safe
import socket
import time
# import multiprocessing as mp
from threading import Thread

timeout= 1

def check_port(host: str, port: int, results: Queue):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    time.sleep(1)
    if result == 0:
        results.put(port)
    sock.close()

# if __name__ == '__main__':
#     start = time.time()
#     host = "localhost"
#     results = Queue()
#     for port in range(80, 100):
#         check_port(host=host, port=port, results=results)
#     while not results.empty():
#         print("Port {0} is open".format(results.get()))
#     print("Completed scan in {0} sec".format(time.time() - start))  # Completed scan in 20.08940100669861 sec
    
# if __name__ == '__main__':
#     start = time.time()
#     host = "localhost"
    
#     mp.set_start_method('spawn')
#     processes = []
#     pool_manager = mp.Manager()
#     with mp.Pool(len(range(80, 100))) as pool:
#         results = pool_manager.Queue()
#         for port in range(80, 100):
#             processes.append(
#                 pool.apply_async(check_port, (host, port, results))
#             )
#         for process in processes:
#             process.get()
#         while not results.empty():
#             print("Port {0} is open".format(results.get()))
#         print("Completed scan in {0} sec".format(time.time() - start))  # Completed scan in 1.7485041618347168 sec

if __name__ == '__main__':
    start = time.time()
    host = "localhost"
    
    threads = []
    results = Queue()
    for port in range(80, 100):
        t = Thread(target=check_port, args=(host, port, results))
        t.start()
        threads.append(t)


    for thread in threads:
        thread.join()
    while not results.empty():
        print("Port {0} is open".format(results.get()))
    print("Completed scan in {0} sec".format(time.time() - start))  # Completed scan in 1.007812261581421 sec