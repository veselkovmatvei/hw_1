#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    for i in range(30):
        if not wall_is_on_the_right():
            fill_cell()
            move_right()
        elif not wall_is_on_the_left():
            fill_cell()
            move_left()
        if wall_is_on_the_left():
            move_down()
            fill_cell()
        elif wall_is_on_the_right():
            move_down()
            fill_cell()



if __name__ == '__main__':
    run_tasks()
