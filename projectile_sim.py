from vpython import *
#Web VPython 3.2

#Changing background to blue and setting camera pointing to centre of projectile's path
scene.background = vector(4,5,5)
scene.centre = vector(0,5,0)
scene.width = 400

#ground box indicator
ground = box(pos=vector(0,0,0), size=vector(5,0.2,5), color = vector(1,0.3,0))

#Incomplete
def Fair(c, v):
    if v>0:
        return c*(-v)

#Projectile function
def Projectile1(g, dt):
    ay = -g
    y= 10
    vy = 0
    ball = sphere(pos = vector(0,y,0), radius = 1, color = vector(0,1,2))
    t = 0
    while y>0:
        y += vy * dt
        vy += ay * dt
        t += dt
        rate(100)
        ball.pos.y = y
        #if y<=0:
            #print(y)
            #print("actual time" = t + y/vy)
    return t, vy, y
        

g = 9.8
dt = 0.01 #smaller val => more accurate t and vy

t, vy,y = Projectile1(g, dt)

print("Ball lands at t=", t, "seconds with velo", vy, "m/s")

#theoretical vals (to check for truncation error(limits of computing))
tth = t-y/vy
print('Theoretical val of t =', tth)
print('Th val of vf = ', g*tth)