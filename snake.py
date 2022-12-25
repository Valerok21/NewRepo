import turtle
import random
import time

score = 0
high_score = 0
delay_time = 0.2

screen = turtle.Screen()
screen.title("Snake")
screen.bgcolor("green")
screen.setup(width=600, height=600)

snake = turtle.Turtle()
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = "Stop"

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.speed(0)
food.penup()
food.goto(0, 100)

sc = turtle.Turtle()
sc.shape("square")
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0, 250)
sc.write("Your_score: 0 high_score : 0", align="center", font=("Arial", 24, "normal"))

turtle.mainloop()

def moveleft():
    if snake.direction != "right":
        snake.direction = "left"

def moveright():
    if snake.direction != "left":
        snake.direction = "right"

def moveup():
    if snake.direction != "down":
        snake.direction = "up"

def movedown():
    if snake.direction != "up":
        snake.direction = "down"

def move():
    if snake.direction == "up":
        coord_y = snake.ycor()
        snake.sety(coord_y+20)

    if snake.direction == "down":
        coord_y = snake.ycor()
        snake.sety(coord_y-20)

    if snake.direction == "right":
        coord_x = snake.xcor()
        snake.setx(coord_x+20)

    if snake.direction == "left":
        coord_x = snake.xcor()
        snake.setx(coord_x-20)

screen.listen()
screen.onkeypress(moveleft, 'a')
screen.onkeypress(moveright, 'd')
screen.onkeypress(moveup, 'w')
screen.onkeypress(movedown, 's')

segments = []

while True:
    screen.update()
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "Stop"
        snake.shape("square")
        snake.color("blue")

        for segment in segments:
            segment.goto(1000, 1000)
            segments.clear()
            player_score = 0
            delay_time = 0.2
            sc.clear()
            sc.write("Player_score: {} high_score: {}".format(player_score, high_score), align="center", font=("Arial", 24, "normal"))

        if snake.distanse(snake_food) < 20:
            coord_x = random.randint(-270, 270)
            coord_y = random.randint(-270, 270)
            snake_food.goto(coord_x, coord_y)

            add_segment = turtle.Turtle()
            add_segment.speed(0)
            add_segment.shape("square")
            add_segment.color("white")
            add_segment.penup()
            segments.append(add_segment)
            delay_time -= 0.001
            player_score += 10

            if player_score > high_score:
                high_score = player_score
                sc.clear()
                sc.write("Player_score: {} high_score: {}".format(player_score, high_score), align="center", font=("Arial", 24, "normal"))

    for i in range(len(segments)-1, 0, -1):
        coord_x = snake.xcor()
        coord_y = snake.ycor()
        segments[0].goto(coord_x, coord_y)
    move()

    for segment in segments:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"
            snake.color('white')
            snake.shape('square')

            for segment in segments:
                segment.goto(1000, 1000)
                segment.clear()
                player_score = 0
                delay_time = 0.2
                sc.clear()
                sc.write("Player_score: {} high_score: {}".format(player_score, high_score), align="center", font=("Arial", 24, "normal"))

            time.sleep(delay_time)

turtle.mainloop()