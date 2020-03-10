#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    for i in range(30):
        if not cell_is_filled():
            move_up()
        if cell_is_filled():
           move_right()

if __name__ == '__main__':
    run_tasks()
