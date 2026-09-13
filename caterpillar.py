import random
import turtle as t

t.bgcolor('yellow')

caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

game_started = False
game_active = False
text_turtle = t.Turtle()
text_turtle.penup()
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = caterpillar.pos()
    outside = \
        x < left_wall or \
        x > right_wall or \
        y < bottom_wall or \
        y > top_wall
    return outside

def game_over():
    global game_active
    game_active = False
    caterpillar.color('yellow')
    leaf.color('yellow')
    text_turtle.penup()
    text_turtle.setpos(0, 0)
    text_turtle.write('GAME OVER!\nPress SPACE to play again', align='center', font=('Arial', 30, 'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))

def place_leaf():
    leaf.hideturtle()
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.color('green')
    leaf.showturtle()

def game_loop(caterpillar_speed, caterpillar_length, score):
    global game_active

    if not game_active:
        return

    caterpillar.forward(caterpillar_speed)

    if caterpillar.distance(leaf) < 20:
        place_leaf()
        caterpillar_length = caterpillar_length + 1
        caterpillar.shapesize(1, caterpillar_length, 1)
        caterpillar_speed = caterpillar_speed + 1
        score = score + 10
        display_score(score)

    if outside_window():
        game_over()
        return

    t.ontimer(lambda: game_loop(caterpillar_speed, caterpillar_length, score), 50)

def reset_game():
    global game_started, game_active

    # Reset turtles without clearing the screen
    caterpillar.hideturtle()
    caterpillar.setpos(0, 0)
    caterpillar.setheading(0)
    caterpillar.color('red')

    leaf.hideturtle()
    leaf.setpos(0,0)
    leaf.color('green')

    # Clear text elements
    text_turtle.clear()
    score_turtle.clear()

    text_turtle.penup()
    text_turtle.setpos(0, 0)
    text_turtle.write('Press SPACE to start', align='center', font=('Arial', 16, 'bold'))
    text_turtle.hideturtle()

    game_started = False
    game_active = False

def start_game():
    global game_started, game_active

    if game_started:
        return

    game_started = True
    game_active = True

    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    game_loop(caterpillar_speed, caterpillar_length, score)

def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

def handle_space():
    global game_active
    if not game_active:
        reset_game()
        start_game()
    else:
        start_game()

# Show initial start message
text_turtle.penup()
text_turtle.setpos(0, 0)
text_turtle.write('Press SPACE to start', align='center', font=('Arial', 16, 'bold'))
text_turtle.hideturtle()

t.onkey(handle_space, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_right, 'Right')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.listen()
t.mainloop()
