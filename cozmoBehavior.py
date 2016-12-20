# -*- coding: utf-8 -*-

"""
Robot Behavior - Version 0.1
Author: Pablo Barros - https://github.com/pablovin/CozmoDevelopmentProject

Description: This method provides Cozmo a pro-active behavior module.

More information: https://github.com/pablovin/CozmoDevelopmentProject


"""


import cozmo
import cozmoGame1

def robotBehavior(robot):
    
   """     
    Robot Behavior method
    
    This method creates a pro-active robot behavior.
    
    Currently it always look for a face, and when it finds it, it starts
    the Boo game.
   """
   face = None

   robot.move_lift(-3)
   robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
   cozmoGame = cozmoGame1.BooGame()
   
   face = None
               
   while True:
      if face and face.is_visible:
         cozmoGame.runGame(robot)
      else:
         face = robot.world.wait_for_observed_face(timeout=30)
         


def run(sdk_conn):
    
   """     
    Run the robot behavior method
    It executes the roboBehavior method, and waits for a crtl+c to exit.
   """ 
   robot = sdk_conn.wait_for_robot()
   robot.say_text("Ready to go!").wait_for_completed()
   

   try:
        robotBehavior(robot)

   except KeyboardInterrupt:
        print("")
        print("Exit requested by user")



if __name__ == '__main__':
    cozmo.setup_basic_logging()
    try:
        cozmo.connect_with_tkviewer(run, force_on_top=True)
    except cozmo.ConnectionError as e:
        print("A connection error occurred: %s" % e)
