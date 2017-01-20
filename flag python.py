import turtle      
from tkinter import *
import time

#starting with defining the functions that are supposed to show the flags later

#belgium - gets its own function because it is going to be used more thanc once
def belgiumflag():	
	belgium = turtle.Turtle()
	belgium.speed(10)
	belgium.color("black")
	belgium.up()
	belgium.goto(100,200)
	belgium.right(90)
	belgium.down()
	belgium.pensize(50)
	belgium.forward(150)
	belgium.up()
	belgium.goto(150,200)
	belgium.color("gold")
	belgium.down()
	belgium.forward(150)
	belgium.up()
	belgium.goto(200,200)
	belgium.color("red")
	belgium.down()
	belgium.forward(150)

#southafrica - gets its own function because it is going to be used more thanc once
def southafriflag():
	wn = turtle.Screen()
	southafri = turtle.Turtle()
	southafri.speed(10)
	southafri.pensize(100)
	southafri.up()
	southafri.goto(50,200)
	southafri.color("red")
	southafri.down()
	southafri.goto(250,200)
	southafri.color("blue")
	southafri.up()
	southafri.goto(250,100)
	southafri.down()
	southafri.goto(50,100)
	southafri.color("black")
	southafri.up()
	southafri.goto(60,150)
	southafri.shapesize(8)
	southafri.shape("circle")
	southafri.stamp()
	southafri.shapesize(1)
	southafri.up()
	southafri.color("yellow")
	southafri.pensize("20")
	southafri.goto(20,240)
	southafri.down()
	southafri.goto(100,150)
	southafri.goto(20,60)
	southafri.up()
	southafri.color("green")
	southafri.pensize("40")
	southafri.goto(60,240)
	southafri.down()
	southafri.goto(140,150)
	southafri.goto(60,60)
	southafri.up()
	southafri.goto(140,150)
	southafri.down()
	southafri.goto(270,150)
	southafri.up()
	southafri.color("white")
	southafri.pensize(20)
	southafri.goto(100,240)
	southafri.down()
	southafri.goto(160,170)
	southafri.goto(290,170)
	southafri.up()
	southafri.goto(100,60)
	southafri.down()
	southafri.goto(160,130)
	southafri.goto(290,130)

#danish

def danishflag():
	wn = turtle.Screen()     
	turtle.title("Flags of countries in which Danish is spoken")   
	title = turtle.Turtle()
	title.up()
	title.goto(-50,270)
	title.write("Danish", font=("Arial",20, "bold"))
	title.ht()
	denmark = turtle.Turtle()
	denmark.speed(10)
	denmark.goto(0,0)
	denmark.color("red")
	denmark.pensize(200)
	denmark.forward(150)
	denmark.color("white")
	denmark.pensize(40)
	denmark.up()
	denmark.goto(-80,0)
	denmark.down()
	denmark.forward(310)
	denmark.up()
	denmark.goto(0,80)
	denmark.down()
	denmark.goto(0,-80)

#dutch

def dutchflags():
	wn = turtle.Screen()
	turtle.title("Flags of countries in which Dutch is spoken")
	title = turtle.Turtle()
	title.up()
	title.goto(-50,270)
	title.write("Dutch", font=("Arial",20, "bold"))
	title.ht()	

	#holland
	holland = turtle.Turtle() 
	holland.speed(10)
	holland.color("red")
	holland.pensize(50)
	holland.goto(-200,0)
	holland.up()
	holland.goto(-200,-100)
	holland.color("blue")
	holland.down()
	holland.forward(200)

	#belgium
	belgiumflag()

#german

def germanflags():
	wn = turtle.Screen() 
	turtle.title("Flags of countries in which German is spoken")
	title = turtle.Turtle()
	title.up()
	title.goto(-50,270)
	title.write("German", font=("Arial",20, "bold"))
	title.ht()

	#germany
	germany = turtle.Turtle()      
	germany.speed(10)
	germany.up()
	germany.goto(80,0)
	germany.down()
	germany.color("black")
	germany.pensize(50)
	germany.forward(200)
	germany.up()
	germany.color("red")
	germany.goto(80,-50)
	germany.down()
	germany.forward(200)
	germany.color("gold")
	germany.up()
	germany.goto(80,-100)
	germany.down()
	germany.forward(200)

	#switzerland
	switzer = turtle.Turtle()
	switzer.speed(10)
	switzer.up()
	switzer.goto(-250,130)
	switzer.down()
	switzer.color ("red")
	switzer.pensize(200)
	switzer.forward(150)
	switzer.up()
	switzer.goto(-230,130)
	switzer.pensize(50)
	switzer.color("white")
	switzer.down()
	switzer.forward(120)
	switzer.up()
	switzer.goto(-170,190)
	switzer.down()
	switzer.right(90)
	switzer.forward(120)

	#austria
	austria = turtle.Turtle()
	austria.speed(10)   
	austria.up()
	austria.goto(-200,-120)
	austria.down()
	austria.color("red")
	austria.pensize(50)
	austria.forward(200)
	austria.up()
	austria.goto(-200,-20)
	austria.down()
	austria.forward(200)
	
	#belgium
	belgiumflag()

