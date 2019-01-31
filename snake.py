'''
Author: <Ali Kaif>
Date: <February 2nd, 2018>
Class: ISTA 130
Section Leader: <your section leader>

Description: Snake Program
<This program is designed to use the turtle methods to draw
out a snake based on functions designed to draw polygons>
'''

import turtle


def triangle(animal, length):
    animal.left(90)
    animal.forward(length)
    animal.left(120)
    animal.forward(length)
    animal.right(240)
    animal.forward(length)
    return None
   

def square(animal, length):
    animal.forward(length)
    animal.left(90)
    animal.forward(length)
    animal.left(90)
    animal.forward(length)
    animal.left(90)
    animal.forward(length)
    return None

def pentagon(animal, length):
    animal.forward(length)
    animal.left(72)
    animal.forward(length)
    animal.left(72)
    animal.forward(length)
    animal.left(72)
    animal.forward(length)
    animal.left(72)
    animal.forward(length)
    animal.left(72)
    return None


def hexagon(animal, length):
    animal.forward(length)
    animal.left(60)
    animal.forward(length)
    animal.left(60)
    animal.forward(length)
    animal.left(60)
    animal.forward(length)
    animal.left(60)
    animal.forward(length)
    animal.left(60)
    animal.forward(length)
    return None

def jump(animal, distance):
    art_turtle.penup()
    art_turtle.fd(distance)
    art_turtle.pendown()
    
  
    


#==========================================================
def main():
    animal = turtle.Turtle()
    '''
    The main function contains all the functions for drawing the geometric polygon shapes
    that when put in the correct order, should be able to replicate a snake drawing
    '''
    #Set's up initial settings for drawing the picture
    animal.pensize(10)
    animal.speed(0)
    

    animal.pencolor("red")
    triangle(animal, 100)
    animal.left(30)

    animal.pencolor('orange')
    square(animal, 100)
    
    animal.left(90)
    animal.forward(100)
    animal.right(30)

    animal.pencolor('yellow')
    hexagon(animal, 100)
    animal.left(30)

    animal.pencolor('lightgreen')
    triangle(animal, 100)
    animal.left(120)
    animal.forward(100)
    animal.right(150)
    triangle(animal, 100)

    animal.forward(100)
    animal.left(120)
    

    animal.penup()
    animal.forward(200)
    animal.pendown()

    animal.pencolor('blue')
    hexagon(animal, 100)
    animal.left(30)
    triangle(animal, 100)
    animal.left(120)
    animal.forward(100)
    animal.right(150)
    triangle(animal, 100)

    animal.left(120)
    animal.forward(100)
    animal.left(10)
    animal.pencolor('purple')

    pentagon(animal, 100)
    
    
    

    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
