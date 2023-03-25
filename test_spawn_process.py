import multiprocessing as mp
import os

def foo(arg: int):
    [_ for _ in range(arg * 1000000)]
    pid= os.getpid()
    print(f"Arg: {arg}, PID: {pid}")

# if __name__ == '__main__':
#     mp.set_start_method('spawn')
#     p = mp.Process(target=foo, args=(1,))
#     p.start()
    
# if __name__ == '__main__':  # reuse one process for there is quite a big overhead.
#     mp.set_start_method('spawn')
#     with mp.Pool(4) as pool:
#         pool.map(foo, range(1,10))

# if __name__ == '__main__':  # set one process for one worker
#     mp.set_start_method('spawn')
#     with mp.Pool(4, maxtasksperchild=1) as pool:
#         pool.map(foo, range(1,10))

import multiprocessing.spawn
import pprint

# pprint.pprint(multiprocessing.spawn.get_preparation_data("example"))  # 부모 프로세스의 준비 데이터
"""
{'authkey': b'\xa4\xd0\xeb0(\x01\xe1\xdf\x807wq\x17J\xe2\xef\xd9p\xef '
            b'\x17\xc7`\x04b\xa7\xc1\xfby>\xfd\xc2',
 'dir': '/Users/parkbosung/Desktop/cpython',
 'init_main_from_path': '/Users/parkbosung/Desktop/cpython/test_spawn_process.py',
 'log_to_stderr': False,
 'name': 'example',
 'orig_dir': '/Users/parkbosung/Desktop/cpython',
 'start_method': 'spawn',
 'sys_argv': ['/Users/parkbosung/Desktop/cpython/test_spawn_process.py'],
 'sys_path': ['/Users/parkbosung/Desktop/cpython',
              '/Library/Frameworks/Python.framework/Versions/3.9/lib/python39.zip',
              '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9',
              '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload',
              '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages']}
"""

