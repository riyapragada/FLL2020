#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, Stop)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep(500)

#Defining DriveBase
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
wheel_diameter = 56
axle_track = 115
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
#Defining Large Motor
Large_Motor = Motor(Port.D)

#From base to Frame.
robot.straight(300)
robot.turn(68)
robot.straight(930)
#Drop cubes into the Frame.
Large_Motor.run_target(100,100,then = Stop.HOLD, wait = True)

Large_Motor.run_angle(-100,100,then = Stop.HOLD, wait = True)
#Back up to the Share part of the mission. 
robot.straight(-450)
robot.turn(-70)
#Pushes the cube(s) into the other team's field and returns to base. 
Large_Motor.run_target(100,100,then = Stop.HOLD, wait = True)
robot.straight(220)
Large_Motor.run_angle(-100,100,then = Stop.HOLD, wait = True)
robot.straight(-500)
robot.turn(70)
robot.straight(-400)
