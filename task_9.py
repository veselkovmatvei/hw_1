#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
     for i in range(30):
         if not wall_is_above() and not wall_is_on_the_right():
                fill_cell()
                move_right(1)
         elif not wall_is_above() and wall_is_on_the_right():
                  fill_cell() 
         elif wall_is_above() and not wall_is_on_the_right():
              move_right(1)

if __name__ == '__main__':
    run_tasks()
