# -*- coding: utf-8 -*-

"""
Boo Game - Version 0.1
Author: Pablo Barros - https://github.com/pablovin/CozmoDevelopmentProject

Description: This game reproduces the "Boo" game with the Cozmo robot.

The robot finds a person's face, the person puts the hands over the face, and then scares the robot.


More information: https://github.com/pablovin/CozmoDevelopmentProject


"""

import cozmo
import time

class BooGame:

   def runGame (self, robot):
       
       """     
       Boo Game
        
       This game happens in thre steps:
           1) The robot trys to find a face and shows a greeting animation.
           2) The robot looks down and then up, the person cover the face with the hands and the cannot find the face anymore.
           3) the robot finds the face again and shows a scared animation.


           The method is based on the robot.world.visible_face_count() to determine if there is a face 
           in the robot's view field. 
           
           To give more stability to the model, we use the sleep clause in the steps one an two.
           
           A in-between step is used (between step 1 and 2) to make sure the face of the person is hidden.
       """
   
       state="first"
       
       amountOfFacesNotFound = 0
       amountOfFacesFound = 0
       isSleep = True
       while True:
           
           if isSleep:
               time.sleep(0.2)
               
           numberOfFaces = robot.world.visible_face_count()                      
           
           if numberOfFaces == 0:
               amountOfFacesNotFound +=1 
           else:
                amountOfFacesFound +=1
           
           if state=="first":
               if numberOfFaces > 0 and amountOfFacesFound>3:
                   robot.play_anim(name="anim_freeplay_reacttoface_identified_01_head_angle_40").wait_for_completed()
                   state="second"
                   amountOfFacesFound = 0
                   amountOfFacesNotFound = 0
                   
           elif state=="second":
               robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE).wait_for_completed()          
               state = "third"
               robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
                                                              
           elif state=="third":                                        
               
               if numberOfFaces == 0 and amountOfFacesNotFound>2:
                   robot.play_anim(name="anim_hiking_observe_01").wait_for_completed()
                   robot.move_lift(-3)
                   robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
                   state="fourth"                   
                   amountOfFacesFound = 0
                   amountOfFacesNotFound = 0  
                   isSleep = False
                   
               elif amountOfFacesFound > 3:
                   state = "first"
                   amountOfFacesFound = 0
                   amountOfFacesNotFound = 0                   
                                
           else:
                if numberOfFaces > 0:
                   robot.play_anim(name="anim_freeplay_reacttoface_like_01").wait_for_completed()
                   robot.move_lift(-3)
                   robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
                   state="first"
                   amountOfFacesFound = 0
                   amountOfFacesNotFound = 0
                   isSleep = True
                   
                   
                                     
           print ("State:", state)
           print ("Number of faces:", numberOfFaces)    
           print ("amountOfFacesNotFound:", amountOfFacesNotFound)
           print ("amountOfFacesFound:", amountOfFacesFound)
           