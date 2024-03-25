import turtle

"""
Global constants
"""
# screen dimensions, borders
screen_width = 800
screen_height = 500
right_edge = screen_width / 2
left_edge = -right_edge
top_edge = screen_height / 2
bottom_edge = -top_edge
middle = 0

# font
font = ("Courier", 24, "normal")

"""
Game State
"""

score_right = 0
score_left = 0
scores = [score_left, score_right]
winning_score = 7

"""
Window
"""
window = turtle.Screen()
window.title("Knight's Pong")
window.bgcolor("black")
window.setup(width=screen_width, height=screen_height)
window.tracer(0)  # control screen updates with game loop

""" 
Ball
"""
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.shapesize(1)
ball.penup()
speed = 0.05
horizontal = speed
vertical = speed

""" 
Left Paddle
"""
left_p = turtle.Turtle()
left_p.shape('square')
left_p.color('white')
left_p.shapesize(8)
left_p.penup()
left_p.goto(430, 0)
left_p.right(90)

""" 
Right Paddle
"""
right_p = turtle.Turtle()
right_p.shape('square')
right_p.color('white')
right_p.shapesize(8)
right_p.penup()
right_p.goto(-430, 0)
right_p.right(90)


""" 
Scoreboard
"""
# add code here to initialize the scoreboard
score_board = turtle.Turtle()
score_board.color("white")
score_board.hideturtle()
score_board.penup()

"""
Message 
"""
message = turtle.Turtle()
message.color("white")
message.hideturtle()

"""
Helper Functions
"""
def up():
    if left_p.ycor() <= 200:
        left_p.forward(-8)
def down():
    if left_p.ycor() >= -200:
        left_p.forward(8)
def up2():
    if right_p.ycor() <= 200:
        right_p.forward(-8)
def down2():
    if right_p.ycor() >= -200:
        right_p.forward(8)

turtle.listen()
turtle.onkey(fun=up, key='Up')
turtle.onkey(fun=down, key='Down')
turtle.onkey(fun=up2, key='w')
turtle.onkey(fun=down2, key='s')

def start_game():
    message.clear()  # clear start message
    play_pong(horizontal, vertical, score_left, score_right)


def game_over(score_left, score_right):
    message.write("GAME OVER", align="center", font=font)
    message.sety(message.ycor() - 50)
    message.write(
        "Lefty wins!" if score_left > score_right else "Righty wins!",
        align="center",
        font=font,
    )


"""
Main Game Loop
"""


def play_pong(horizontal, vertical, score_left, score_right):
    # prints score
    speed = 0.05
    scores = [score_left, score_right]
    score_board.sety(score_board.ycor() + 200)    
    score_board.write(str(scores), align='center', font=font)

    while True:
        window.update()
        ball.forward(horizontal)
        ball.left(90)
        ball.forward(vertical)
        ball.right(90)
        # if the ball hits the top or bottom
        if ball.ycor() >= 245:
            vertical = -1 * speed
        if ball.ycor() <= -245:
            vertical = speed

        # if the all hits the paddles
        if ball.ycor() >= left_p.ycor() - 64 and ball.ycor() <= left_p.ycor() + 64 and ball.xcor() >= 345:
            speed *= 1.1
            horizontal = -1 * speed
        elif ball.ycor() >= right_p.ycor() - 64 and ball.ycor() <= right_p.ycor() + 64 and ball.xcor() <= -345:
            speed *= 1.1
            horizontal = speed

        # if the ball goes out
        if ball.xcor() >= 348:
            score_left += 1
            scores = [score_left, score_right]
            score_board.clear()
            score_board.write(str(scores), align='center', font=font)
            ball.goto(0,0)
            horizontal = 0.05
            vertical = 0.05
            speed = 0.05
        elif ball.xcor() <= -348:
            score_right += 1
            scores = [score_left, score_right]
            score_board.clear()
            score_board.write(str(scores), align='center', font=font)
            ball.goto(0,0)
            speed = 0.05
            horizontal = -0.05
            vertical = 0.05
    # main game loop

        if max(score_left, score_right) < winning_score:
            pass
    #        window.ontimer(play_pong(horizontal, vertical), 1000 // 60)
        else:
            game_over(score_left, score_right)
            break


"""
Event listeners
"""
window.onkey(start_game, "space")
window.listen()


message.write("Press space to start", align="center", font=font)
turtle.mainloop()
