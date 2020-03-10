#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    for i in range(30):
        if wall_is_above() and wall_is_beneath() and not wall_is_on_the_right():
           move_right()
        if wall_is_above() and not wall_is_beneath() and not wall_is_on_the_right():
           move_right()
        if not wall_is_above() and wall_is_beneath() and not wall_is_on_the_right():
           fill_cell()
           move_right()
        if not wall_is_above() and not wall_is_beneath() and not wall_is_on_the_right():
            move_right()
        if not wall_is_above() and wall_is_beneath() and wall_is_on_the_right():
           fill_cell()



if __name__ == '__main__':
    run_tasks()
