"""
1. Write the method that return the number of threads currently in execution.
Also prepare the method that will be executed with threads and run during the first method counting.
"""


from threading import Thread, activeCount
import time


def f():
    time.sleep(0.5)


def print_active_count():
    print(f'Active count: {activeCount()}')


threading = Thread(target=f)
threading1 = Thread(target=f)
threading2 = Thread(target=f)

threading.start()
threading1.start()
threading2.start()

print_active_count()

threading.join()
threading1.join()
threading2.join()



