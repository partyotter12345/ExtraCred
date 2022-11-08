
# My Game

from graphics import *
import time
import random
import math

'''
circles
window
set of functions
time
global
loop
input
if statement
'''
# while True:
#    print("HI")
#    time.sleep(1)

wHeight = 1000
wWidth = 1000

win = GraphWin("My Game", wWidth, wHeight)

tCircles = list()

found = 0
clicks = 0

def check(p):
    global tCircles
    for tp in tCircles:
        cx = tp[0]
        cy = tp[1]
        ux = p.getX()
        uy = p.getY()
        if abs(cx - ux) <= 100 and abs(cy - uy) <= 100:
            tCircles.remove(tp)
            return (True, tp) # if near a circle return a bool, with tuple

    return False, None



    
    
    
    

def main():
    cir_ran_num = int(input("How many random circles do you want to find? "))
    print(cir_ran_num)
    # create n number of circle
    global wHeight, wWidth, tCircles, found, clicks
    # EC: Find a way to generate random points that are not overlaying? 30 points



    

    
    #to ensure loop runs until # of circles desired is reached
    while len(tCircles) < cir_ran_num:
        for i in list(range(cir_ran_num)):
            #generate rand x value
            x = random.randrange(100, wHeight / 2)
            #generate rand y value
            y = random.randrange(100, wWidth / 2)

            for check in tCircles:
                x2 = check[0]
                y2 = check[1]

                euclidiandistance = math.dist([x,y],[x2,y2])

                if euclidiandistance <100:
                    break
            else:
                print("x: {} y: {}".format(x, y))
                tCircles.append((x,y))


            

        

        #adds the tuple to the tCircles list
        #prints the tuple
        
    print(tCircles)

    while True:
        userPoint = win.getMouse()
        status,tp = check(userPoint)
        print(userPoint)
        print(status)
        print(tp)
        clicks = clicks + 1
        if status:
            circle = Circle(Point(tp[0], tp[1]), 50)
            circle.setFill("red")
            circle.draw(win)
            found = found + 1
        print(tCircles)
        # check game status
        if len(tCircles) == 0:
            print("Game Over Clicks {} Founds: {}".format(clicks, found))
            break
    
    win.close() # close the window


main()

