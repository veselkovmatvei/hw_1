#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
      
      for i in range(20):
          if not wall_is_beneath():
                 move_down()
      for i in range(20):
          if wall_is_beneath():
             move_right()

      for i in range(1):
          move_down()
          move_left()

      for i in range(20):
          if not wall_is_on_the_left():
                 move_left()
      

if __name__ == '__main__':
    run_tasks()
    