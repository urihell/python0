# Examples of mouse input
#http://www.codeskulptor.org/#user26_iuFijDWMI1_2.py


import simplegui
import math

# intialize globals
WIDTH = 450
HEIGHT = 300
ball_pos = [WIDTH / 2, HEIGHT / 2]
BALL_RADIUS = 15
ball_color = "Red"


def distance(p,q):
    #Calculate distance between new point and the last point
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)
    

def click(pos):
#Turns Green when clicked within Radius
    global ball_pos, ball_color
    if distance(pos, ball_pos) < BALL_RADIUS:
        ball_color = "Green"
    else:
#Turns Red and relocates the circle
        ball_pos = list(pos)
        ball_color = "Red"
    
def draw(canvas):
#Drawing a circle based on vraiables
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1,"Black", ball_color)

# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()
    