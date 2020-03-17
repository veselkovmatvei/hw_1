#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()
    a = True
    for _ in range(22):
        fill_cell()
    for _ in range(25):
        if a:
            move_right()
        else:
            move_left()
            fill_cell()
            move_down()

if __name__ == '__main__':
    run_tasks()
