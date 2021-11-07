import turtle 
s =turtle.Turtle()
s.speed(0)
s.screen.bgcolor("yellow")
s.pencolor("green")
a=0
b=0
s.penup()
s.goto(0,200)#optional no need but it make it to start from centre
s.pendown()
while True:
	s.fd(a)
	s.rt(b)
	a+=3
	b+=1
	if b==200:
	    break
	s.hideturtle()
turtle.done()