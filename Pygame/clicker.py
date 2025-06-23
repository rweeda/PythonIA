import play

block = play.new_box(
    color="black",
    x=play.random_position().x,
    y=play.random_position().y,
    height=35,
    width=35
)

time = 5

time_text = play.new_text(
    words=str(time),
    x=0,
    y=200
)

score = 0

score_text = play.new_text(
    words="score: " + str(score),
    x=0,
    y=250,
    font_size=24
)

gameOver = False

@play.repeat_forever
async def timer():
    global time, gameOver
    if not gameOver:
        await play.timer(seconds=1)
        time -= 1
        time_text.words = str(time)

@play.repeat_forever
def checkGameState():
    global time, gameOver
    if time <= 0 and not gameOver:
        print("Game over")
        gameOver = True

@play.repeat_forever
def gameIsOver():
    if gameOver:
        score_text.font_size=36
        score_text.y=0
        time_text.hide()
        block.hide()

@block.when_clicked
def blockClicked():
    global score
    score += 1
    score_text.words = "score: " + str(score)
    random_pos = play.random_position()
    block.x=random_pos.x
    block.y=random_pos.y

play.start_program()