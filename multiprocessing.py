'''
Chad Meadowcroft
Credit to Sentdex (https://pythonprogramming.net/)
'''

import multiprocessing

def spawn(num):
    print('Spawned! {}'.format(num))

if __name__ == '__main__':
    for i in range(5):
        # .process spawns a process object, works similar to threading.thread
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()  # Starts multiprocess
        p.join()   # Performs processes in order