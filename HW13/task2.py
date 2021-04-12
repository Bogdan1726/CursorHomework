"""
2. Print current date by using 2 threads.
#1. Define a subclass using Thread class.
#2. Instantiate the subclass and trigger the thread.
"""

from threading import Thread
import datetime


class ClassDateTime(Thread):

    def date(self):
        now = datetime.date.today()
        print(f'The current date: {now}')

    def time(self):
        now = datetime.datetime.now().time()
        print(f'The current time: {now}')


threading = ClassDateTime()
threading2 = ClassDateTime()

threading.date()
threading2.time()

threading.start()
threading2.start()

threading.join()
threading2.join()
