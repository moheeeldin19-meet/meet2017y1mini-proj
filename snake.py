import turtle
import random

turtle.tracer(1,0)

moo=turtle.clone()
moo.penup()
moo.goto(400,-250)
moo.pendown()
moo.goto(400,250)
moo.goto(-400,250)
moo.goto(-400,-250)
moo.goto(400,-250)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE=20
START_LENGTH=2

pos_list=[]
stamp_list = []
food_pos =[]
food_stamps =[]


snake =turtle.clone()
snake.shape("square")
turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE
    

    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(snake.pos())
    pizza=snake.stamp()
    stamp_list.append(pizza)

UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=200
SPACEBAR="spacebar"

UP=0
LEFT=2
DOWN=1
RIGHT=3

direction =UP
UP_EDGE=240
DOWN_EDGE=-240
RIGHT_EDGE=400
LEFT_EDGE=-400
def up():
    global direction
    direction=UP
     #<----REMEMBER ME LATERR!!!!!!!!
    print("you pressed the up key")
def down():
    global direction
    direction=DOWN
    print("you pressed the down key")

def left():
    global direction
    direction = LEFT
    print("you pressed the left key")

def right():
    global direction
    direction=RIGHT
    print("you pressed the right key")
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.listen()
c=0
turtle.goto(-378,230)
def move_snake():
    my_pos = snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    if direction ==RIGHT:
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print("you moved right")
    elif direction ==LEFT:
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
        print("you moved left")
    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print("you moved up")
    elif direction==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)
    global food_stamps,food_pos,c
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("you have eaten the food")
        make_food()
        c=c+1
        
        turtle.write(c)
    
        
    else:
            #HINT: this if statment may be useful for part 8
        old_stamp =stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]
    if new_x_pos>=RIGHT_EDGE:
        print("you hit the right edge! GAME OVER!")
        quit()
    if new_x_pos<=LEFT_EDGE:
        print("you hit the left edge! GAME OVER!")
        quit()
    if new_y_pos<=DOWN_EDGE:
        print("you hit the down edge ! GAME OVER!")
        quit()
    if new_y_pos>=UP_EDGE:
        print("you hit the up edge! GAME OVER!")
        quit()
    if pos_list[-1]in pos_list[0:-1]:
        print("you ate yourself !!GAME OVER!!")
        quit()
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()
turtle.register_shape("trash.gif")
food=turtle.clone()
food.shape("trash.gif")

food_pos=[]
food_stamps=[]
food.hideturtle()
##def food_places(start,end):
##    food.goto(start,end)
##    aliens=food.stamp()
##    food_stamps.append(aliens)
##food_places(100,100)
##food_places(-100,100)
##food_places(-100,-100)
##food_places(100,-100)

def make_food():
    min_x=-int(SIZE_X/2.5/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2.5/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2.5/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2.5/SQUARE_SIZE)+1
    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    aliens=food.stamp()
    food_stamps.append(aliens)
make_food()

