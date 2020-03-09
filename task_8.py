#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_7():
        for i in range(20):
            if wall_is_above():
               move_right()
            elif wall_is_beneath():
                move_right()

if __name__ == '__main__':
    run_tasks()
