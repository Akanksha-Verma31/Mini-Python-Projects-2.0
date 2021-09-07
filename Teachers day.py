from turtle import *
import time
import random
from pygame import mixer

my_colors = ["white", "yellow", "pink", "cyan"]
n = 45
speed(0)
bgpic("image.gif")

mixer.init()
mixer.music.load("")
mixer.music.play()

def one():
    return random.randint(15, 70)

def two():
    return random.randint(3,7)

def animate_works(a,b):
    pensize(1)
    hideturtle()
    col1 = random.choice(my_colors)
    l = one()
    color(col1)
    penup()
    goto(a,b)
    pendown()
    for i in range(72):
        forward(l)
        backward(l)
        left(5)

def animated_stars(a,b):
    pensize(1)
    hideturtle()
    col1 = random.choice(my_colors)
    l = one()
    color(col1)
    penup()
    goto(a,b)
    pendown()
    begin_fill()
    for i in range(5):
        forward(l)
        right(144)
        forward(l)
    end_fill()

onscreenclick(animated_stars, 1)    # 1 for left
onscreenclick(animate_works, 3)    # 3 for right

done()
