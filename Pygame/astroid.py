import play
from play import db

enemies = []
gameOver = False
score = 0
spawn_interval = 1

try:
    db.get_data("highscore")
except:
    db.set_data("highscore", 0)


player = play.new_circle(
    color="black",
    x=0,
    y=0,
    radius=10
)

score_text = play.new_text(
    words=str(score),
    x=0,
    y=play.screen.top-50
)

end_text = play.new_text(
    words="Je score was:",
    x=0,
    y=100
)
end_text.hide()

highscore_text = play.new_text(
    words="De vorige highscore was " + str(db.get_data("highscore")),
    x=0,
    y=-100,
    font_size=24
)
highscore_text.hide()

restart_text = play.new_text(
    words="Klik op het scherm om opniew te beginnen",
    x=0,
    y=-150,
    font_size=24
)
restart_text.hide()

@play.repeat_forever
def move_player():
    player.x = play.mouse.x
    player.y = play.mouse.y

@play.repeat_forever
def move_enemies():
    global score
    if not gameOver:
        for enemy in enemies:
            enemy.x += 8
            if enemy.y > play.screen.top or enemy.y < play.screen.bottom or enemy.x > play.screen.right or enemy.x < play.screen.left:
                enemies.remove(enemy)
                enemy.remove()
                score += 1
                score_text.words = str(score)

@play.repeat_forever
async def spawn_enemy():
    global spawn_interval
    if not gameOver:
        if spawn_interval < 0.05: spawn_interval = 0.05
        new_enemy = play.new_box(
            color="black",
            x=play.screen.left,
            y=play.random_number(play.screen.top, play.screen.bottom),
            height=35,
            width=35,
            angle=45
        )
        enemies.append(new_enemy)
        await play.timer(seconds=spawn_interval)
        spawn_interval -= 0.05

@play.repeat_forever
def collide():
    global gameOver
    for enemy in enemies:
        if player.is_touching(enemy):
            gameOver = True
            remove_all_enemies()
            show_game_over_texts()
            handle_highscore()

def remove_all_enemies():
    for enemy in enemies:
        enemy.remove()

def show_game_over_texts():
    end_text.show()
    restart_text.show()
    highscore_text.show()
    score_text.y = 0

def hide_game_over_texts():
    end_text.hide()
    restart_text.hide()
    highscore_text.hide()
    score_text.y = play.screen.top-50

def handle_highscore():
    high_score = db.get_data("highscore")
    highscore_text.words = "De vorige highscore was " + str(high_score)
    if score > high_score:
        db.set_data("highscore", score)

@play.when_mouse_clicked
def restart_game():
    global gameOver, score, spawn_interval, enemies
    if gameOver:
        gameOver = False
        hide_game_over_texts()
        score = 0
        spawn_interval = 1
        score_text.words = str(score)
        enemies = []

play.start_program()