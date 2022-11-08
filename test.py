from graphics import *
list = [(157, 373), (459, 438), (496, 160), (287, 478), (371, 282), (273, 218), (128, 475), (122, 168), (360, 108), (494, 283)]

print(list)

wHeight = 1000
wWidth = 1000

win = GraphWin("My Game", wWidth, wHeight)

for i in list :
    x=i[0]
    y=i[1]

    circle = Circle((Point(x,y)), 50)
    circle.setFill("red")
    circle.draw(win)
    
