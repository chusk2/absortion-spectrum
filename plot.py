from turtle import Turtle, Screen
scr = Screen()
bars = []
sodium_lengths = [330.3, 589.6, 819.5]
potassium_lengths = [344.7, 404.7, 693.9, 696.4, 769.7]
x_origin = -50
y_origin = 0
x_axis = Turtle()
x_axis.penup()
x_axis.goto(x_origin, y_origin + 20)
x_axis.write(str('Long. onda, nm'), move=False, align='left', font=('Arial', 8, 'normal'))

sodio = Turtle()
sodio.color('blue')
sodio.penup()
sodio.goto(x_origin, y_origin - 40)
sodio.pendown()
sodio.write(str('Sodio (Na), azul'), move=False, align='left', font=('Arial', 8, 'normal'))
sodio.hideturtle()
potasio = Turtle()
potasio.color('red')
potasio.penup()
potasio.goto(x_origin, y_origin - 60)
potasio.write(str('Potasio (Ka), rojo'), move=False, align='left', font=('Arial', 8, 'normal'))
potasio.hideturtle()

x_axis.goto(x_origin, y_origin)
x_axis.pendown()
x_axis.goto(700, 0)
x_axis.penup()
x_axis.hideturtle()
bar_width = 2

for i in range(len(sodium_lengths)):
    xpos = sodium_lengths[i] - 200  # reduce x axis scale
    bars.append(Turtle())
    t = bars[i]  # current turtle
    t.color('blue')
    t.hideturtle()
    t.penup()
    t.goto(xpos-5, -20)
    t.write(str(xpos+200), move=False, align='left', font = ('Arial', 8, 'normal'))
    t.fillcolor('blue')
    t.begin_fill()
    t.goto(xpos, 0)
    t.goto(xpos, 100)
    t.goto(xpos + bar_width, 100)
    t.goto(xpos + bar_width, 0)
    t.goto(xpos, 0)
    t.end_fill()

for i in range(len(potassium_lengths)):
    xpos = potassium_lengths[i] - 200   # reduce x axis scale
    bars.append(Turtle())
    t = bars[i]  # current turtle
    t.color('red')
    t.hideturtle()
    t.penup()
    y_pos = -40  # fix overlapped bars in 600 nm
    if i == 3:
        y_pos = -60
    t.goto(xpos-5, y_pos)
    t.write(str(xpos+200), move=False, align='left', font = ('Arial', 8, 'normal'))
    t.fillcolor('red')
    t.begin_fill()
    t.goto(xpos, 0)
    t.goto(xpos, 100)
    t.goto(xpos + bar_width, 100)
    t.goto(xpos + bar_width, 0)
    t.goto(xpos, 0)
    t.end_fill()
scr.exitonclick()