#english

def englishflags():
	wn = turtle.Screen()
	turtle.title("Flags of some countries in which English is spoken")
	title = turtle.Turtle()
	title.up()
	title.goto(-50,270)
	title.write("English (Some Examples)", font=("Arial",20, "bold"))
	title.ht()

	#uk
	uk = turtle.Turtle()
	uk.speed(10)
	uk.color("blue")
	uk.up()
	uk.goto(-230,100)
	uk.pensize(200)
	uk.down()
	uk.forward(150)
	uk.pensize(40)
	uk.goto(0,175)
	uk.color("white")
	uk.down()
	uk.goto(-310,10)
	uk.up()
	uk.goto(-310,190)
	uk.down()
	uk.goto(0,0)
	uk.up()
	uk.goto(-155,200)
	uk.down()
	uk.goto(-155,0)
	uk.up()
	uk.goto(-320,100)
	uk.down()
	uk.goto(40,100)
	uk.color("red")
	uk.pensize(20)
	uk.goto(-320,100)
	uk.up()
	uk.goto(-155,0)
	uk.down()
	uk.goto(-155,200)
	uk.up()
	uk.goto(20,175)
	uk.down()
	uk.goto(-310,10)
	uk.up()
	uk.goto(-310,190)
	uk.down()
	uk.goto(-20,0)

	#us
	us = turtle.Turtle()
	us.speed(10)
	us.color("red")
	us.pensize(10)
	us.up()
	us.forward(50)
	for i in range(11): 
		us.down()
		us.forward(250)
		us.up()
		us.right(90)
		us.forward(15)
		us.right(90)
		us.forward(250)
		us.left(180)
		us.down()
	us.up()
	us.forward(25)
	us.left(90)
	us.forward(90)
	us.right(90)
	us.down()
	us.color("blue")
	us.pensize(60)
	for i in range(4):
		us.forward(80)
		us.left(90)
		us.forward(50)
		us.left(90)

	#canada
	canada = turtle.Turtle()
	canada.speed(10)
	canada.color("red")
	canada.up()
	canada.goto(-230,-170)
	canada.pensize(200)
	canada.down()
	canada.forward(150)
	canada.up()
	canada.goto(-150,-70)
	canada.pensize(100)
	canada.left(90)
	canada.color("white")
	canada.down()
	canada.forward(-200)
	canada.up()
	canada.forward(100)
	canada.color("red")
	canada.shape("turtle")
	canada.shapesize(4)
	canada.stamp()

	#south africa
	southafriflag()

#swedish

def swedenflag():
	wn = turtle.Screen()   
	turtle.title("Flags of countries in which Swedish is spoken")  
	title = turtle.Turtle()
	title.up()
	title.goto(-50,270)
	title.write("Swedish", font=("Arial",20, "bold"))   
	title.ht()
	sweden = turtle.Turtle()    
	sweden.speed(10)  
	sweden.color("blue")
	sweden.pensize(200)
	sweden.forward(150)
	sweden.color("gold")
	sweden.pensize(40)
	sweden.up()
	sweden.goto(-80,0)
	sweden.down()
	sweden.forward(310)
	sweden.up()
	sweden.goto(0,80)
	sweden.down()
	sweden.goto(0,-80)

#norwegian

def norwayflag():
	wn = turtle.Screen()
	turtle.title("Flags of countries in which Norwegian is spoken")
	title = turtle.Turtle()
	title.up()
	title.goto(-50,270)
	title.write("Norwegian", font=("Arial",20, "bold"))
	title.ht()
	norway = turtle.Turtle()      
	norway.speed(10)
	norway.color("red")
	norway.pensize(200)
	norway.forward(150)
	norway.color("white")
	norway.up()
	norway.pensize(40)
	norway.goto(0,80)
	norway.down()
	norway.goto(0,-80)
	norway.up()
	norway.goto(-80,0)
	norway.down()
	norway.forward(310)
	norway.color("blue")
	norway.pensize(20)
	norway.forward(-310)
	norway.up()
	norway.goto(0,80)
	norway.down()
	norway.goto(0,-80)

#icelandic

def icelandflag():
	wn = turtle.Screen() 
	turtle.title("Flags of countries in which Icelandic is spoken")
	title = turtle.Turtle()
	title.up()
	title.goto(-50,270)
	title.write("Icelandic", font=("Arial",20, "bold"))
	title.ht()
	iceland = turtle.Turtle()
	iceland.speed(10)
	iceland.color("blue")
	iceland.pensize(200)
	iceland.forward(150)
	iceland.color("white")
	iceland.up()
	iceland.pensize(40)
	iceland.goto(0,80)
	iceland.down()
	iceland.goto(0,-80)
	iceland.up()
	iceland.goto(-80,0)
	iceland.down()
	iceland.forward(310)
	iceland.color("red")
	iceland.pensize(20)
	iceland.forward(-310)
	iceland.up()
	iceland.goto(0,80)
	iceland.down()
	iceland.goto(0,-80)

#afrikaans

