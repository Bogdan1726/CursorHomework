"""
4. Divide the work between 2 methods: print_cube that returns the cube of number
and print_square that returns the square of number. These two methods should be executed by using 2 different processes.
"""

from multiprocessing import current_process, Process


def print_cube(*args):
    print(f'{current_process().name}')
    for el in args:
        print(f'Cube of number({el}) = {el**3}\n')


def print_square(*args):
    print(f'{current_process().name}')
    for el in args:
        print(f'Square of number({el}) = {el**2}\n')


processes1 = Process(target=print_cube, args=(3, 4, 6, 8))
processes2 = Process(target=print_square, args=(5, 4, 3, 5))

processes1.start()
processes2.start()

processes1.join()
processes2.join()

