#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
       for i in range(20):
           if not wall_is_beneath():
                  move_right()
       
       for i in range(20):
           if wall_is_beneath():
                move_right()

if __name__ == '__main__':
    run_tasks()