def afrikaansflag():
	wn = turtle.Screen()
	turtle.title("Flags of countries in which Afrikaans is spoken")
	title = turtle.Turtle()
	title.up()
	title.goto(-50,270)
	title.write("Afrikaans", font=("Arial",20, "bold"))
	title.ht()
	
	#namibia
	nami = turtle.Turtle()
	nami.speed(10)
	nami.up()
	nami.goto(-250,-200)
	nami.color("green")
	nami.down()
	nami.begin_fill()
	nami.goto(-10,-200)
	nami.goto(-10,-50)
	nami.goto(-250,-200)
	nami.end_fill()
	nami.up()
	nami.color("blue")
	nami.goto(-250,-150)
	nami.down()
	nami.begin_fill()
	nami.goto(-250,-10)
	nami.goto(-10,-10)
	nami.goto(-250,-150)
	nami.end_fill()
	nami.color("red")
	nami.pensize(20)
	nami.up()
	nami.goto(-250,-175)
	nami.down()
	nami.goto(-10,-30)
	nami.up()
	nami.goto(-200,-50)
	nami.shape("turtle")
	nami.color("gold")
	nami.left(90)
	nami.stamp()

	#south africa
	southafriflag()

# defining a function for a window that is supposed to open for a false entry

def falseentry():
	wn = turtle.Screen()
	wn.bgcolor("red")
	false = turtle.Turtle()
	false.ht()
	false.up()
	false.forward(-120)      
	false.write("False Entry!", font=("Arial", 33, "bold"))
	time.sleep(3)

#listing the expressions for family members to each language that is represented as flags as well

danishfam = ["moder", "far", "bedstemor", "bedstefar", "onkel", "tante"
"datter", "søn", "søster", "bror", "nevø", "niece", "barnebarn", "barnebarn"
 "fætter", "fætter"]
dutchfam = ["moeder", "vader", "grootmoeder", "opa", "oom", "tante"
"dochter", "zoon", "zuster", "broer", "neef", "nicht", "kleinzoon", 
"kleindochter", "neef", "neef"]
germanfam = ["Mutter", "Vater", "Großmutter", "Großvater", "Onkel", "Tante",
"Tochter", "Sohn", "Schwester", "Bruder", "Neffe", "Nichte", "Enkel", "Enkelin",
 "Cousin", "Cousine"]
englishfam = ["mother", "father", "grandmother", "grandfather", "uncle", "aunt"
"daughter", "son", "sister", "brother", "nephew", "niece", "grandson", 
"granddaughter", "cousin, cousin"]
swedishfam = ["mamma", "fader", "mormor", "farfar", "farbror", "moster"
"dotter", "son", "syster", "broder", "brorson", "niece", "barnbarn", "barnbarn"
 "kusin", "kusin"]
norfam = ["mother", "far", "bestemor", "bestefar", "onkel", "tante"
"daughter", "sønn", "søster", "bror", "nevø", "niese", "barnebarn", 
"barnebarn", "fetter", "fetter"]
icefam = ["móðir", "faðir", "amma", "Afi", "frændi", "frænka", "dóttir",
 "sonur", "systir", "bróðir", "frændi", "frænka", "barnabarn", "barnabarn"
 "cousin," "frændi"]
afrikaansfam = ["moeder", "vader", "ouma", "oupa", "oom", "tannie", "dogter",
 "seun", "suster", "broer", "neef", "niggie", "kleinseun", "kleindogter"
 "neef," "neef"]

#list to which the word typed in by the user is going to be added

insert_word = []

#defining a function for a user interface, pattern for interface found on http://www.python-course.eu/tkinter_entry_widgets.php

def show_entry_fields():
   insert_word.append(e1.get())

master = Tk()
Label(master, text="Type in an expression for a family member in German, "
	"Danish, Dutch, English, Swedish, Norwegian or Icelandic!").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)

Button(master, text='1. Step: Submit', command=show_entry_fields).grid(row=3,
 column=1, sticky=W, pady=4)
Button(master, text='2. Step: Show flag', command=master.quit).grid(row=3,
 column=0, sticky=W, pady=4)

mainloop()

#defining a final function to connect flag functions with language lists
	
def langvisual():
	for i in insert_word:
		languagefound = False
		if i in germanfam:
			languagefound = True
			germanflags()
			time.sleep(3)
		if i in danishfam:
			languagefound = True
			turtle.clearscreen()
			danishflag()
			time.sleep(3)
		if i in dutchfam:
			languagefound = True
			turtle.clearscreen()
			dutchflags()
			time.sleep(3)
		if i in englishfam:
			languagefound = True
			turtle.clearscreen()
			englishflags()
			time.sleep(3)
		if i in swedishfam:
			languagefound = True
			turtle.clearscreen()
			swedenflag()
			time.sleep(3)
		if i in norfam:
			languagefound = True
			turtle.clearscreen()
			norwayflag()
			time.sleep(3)
		if i in icefam:
			languagefound = True
			turtle.clearscreen()
			icelandflag()
			time.sleep(3)
		if i in afrikaansfam:
			languagefound = True
			turtle.clearscreen()
			afrikaansflag()
			time.sleep(3)

		if languagefound != True:
			falseentry()

langvisual()


