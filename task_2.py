#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
    move_right()
    move_down(4)

if __name__ == '__main__':
    run_tasks()