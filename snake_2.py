import turtle as t
import time
import random

score=0
high_score=0
delay=0.2
color_screen="green"
color_head="black"
color_snake="white"
color_food="red"

def create_screen(width,height,color):
    screen=t.Screen()
    screen.title("Snake")
    screen.bgcolor(color)
    screen.setup(width=width,height=height)
    screen.tracer(0)
    return screen

def create_turtle(x,y,shape,color):
    tmp=t.Turtle()
    tmp.shape(shape)
    tmp.penup()
    tmp.color(color)
    tmp.setx(x)
    tmp.sety(y)
    return tmp

def checking(head,snake):
    for s in snake:
        if s.distance(head)<15:
            return True
    if head.xcor()>280 or head.xcor()<-280 or head.ycor()>280 or head.ycor()<-280:
        return True

    return False

def goleft():
    head.setheading(180)

def goright():
    head.setheading(0)

def goup():
    head.setheading(90)

def godown():
    head.setheading(270)

screen=create_screen(600,600,color_screen)
screen.listen()
screen.onkeypress(goleft,'a')
screen.onkeypress(goright,'d')
screen.onkeypress(goup,'w')
screen.onkeypress(godown,'s')

head=create_turtle(0,0,'square',color_head)
food=create_turtle(-100,-100,'circle',color_food)
snake=[create_turtle(-20*(i+1),0,'square',color_snake) for i in range(4)]

score=0
while True:
    screen.update()
    (pos,hd)=(head.pos(),head.heading())
    for s in snake:
        (tmp_pos,tmp_hd)=(s.pos(),s.heading())
        s.setheading(hd)
        s.setpos(pos)
        (hd,pos)=(tmp_hd,tmp_pos)
    head.forward(20)

    if head.distance(food)<20:
        [x,y]=snake[-1].pos()
        snake.append(create_turtle(x,y,'square',color_snake))
        food.setpos(random.randrange(-280,280,20),random.randrange(-280,280,20))
        score+=1

    screen.title(str(score))
    time.sleep(delay)

    if checking(head,snake):
        break

screen.mainloop()