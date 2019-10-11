import turtle as t
import random as r


def stop():
    t.bye()

def draw_point(p):
    t.goto(p)
    t.dot(5, r.random(), r.random(), r.random())

def prepare_turtle_canvas():
    t.setup(1024, 768)
    t.bgcolor(0.2, 0.2, 0.2)
    t.penup()
    t.hideturtle()
    t.shape('arrow')
    t.shapesize(2)
    t.pensize(5)
    t.color(1, 0, 0)
    t.speed(100)
    t.goto(-500, 0)
    t.pendown()
    t.goto(480, 0)
    t.stamp()
    t.penup()
    t.goto(0, -360)
    t.pendown()
    t.goto(0, 360)
    t.setheading(90)
    t.stamp()
    t.penup()
    t.home()

    t.shape('circle')
    t.pensize(1)
    t.color(0, 0, 0)
    t.speed(50)

    t.onkey(stop, 'Escape')
    t.listen()

def draw_big_point(p):
    t.goto(p)
    t.color(0.8, 0.9, 0)
    t.dot(15)
    t.write('     '+str(p))

def draw_line(kwargs):
    draw_big_point(kwargs[0])
    draw_big_point(kwargs[1])
    draw_big_point(kwargs[2])
    draw_big_point(kwargs[3])

    # draw p1-p2
    while(True):
        for i in range(0, 50, 2):
            t = i / 100
            x = (2*t**2-3*t+1)*kwargs[0][0]+(-4*t**2+4*t)*kwargs[1][0]+(2*t**2-t)*kwargs[2][0]
            y = (2*t**2-3*t+1)*kwargs[0][1]+(-4*t**2+4*t)*kwargs[1][1]+(2*t**2-t)*kwargs[2][1]
            draw_point((x, y))
        draw_point(kwargs[1])

        # draw p2-p3
        for i in range(0, 100, 2):
            t = i / 100
            x = ((-t**3 + 2*t**2 - t)*kwargs[0][0] + (3*t**3 - 5*t**2 + 2)*kwargs[1][0] + (-3*t**3 + 4*t**2 + t)*kwargs[2][0] + (t**3 - t**2)*kwargs[3][0])/2
            y = ((-t**3 + 2*t**2 - t)*kwargs[0][1] + (3*t**3 - 5*t**2 + 2)*kwargs[1][1] + (-3*t**3 + 4*t**2 + t)*kwargs[2][1] + (t**3 - t**2)*kwargs[3][1])/2
            draw_point((x, y))
        draw_point(kwargs[2])

        # draw p3-p4
        for i in range(50, 100, 2):
            t = i / 100
            x = (2*t**2-3*t+1)*kwargs[1][0]+(-4*t**2+4*t)*kwargs[2][0]+(2*t**2-t)*kwargs[3][0]
            y = (2*t**2-3*t+1)*kwargs[1][1]+(-4*t**2+4*t)*kwargs[2][1]+(2*t**2-t)*kwargs[3][1]
            draw_point((x, y))
        draw_point(kwargs[3])

        #draw p4-p1
        for i in range(0, 100, 2):
            t = i / 100
            x = ((-t**3 + 2*t**2 - t)*kwargs[2][0] + (3*t**3 - 5*t**2 + 2)*kwargs[3][0] + (-3*t**3 + 4*t**2 + t)*kwargs[0][0] + (t**3 - t**2)*kwargs[1][0])/2
            y = ((-t**3 + 2*t**2 - t)*kwargs[2][1] + (3*t**3 - 5*t**2 + 2)*kwargs[3][1] + (-3*t**3 + 4*t**2 + t)*kwargs[0][1] + (t**3 - t**2)*kwargs[1][1])/2
            draw_point((x, y))
        draw_point(kwargs[0])

prepare_turtle_canvas()
points = [(-300, 200), (400, 350), (300, -300), (-200, -200)]
draw_line(points)

t.done()