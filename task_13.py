#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    for i in range(30):
        if wall_is_above() and wall_is_beneath() and not wall_is_on_the_right():
            move_right()
        if not wall_is_above() and wall_is_beneath() and not wall_is_on_the_right():
            move_up ()
            fill_cell()
            move_down ()
            move_right()
        if  wall_is_above() and not wall_is_beneath() and not wall_is_on_the_right():
            move_down ()
            fill_cell()
            move_up ()
            move_right()
        if  not wall_is_above() and not wall_is_beneath() and not wall_is_on_the_right():
            move_down ()
            fill_cell()
            move_up (2)
            fill_cell()
            move_down()
            move_right()
        if not wall_is_above() and wall_is_beneath() and wall_is_on_the_right():
            move_up ()
            fill_cell()
            move_down ()
        if  wall_is_above() and not wall_is_beneath() and wall_is_on_the_right():
            move_down ()
            fill_cell()
            move_up ()
        if  not wall_is_above() and not wall_is_beneath() and wall_is_on_the_right():
            move_down ()
            fill_cell()
            move_up (2)
            fill_cell()
            move_down()



if __name__ == '__main__':
    run_tasks()
