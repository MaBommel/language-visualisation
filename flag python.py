import turtle      
from tkinter import *
import time

def belgiumflag():										#This function will be needed fo the flagscreens for the languages German and Dutch
		belgium = turtle.Turtle()
		belgium.speed(10)
		belgium.color("black")
		belgium.up()
		belgium.forward(100)
		belgium.right(90)
		belgium.forward(-250)
		belgium.down()
		belgium.pensize(50)
		belgium.forward(150)
		belgium.up()
		belgium.left(90)
		belgium.forward(50)
		belgium.left(90)
		belgium.color("gold")
		belgium.down()
		belgium.forward(150)
		belgium.up()
		belgium.right(90)
		belgium.forward(50)
		belgium.right(90)
		belgium.color("red")
		belgium.down()
		belgium.forward(150)

#danish

def danishflag():
	wn = turtle.Screen()     
	turtle.title("Flags of countries in which Danish is spoken")   
	denmark = turtle.Turtle()      
	denmark.color("red")
	denmark.pensize(200)
	denmark.forward(150)
	denmark.color("white")
	denmark.pensize(40)
	denmark.forward(80)
	denmark.forward(-310)
	denmark.up()
	denmark.left(45)
	denmark.forward(120)
	denmark.down()
	denmark.right(135)
	denmark.forward(170)
	#wn.exitonclick()

#dutch

def dutchflags():
	wn = turtle.Screen()
	turtle.title("Flags of countries in which Dutch is spoken")
	#holland
	holland = turtle.Turtle() 
	holland.color("red")
	holland.pensize(50)
	holland.up()
	holland.forward(-250)
	holland.down()
	holland.forward(150)
	holland.right(90)
	holland.up()
	holland.forward(100)
	holland.right(90)
	holland.color("blue")
	holland.down()
	holland.forward(150)
	#belgium
	belgiumflag()
	#wn.exitonclick()

#german

def germanflags():
	wn = turtle.Screen() 
	turtle.title("Flags of countries in which German is spoken")
	#germany
	germany = turtle.Turtle()      
	germany.speed(10)
	germany.up()
	germany.forward(80)
	germany.down()
	germany.color("black")
	germany.pensize(50)
	germany.forward(200)
	germany.up()
	germany.color("red")
	germany.right(90)
	germany.forward(50)
	germany.right(90)
	germany.down()
	germany.forward(200)
	germany.color("gold")
	germany.up()
	germany.left(90)
	germany.forward(50)
	germany.left(90)
	germany.down()
	germany.forward(200)

	#switzerland
	
	switzer = turtle.Turtle()
	switzer.speed(10)
	switzer.up()
	switzer.forward(-250)
	switzer.left(90)
	switzer.forward(130)
	switzer.right(90)
	switzer.down()
	switzer.color ("red")
	switzer.pensize(200)
	switzer.forward(150)
	switzer.up()
	switzer.forward(-75)
	switzer.right(90)
	switzer.forward(-60)
	switzer.pensize(50)
	switzer.color("white")
	switzer.down()
	switzer.forward(120)
	switzer.up()
	switzer.right(135)
	switzer.forward(85)
	switzer.down()
	switzer.right(135)
	switzer.forward(120)
	#austria
	austria = turtle.Turtle()
	austria.speed(10)   
	austria.up()
	austria.forward(-200)
	austria.left(90)
	austria.forward(-120)
	austria.right(90)
	austria.down()
	austria.color("red")
	austria.pensize(50)
	austria.forward(200)
	austria.up()
	austria.right(90)
	austria.forward(50)
	austria.right(90)
	austria.forward(200)
	austria.color("blue")
	austria.up()
	austria.left(90)
	austria.forward(50)
	austria.left(90)
	austria.down()
	austria.forward(200)
	#belgium
	belgiumflag()
	#wn.exitonclick()

#english

def englishflags():
	wn = turtle.Screen()
	turtle.title("Flags of countries in which English is spoken")
	#uk
	uk = turtle.Turtle()
	uk.speed(10)
	uk.color("blue")
	uk.up()
	uk.forward(-100)
	uk.right(90)
	uk.forward(-120)
	uk.right(90)
	uk.pensize(200)
	uk.down()
	uk.forward(150)
	uk.pensize(40)
	uk.up()
	uk.right(90)
	uk.forward(-70)
	uk.right(90)
	uk.forward(-30)
	uk.left(33)
	uk.color("white")
	uk.down()
	uk.forward(250)
	uk.pensize(20)
	uk.color("red")
	uk.forward(-250)
	uk.up()
	uk.right(33)
	uk.forward(200)
	uk.left(327)
	uk.color("white")
	uk.pensize(40)
	uk.forward(-250)
	uk.down()
	uk.forward(250)
	uk.color("red")
	uk.pensize(20)
	uk.forward(-250)
	uk.up()
	uk.left(33)
	uk.forward(110)
	uk.right(90)
	uk.pensize(40)
	uk.color("white")
	uk.down()
	uk.forward(140)
	uk.color("red")
	uk.pensize(20)
	uk.forward(-140)
	uk.up()
	uk.left(55)
	uk.forward(130)
	uk.left(35)
	uk.pensize(40)
	uk.color("white")
	uk.down()
	uk.forward(-220)
	uk.color("red")
	uk.pensize(20)
	uk.forward(220)
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
	canada.forward(-250)
	canada.right(90)
	canada.forward(150)
	canada.pensize(200)
	canada.left(90)
	canada.down()
	canada.forward(150)
	canada.up()
	canada.forward(-75)
	canada.left(90)
	canada.forward(100)
	canada.pensize(100)
	canada.color("white")
	canada.down()
	canada.forward(-200)
	canada.up()
	canada.forward(100)
	canada.color("red")
	canada.shape("turtle")
	canada.stamp()
	#wn.exitonclick()

