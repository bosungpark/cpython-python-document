from queue import Queue  # thread safe
import _xxsubinterpreters as subinterpreters
from threading import Thread
import textwrap as tw
import time

timeout= 1

def run(host: str, port: int, results: Queue):
    channel_id= subinterpreters.channel_create()
    interpid= subinterpreters.create()
    subinterpreters.run_string(
        interpid,
        tw.dedent(
        """
        import socket; import _xxsubinterpreters as subinterpreters
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        subinterpreters.channel_send(channel_id, result)
        sock.close()
        """
        ),
        shared=dict(
        channel_id=channel_id,
        host=host,
        port=port,
        timeout=timeout
        )
    )
    output = subinterpreters.channel_recv(channel_id)
    subinterpreters.channel_release(channel_id)
    if output == 0:
        results.put(port)


if __name__ == '__main__':
    start = time.time()
    host = "localhost"
    
    threads = []
    results = Queue()
    for port in range(80, 100):
        t = Thread(target=run, args=(host, port, results))
        t.start()
        threads.append(t)


    for thread in threads:
        thread.join()
    while not results.empty():
        print("Port {0} is open".format(results.get()))
    print("Completed scan in {0} sec".format(time.time() - start))  # Completed scan in 0.3999629020690918 sec