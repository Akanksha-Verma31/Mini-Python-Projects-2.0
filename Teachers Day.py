import turtle
import time
import random

t = turtle.Turtle()
t.hideturtle()
screen = turtle.Screen()
screen.title("Happy Teacher's Day!!")
screen.bgcolor("black")
screen.setup(700,600)


pen_color = ["blue","white","yellow","green"]
fill_color = ["white"]

screen.tracer(0)
t.speed(0)

def make_circle():
    for i in range(10):
        p, q = random.randrange(-450, 450), random.randrange(-300, 350)
        t2 = turtle.Turtle()  # new pen
        t2.color(random.choice(pen_color))  # it will choose some random color for the pen
        t2.write("Happy Teacher's Day!", font=("chiller", 80, "bold italic"),align="center")
        t2.clear()  # it will clear out the t2 pen

        t.penup()
        t.goto(p, q)
        r = 5
        t.circle(r)
        t.pendown()
        t.begin_fill()
        t.color(random.choice(pen_color))

        for i in range(6):
            #t.forward(30)
            #t.right(144)
            t.circle(r)
        t.end_fill()

#while True:
 #   make_circle()

screen.bgpic('teacher (2).png')
screen.update()
time.sleep(2)
screen.update()
screen.bgpic('teacher3 (1).png')
screen.update()
time.sleep(2)
screen.bgpic('teacher5 (1).png')
screen.update()
time.sleep(2)
screen.bgpic('teachers2 (1).png')
screen.update()
time.sleep(2)


while True:
    make_circle()
    t.clear()

turtle.mainloop()


