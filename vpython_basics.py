# Import the VPython library
from vpython import *

# Create a red box at position (1,0,0) with size (.5,.3,.2) and opacity 0.2
box(pos=vector(1,0,0), size=vector(.5,.3,.2), color=color.red, opacity=0.2)

# Create a purple box at position (2,1,3) with size (0.2,0.3,0.1)
#box(pos=vector(2,1,3), size=vector(0.2,0.3,0.1), color=color.purple)

# Set the scene background to blue and the range to 5
scene.background = color.vector(0,0,1)
scene.range = 5

# The following code is commented out, but it shows how to create a box with a specific color using RGB values.
# It also shows how to create a sphere and a cylinder with specific positions and axes.
# c = vector(1,1,0)
# c2 = color.rgb_to_csv(c)
# bright purple
# box(pos=vector(0,1,3), size=vector(0.2,0.3,0.1), color=vector(0.5,0.1,0.9))
# sphere(pos=vector(3,3,3))
# cylinder(pos=vector(2,2,2),axis=vector(1,4,4))

# Create three cylinders to represent the x, y, and z axes
xaxis = cylinder(axis=vector(5,0,0), color=color.gray(0.5),radius = 0.1)
radius = xaxis.radius
yaxis = cylinder(axis=vector(0,5,0), color=color.gray(0.5),radius = radius) 
zaxis = cylinder(axis=vector(0,0,5), color=color.gray(0.5),radius = radius) 

# Create a dumbbell shape using a cylinder and two spheres
pos = vector(-1,-3,3)
bar = cylinder(pos=pos, radius = 0.7,axis=vector(9,2,2))
s1 = sphere(pos=bar.pos, radius = bar.radius*3)
s2 = sphere(pos=bar.pos+bar.axis, radius = bar.radius*3)

# Create a table using a box and a cylinder for the leg
tablex = 1
tabley = 1
tablez = -7
tablelen = 5
tablewidth = 3
tableht= 7
tablecolor = color.yellow
legradius = tablewidth/20
top = box(pos=vector(tablex,tabley,tablez),size=vector(tablelen,tablewidth,tableht/10),color=tablecolor)
leg1 = cylinder(radius=legradius, axis=vector(tablex,0,tableht-tableht/10),color=tablecolor,
    pos=vector(0,0,-7)) 

#Animations
# Create a box that moves diagonally across the screen
b1 = box(pos=vector(2,2,2))
while b1.pos.x <5 and b1.pos.y<7:
    rate(50) # Set the rate of execution
    b1.pos.x += 0.05
    b1.pos.y += 0.1

# Create a sphere that moves in a circle and plot its position on a graph
movingsphere = sphere(pos=vector(1,0,0), color = vector(0,0,4), make_trail=True, trail_type='points', interval=10)
theta = 0
r = 3
graph(width=300, height=250, title='Test', xtitle='x pos', ytitle='y pos')
xdots = gdots(color=color.green)
ydots = gdots(color=vector(0,2,3))
t=0
while theta<=3.14*2:
    rate(50)
    x=r*cos(theta)
    y=r*sin(theta)
    movingsphere.pos=vector(x,y,0)
    xdots.plot(t,x)
    ydots.plot(t,y)
    t+=1
    theta+=0.03
print(t) # Print the number of iterations of the while loop
