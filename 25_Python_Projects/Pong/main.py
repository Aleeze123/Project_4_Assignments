import turtle
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(stretch_wid=6, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("red")
paddle2.shapesize(stretch_wid=6, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

score1 = 0
score2 = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

def paddle1_up():
    y = paddle1.ycor()
    if y < 250:
        y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    if y > -240:
        y -= 20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    if y < 250:
        y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    if y > -240:
        y -= 20
    paddle2.sety(y)

wn.listen()
wn.onkey(paddle1_up, "w")
wn.onkey(paddle1_down, "s")
wn.onkey(paddle2_up, "Up")
wn.onkey(paddle2_down, "Down")

def game_over(winner):
    score_display.clear()
    score_display.goto(0, 0)
    score_display.write(f"Game Over! {winner} Wins!", align="center", font=("Courier", 24, "normal"))
    turtle.done()

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score_display.clear()
        score_display.goto(0, 260)
        score_display.write(f"Player 1: {score1}  Player 2: {score2}", align="center", font=("Courier", 24, "normal"))
        if score1 == 5:
            game_over("Player 1")
            break

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score_display.clear()
        score_display.goto(0, 260)
        score_display.write(f"Player 1: {score1}  Player 2: {score2}", align="center", font=("Courier", 24, "normal"))
        if score2 == 5:
            game_over("Player 2")
            break

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
        ball.color("red")
        ball.dx *= -1

    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
        ball.color("blue")
        ball.dx *= -1
