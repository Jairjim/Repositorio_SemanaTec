"""Snake, classic arcade game.
Exercises
1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *
import turtle
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
aid = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

# def inside(head):
#     "Return True if head inside boundaries."
#     return -250 < head.x < 250 and -250 < head.y < 250


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    
    if(head.x >= 250):
        change(0, 5)
            
    elif(head.x <= -200):
        change(0, -5)    
    
    elif(head.y >= 200):
        change(-5,0)
            
    elif(head.y <= -200):
        change(5, 0)
        
    snake.append(head)
            

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 10, 'black')

    square(food.x, food.y, 5, 'green')
    update()
    ontimer(move, 100) 
        

print('1.- Velocidad Baja')
print('2.- Velocidad Media')
print('3.- Velocidad Alta')
select = int(input('Elige su velocidad(1/2/3): '))

if(select == 1):
    setup(1000, 1000, 0, 0)
    hideturtle()
    tracer(False)
    listen()
    velocidad = int(4)
    onkey(lambda: change(velocidad, 0), 'Right')
    onkey(lambda: change(-velocidad, 0), 'Left')
    onkey(lambda: change(0, velocidad), 'Up')
    onkey(lambda: change(0, -velocidad), 'Down')
    move()

elif(select == 2):
    setup(1000, 1000, 0, 0)
    hideturtle()
    tracer(False)
    listen()
    velocidad = int(6)
    onkey(lambda: change(velocidad, 0), 'Right')
    onkey(lambda: change(-velocidad, 0), 'Left')
    onkey(lambda: change(0, velocidad), 'Up')
    onkey(lambda: change(0, -velocidad), 'Down')
    move()

elif(select == 3):
    setup(1000, 1000, 0, 0)
    hideturtle()
    tracer(False)
    listen()
    velocidad = int(8)
    onkey(lambda: change(velocidad, 0), 'Right')
    onkey(lambda: change(-velocidad, 0), 'Left')
    onkey(lambda: change(0, velocidad), 'Up')
    onkey(lambda: change(0, -velocidad), 'Down')
    move()
done()