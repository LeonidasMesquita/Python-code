from turtle import *
import turtle

t = turtle.Turtle()
def star():
      
       t.fillcolor('black')
       t.begin_fill()
       for i in range(5):
           t.forward(30)
           t.right(144)
       t.end_fill()
       
def draw_circle(color, radius, x, y):
  t.penup()
  t.fillcolor(color,)
  t.goto(x,y)
  
  t.begin_fill()
  t.circle(radius)
  t.end_fill()
  t.pendown()

t = turtle.Turtle()
t.color('red', 'blue')

def dragon():
    t.penup()
    draw_circle("#ffb800",70, -18, -110)
    draw_circle("#ff9a00", 65, -21, -105)
    draw_circle("#fbc12c",40,-30,-65)
    t.pendown()
    t.color('#fbc12c', 'blue')
    t.goto(-30, -33)
    t.pendown()
    star()
    t.goto(10, -33)
    t.pendown()
    star()
    t.pendown()
    t.goto(-70, -33)
    star()
    
    t.pendown()
    t.goto(-50, -63)
    star()
    t.pendown()
    t.goto(-10, -63)
    star()
    
    t.pendown()
    t.goto(-50, -3)
    star()
    t.pendown()
    t.goto(-10, -3)
    star()

    draw_circle("#ffb800",70, -148, -110)
    draw_circle("#ff9a00", 65, -151, -105)
    draw_circle("#fbc12c",40,-160,-65)
    
    t.pendown()
    t.goto(-190, -20)
    star()
    t.pendown()
    t.goto(-130, -20)
    star()

    t.pendown()
    t.goto(-190, -60)
    star()
    t.pendown()
    t.goto(-130, -60)
    star()


    draw_circle("#ffb800",70, 100, -110)
    draw_circle("#ff9a00", 65,98, -105)
    draw_circle("#fbc12c",40,100,-65)

    t.pendown()
    t.goto(85, -20)
    star()
    t.pendown()
    t.goto(60, -50)
    star()
    t.pendown()
    t.goto(110, -50)
    star()  
    turtle.hideturtle()

    draw_circle("#ffb800",70, -70, 5)
    draw_circle("#ff9a00", 65, -70, 10)
    draw_circle("#fbc12c",40,-85,55)
    
    t.pendown()
    t.goto(-85, 80)
    star()  
    turtle.hideturtle()

    draw_circle("#ffb800",70, 70, 5)
    draw_circle("#ff9a00", 65, 70, 10)
    draw_circle("#fbc12c",40,65,55)

    t.pendown()
    t.goto(30, 90)
    star()
    t.pendown()
    t.goto(80, 60)
    star()

    draw_circle("#ffb800",70, -90, -220)
    draw_circle("#ff9a00", 65, -95, -215)
    draw_circle("#fbc12c",40,-100,-170)

    t.goto(-105, -117)
    t.pendown()
    star()
    t.pendown()
 
    t.goto(-145, -137)
    t.pendown()
    star()

    t.goto(-65, -137)
    t.pendown()
    star()

    t.goto(-125, -173)
    t.pendown()
    star()

    t.goto(-80, -173)
    t.pendown()
    star()

    draw_circle("#ffb800",70, 60, -220)
    draw_circle("#ff9a00", 65, 55, -215)
    draw_circle("#fbc12c",40,50,-170)

    t.goto(45, -112)
    t.pendown()
    star()
    t.pendown()
 
    t.goto(5, -137)
    t.pendown()
    star()

    t.goto(80, -137)
    t.pendown()
    star()

    t.goto(65, -173)
    t.pendown()
    star()

    t.goto(20, -173)
    t.pendown()
    star()

    t.goto(45, -143)
    t.pendown()
    star()
    

if __name__ == '__main__':
    screensize(8000, 6000, "#f0f0f0")
    turtle.Screen().bgcolor("#dceaf6")
  
    pensize(3)
    speed(9)
    dragon()