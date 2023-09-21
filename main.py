import turtle
import time


# PROJECT TRACKER:
# Black and white: DONE 
# 1 picture drawn with Turtle graphics: DONE
# 2 Vars that can change the image: DONE
# At least 2 for loops: DONE
  # At least one of the loops uses the loop var to do something dif each time: DONE
# At least 2 functions: DONE
  # Each function is called at least 2 times: DONE
  # At least one function has a a parameter with 2+ arguments: DONE
'''
How-to:
trackpad width between 1 and 340 is best (default 100)

logo_border_sides changes the number of sides the logo has, I reccomend between 4 and 12 (3 is iffy)
'''

# Custom vars
trackpad_width = 100 # 1 to 340 (100 is default)
logo_border_sides = 10 # sides on the on-screen logo between 4 and 12 (for best results)

# Even out logo border
if logo_border_sides == 4:
  tare = 5
else:
  if logo_border_sides == 3:
    tare = 10
  else:
    tare = 0

# Makes the turtle draw instantly
turtle.tracer(0,0)

'''include interactive var'''

'''Meet requirments:
- Don't have look super good
- 2 functions
- Can add a little spiral or something to meet requirments
'''

# Func defs for basics
# Letter is angle, word is line
# r(10) = turn 10 deg right
# right(10) = go 10 px to the right
def speed(speed):
  turtle.speed(speed)

def go(px):
  turtle.forward(px)

def back(px):
  turtle.back(px)

def right(degrees):
  turtle.right(degrees)

def left(degrees):
  turtle.left(degrees)

# Set angle
def set_angle(degree):
  turtle.seth(degree)
'''
90 is up
180 is left
270 is down
0 is right
'''

def on():
  turtle.pendown()

def off():
  turtle.penup()

def set(x, y):
  turtle.setx(x)
  turtle.sety(y)
  
def set_draw(xd, yd):
  turtle.setx(xd)
  turtle.sety(yd)

def clear():
  turtle.clearscreen()

def wait(seconds):
  time.sleep(seconds)

# Multi step functions
def up(px):
  # Gets the current direction (to return to)
  original_direction = turtle.heading()
  set_angle(90)
  go(px)
  set_angle(original_direction)

def down(px):
  original_direction = turtle.heading()
  set_angle(270)
  go(px)
  set_angle(original_direction)

# def left(px):
#   original_direction = turtle.heading()
#   a(180)
#   f(px)
#   a(original_direction)

# def right(px):
#   original_direction = turtle.heading()
#   a(0)
#   f(px)
#   a(original_direction)
'''CODE STARTS HERE'''
# Start the code
# Top is (300 x 120)
# Screen is (280X100)

# Draw screen
speed(10)
on()
go(150)
up(120)
for _ in range(2):
  back(150)
down(120)
go(150)
off()
back(150)
# Draw bottom part
set_angle(250)
on()
go(100)
set_angle(0)
go(368)
set_angle(110)
go(100)
set_angle(90)
go(110)
set_angle(190)
off()
go(10)
on()
set_angle(180)
go(280)
left(90)
go(100)
left(90)
go(280)
left(90)
go(100)
off()
# Set up for drawing keys
down(114)
set_angle(0)
back(280)

# Key drawing function
def keys(side_length,space,quantity):
  go(space/2) # Centers keys
  for _ in range(quantity):
    on()
    for i in range(4):
      go(side_length)
      right(90)
    off()
    go(side_length+space)

    
# Row 1
speed(10)
keys(15,2.5,16)
# Rows 2 and 3
for l in range(2):
  off()
  down(20)
  back(277)
  # Centers rows
  'This is where the loop variable is used in the for loop'
  back(((l+1)*17.5)/2)
  back(2*((l+1)*2))
  keys(15,2.5,(16+(l+1)))
  # Centers row 3
  back(14/2)

# Draws the trackpad
set(0,-65)
back(trackpad_width/2)
on()
for _ in range(2):
  go(trackpad_width)
  right(90)
  go(25)
  right(90)
# Draws the trackpad clicky buttons
down(2*(25/3))
go(trackpad_width)
off()
# turtle
back(trackpad_width/2)
on()
down(25/3)
off()

# Laptop body done drawing
# Draw laptop screen icon
set(0,55+tare)
down(25)
on()
# Draw logo border
go(108/logo_border_sides) # Center it
for n in range (logo_border_sides):
  back(220/logo_border_sides)
  right(360/logo_border_sides)
off()
set(-19,70)
on()
# Draw star
set_angle(0)
for _ in range(5):
  go(40)
  right(144)
# Write Kehillah
off()
set(-(25/2.5),30)
set_angle(0)
down(20)
back(68)
turtle.write("Kehillah Jewish High School")


# Hides turtle arrow
turtle.hideturtle()

# Second part of turtle instant draw
turtle.update()