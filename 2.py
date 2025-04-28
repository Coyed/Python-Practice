# 2 wheeled mobile
import time

leftwheelmotion = False
rightwheelmotion = False
motion = False

def check_motion():
    global motion
    if leftwheelmotion and rightwheelmotion:
        motion = True
    elif not leftwheelmotion and not rightwheelmotion:
        motion = False
    elif leftwheelmotion and not rightwheelmotion:
        motion = True
        print("Turning left")
    elif rightwheelmotion and not leftwheelmotion:
        motion = True
        print("Turning right")
    else:
        print("Logical Error")


def leftturn():
    global leftwheelmotion, rightwheelmotion, motion
    leftwheelmotion = True
    rightwheelmotion = False
    check_motion()

def rightturn():
    global leftwheelmotion, rightwheelmotion, motion
    rightwheelmotion = True
    leftwheelmotion = False
    check_motion()

def drive():
    rightturn()
    time.sleep(2)
    leftturn()

drive()