#swedish

def swedenflag():
	wn = turtle.Screen()   
	turtle.title("Flags of countries in which Swedish is spoken")     
	sweden = turtle.Turtle()      
	sweden.color("blue")
	sweden.pensize(200)
	sweden.forward(150)
	sweden.color("gold")
	sweden.pensize(40)
	sweden.forward(80)
	sweden.forward(-310)
	sweden.up()
	sweden.left(45)
	sweden.forward(120)
	sweden.down()
	sweden.right(135)
	sweden.forward(170)
	#wn.exitonclick()

#norwegian

def norwayflag():
	wn = turtle.Screen()
	turtle.title("Flags of countries in which Norwegian is spoken")
	norway = turtle.Turtle()      
	norway.color("red")
	norway.pensize(200)
	norway.forward(150)
	norway.color("white")
	norway.pensize(40)
	norway.forward(80)
	norway.forward(-310)
	norway.up()
	norway.left(45)
	norway.forward(120)
	norway.down()
	norway.right(135)
	norway.forward(170)
	norway.color("blue")
	norway.pensize(20)
	norway.forward(-170)
	norway.right(45)
	norway.up()
	norway.forward(120)
	norway.down()
	norway.left(135)
	norway.forward(310)
	# wn.exitonclick()

#icelandic

def icelandflag():
	wn = turtle.Screen() 
	turtle.title("Flags of countries in which Icelandic is spoken")       
	iceland = turtle.Turtle()      
	iceland.color("blue")
	iceland.pensize(200)
	iceland.forward(150)
	iceland.color("white")
	iceland.pensize(40)
	iceland.forward(80)
	iceland.forward(-310)
	iceland.up()
	iceland.left(45)
	iceland.forward(120)
	iceland.down()
	iceland.right(135)
	iceland.forward(170)
	iceland.color("red")
	iceland.pensize(20)
	iceland.forward(-170)
	iceland.right(45)
	iceland.up()
	iceland.forward(120)
	iceland.down()
	iceland.left(135)
	iceland.forward(310)
	# wn.exitonclick()

#afrikaans
	

danishfam = ["moder", "far", "bedstemor", "bedstefar", "onkel", "tante", "datter", "søn", "søster", "bror", "nevø", "niece", "barnebarn", "fætter"]
dutchfam = ["moeder", "vader", "grootmoeder", "grootvader", "oom", "tante", "dochter", "zoon", "zus", "broer", "neef", "nicht", "kleinzoon", "kleindochter"]
germanfam = ["Mutter", "Vater", "Großmutter", "Großvater", "Onkel", "Tante", "Tochter", "Sohn", "Schwester", "Bruder", "Neffe", "Nichte", "Enkel", "Enkelin", "Cousin", "Cousine"]
englishfam = ["mother", "father", "grandpa", "grandma", "uncle", "aunt", "daughter", "sister", "brother", "son", "niece", "nephew", "grandchild", "cousin"]
swedishfam = ["mamma", "fader", "mormor", "farfar", "farbror", "moster", "dotter", "son", "syster", "broder", "brorson", "niece", "barnbarn", "kusin"]
norfam = ["mother", "far", "bestemor", "bestefar", "onkel", "tante", "datter", "sønn", "søster", "bror", "nevø", "niese", "barnebarn", "fetter"]
icefam = ["móðir", "faðir", "amma", "afi", "frændi", "frænka", "dóttir", "sonur", "systir", "bróðir", "frændi", "frænka", "barnabarn","frændi"]
afrikaansfam = ["Moeder", "vader", "ouma", "Oupa", "oom", "tannie", "dogter", "seun", "suster", "broer", "neef", "niggie", "kleinseun","kleindogter","neef","neef"]

insert_word = []

def show_entry_fields():
   insert_word.append(e1.get())

master = Tk()
Label(master, text="Type in an expression for a family member in German, Danish, Dutch, English, Swedish, Norwegian or Icelandic!").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)

Button(master, text='1. Step: Submit', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='2. Step: Show flag', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)

mainloop( )

def langvisual():
	for i in insert_word:
		if i in germanfam:
			print(germanflags())
			time.sleep(3)
		if i in danishfam:
			turtle.clearscreen()
			print(danishflag())
			time.sleep(3)
		if i in dutchfam:
			turtle.clearscreen()
			print(dutchflags())
			time.sleep(3)
		if i in englishfam:
			turtle.clearscreen()
			print(englishflags())
			time.sleep(3)
		if i in swedishfam:
			turtle.clearscreen()
			print(swedenflag())
			time.sleep(3)
		if i in norfam:
			turtle.clearscreen()
			print(norwayflag())
			time.sleep(3)
		if i in icefam:
			turtle.clearscreen()
			print(icelandflag())
			time.sleep(3)

print(langvisual())