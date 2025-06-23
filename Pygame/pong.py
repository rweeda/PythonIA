import play

score_1 = 0
score_2 = 0

tekst_1 = play.new_text(
    words=str(score_1),
    x=50,
    y=250
)

tekst_2 = play.new_text(
    words=str(score_2),
    x=-50,
    y=250
)

paddle_1 = play.new_box(
    color='red',
    x=380,
    y=0,
    width=20,
    height=100,
)

paddle_2 = play.new_box(
    color='blue',
    x=-380,
    y=0,
    width=20,
    height=100,
)

ball = play.new_circle(
    color='white',
    x=0,
    y=0,
    radius=10,
    border_color="black",
    border_width=3
)

ball.start_physics(
    x_speed = 20,
    y_speed = play.random_number(-15, 15) * 1.5,
    obeys_gravity=False
)

@play.when_key_pressed('up')
def beweeg_omhoog_up():
    if paddle_1.top < play.screen.top:
        paddle_1.y += 10

@play.when_key_pressed('down')
def beweeg_omlaag_up():
    if paddle_1.bottom > play.screen.bottom:
        paddle_1.y -= 10

@play.when_key_pressed('w')
def beweeg_omhoog_w():
    if paddle_2.top < play.screen.top:
        paddle_2.y += 10

@play.when_key_pressed('s')
def beweeg_omlaag_s():
    if paddle_2.bottom > play.screen.bottom:
        paddle_2.y -= 10

@ball.when_touching(paddle_1)
def botsing_1():
    ball.physics.x_speed = -20
    ball.physics.y_speed += play.random_number(-5,5)

@ball.when_touching(paddle_2)
def botsing_2():
    ball.physics.x_speed = 20
    ball.physics.y_speed += play.random_number(-5,5)

@play.repeat_forever
def botsing():
    global score_1
    global score_2
    if ball.right >= play.screen.right - 5:
        resetBal()
        score_2 += 1
        tekst_2.words = str(score_2)

    if ball.left <= play.screen.left + 5:
        resetBal()
        score_1 += 1
        tekst_1.words = str(score_1)

def resetBal():
    ball.x = 0
    ball.y = 0
    ball.physics.x_speed = 20
    ball.physics.y_speed = play.random_number(-15, 15) * 1.5

play.start_program()