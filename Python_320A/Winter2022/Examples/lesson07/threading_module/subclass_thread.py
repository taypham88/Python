"""
A simple demonstration of subclassing threads

Same as the simple_threads.py example, but with a Thread subclass
"""

import random
import time
import threading


def working_function(max, storage=None):
    """
    an example function that does very little, but
    simulates a complex computation
    """
    num = random.randint(1, max)
    # pause for up to two seconds to simulate computation time
    time.sleep(random.random() * 2)

    if storage is not None:
        storage.append(num)
    print("computed", num)
    return num


class WorkingThread(threading.Thread):

    def __init__(self, max, storage=None):
        self.max = max
        self.storage = storage
        super().__init__()

    def run(self):
        working_function(self.max, self.storage)


# using it sequentially:

def run_sequential():
    results = []
    for i in range(10):
        working_function(100, results)
    print(f"{results=}")


def run_in_threads():
    results = []
    for i in range(10):
        WorkingThread(100, results).start()
    print(f"{results=}")
    return results


# waiting for the threads to complete:
def run_in_threads_wait():
    results = []
    all_threads = []
    for i in range(10):
        t = WorkingThread(100, results)
        all_threads.append(t)
        t.start()

    # make sure they are all done before finishing.
    for t in all_threads:
        print(f"waiting for thread: {t.ident}")
        t.join()

    print(f"{results=}")
    return results

if __name__ == "__main__":
    # run_sequential()

    results1 = run_in_threads()
    print("results after calling run_in_threads", results1)

    results2 = run_in_threads_wait()
    print("results after calling run_in_threads_wait", results2)

    print("results after waiting:", results1)
    print("results after waiting:", results2)

