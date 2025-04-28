# a nice code car
import time
import random

class Car:
    def __init__(self, company, mph, gas, green, model, colour, interior, seats, price):
        self.company = company
        self.mph = mph
        self.gas = gas
        self.green = green
        self.model = model
        self.colour = colour
        self.interior = interior
        self.seats = seats
        self.price = price

class Pilot:
    def __init__(self, name, surname, height, iq, athletic, married, age, notes):
        self.name = name
        self.surname = surname
        self.height = height
        self.iq = iq
        self.athletic = athletic
        self.married = married
        self.age = age
        self.notes = notes

p1 = Pilot("Omar", "Mohammed", 183, 140, True, True, 28, "drives to work 24/7")
p2 = Pilot("Yaqub", "Hussain", 155, 158, True, False, 13, "wrote this code")
p3 = Pilot("Little", "Man", 126, 78, True, False, 9, "no prior driving experience")
p4 = Pilot("Big", "Blue", 213, 96, False, True, 45, "how did he get a wife?")

c1 = Car('Tesla', 155, False, True, "Model Y", "Midnight Silver Metallic", "Black and White", 5, 67090)
c2 = Car('Ferrari', 211, True, False, "Ferrari F8 Tributo", "Red", "Black", 5, 203476)
c3 = Car('Range Rover', 145, True, False, '2015 Land Range Rover Evopue', "White", "Black", 5, 41100)
c4 = Car('MMYY LTD', 767, False, True, "001", "holographic", "null", 1, 340000)

tst = input("Check: ")

def location():
    loc = input("Where would you like to drive? South America, Asia, Europe, United States of America or Africa?")
    if loc == "Africa":
        print("We are in Africa, Rwanda, Kigali")
    elif loc == "Asia":
        print("We are in Asia, Japan, Tokyo")
    elif loc == "South America":
        print("We are in South America, Peru, Machu Picchu")
    elif loc == "United States of America":
        print("We are in the United States of America, Alaska, Fairbanks")
    elif loc == "Europe":
        print("We are in Central London, Westminster Abbey")

location()

def testdrive():
    if tst == "Car 1":
        print("Company/Branding " + c1.company)
        time.sleep(1)
        print("Gas car " + str(c1.gas))
        time.sleep(1)
        print("Green car " + str(c1.green))
        time.sleep(1)
        print("The model " + c1.model)
        time.sleep(1)
        print("Colour " + c1.colour)
        time.sleep(1)
        print("Inside " + c1.interior)
        time.sleep(1)
        print("Seats " + str(c1.seats))
        time.sleep(1)
        print("The cost: " + str(c1.price))
        time.sleep(3)
        print("This is Car One, "+ c1.company)
    elif tst == "Car 2":
        print("Company/Branding " + c2.company)
        time.sleep(1)
        print("Gas car " + str(c2.gas))
        time.sleep(1)
        print("Green car " + str(c2.green))
        time.sleep(1)
        print("The model " + c2.model)
        time.sleep(1)
        print("Colour " + c2.colour)
        time.sleep(1)
        print("Inside " + c2.interior)
        time.sleep(1)
        print("Seats " + str(c2.seats))
        time.sleep(1)
        print("The cost: " + str(c2.price))
        time.sleep(3)
        print("This is Car Two, " + c2.company)
    elif tst == "Car 3":
        print("Company/Branding " + c3.company)
        time.sleep(1)
        print("Gas car " + str(c3.gas))
        time.sleep(1)
        print("Green car " + str(c3.green))
        time.sleep(1)
        print("The model " + c3.model)
        time.sleep(1)
        print("Colour " + c3.colour)
        time.sleep(1)
        print("Inside " + c3.interior)
        time.sleep(1)
        print("Seats " + str(c3.seats))
        time.sleep(1)
        print("The cost: " + str(c3.price))
        time.sleep(3)
        print("This is Car Three, " + c3.company)
    elif tst == "Car 4":
        print("Company/Branding " + c4.company)
        time.sleep(1)
        print("Gas car " + str(c4.gas))
        time.sleep(1)
        print("Green car " + str(c4.green))
        time.sleep(1)
        print("The model " + c4.model)
        time.sleep(1)
        print("Colour " + c4.colour)
        time.sleep(1)
        print("Inside " + c4.interior)
        time.sleep(1)
        print("Seats " + str(c4.seats))
        time.sleep(1)
        print("The cost: " + int(c4.price))
        time.sleep(3)
        print("This is Car Three, " + c3.company)

testdrive()

drive = input("Start Drive:")

max1 = c1.mph
max2 = c2.mph
mph = [10, 15, 20, 30]

def IDT():
    if drive == c1.company:
        print("Tesla Starting")
        time.sleep(1)
        print("Identifying...")
        time.sleep(1)
        name = input("Are you " + p1.name + " Y/N ")
        if name == "Y":
            print("Welcome " + p1.name)
            time.sleep(1)
            print("Starting...")
            time.sleep(2)
            print("Dashboard: ")
            time.sleep(0.5)
            print("Driving at")
        elif name == "N":
            print("Access Denied")

IDT()

def IDF():
    if drive == c2.company:
        print("Ferrari Starting")
        time.sleep(1)
        print("Identifying...")
        time.sleep(1)
        name = input("Are you " + p2.name + " Y/N ")
        if name == "Y":
            print("Welcome " + p2.name)
            time.sleep(1)
            print("Starting...")
            time.sleep(3)
            print("Driving at 10 mph")
        elif name == "N":
            print("Access Denied ")

IDF()

def IDR():
    if drive == c2.company:
        print("Range Rover Starting")
        time.sleep(1)
        print("Identifying...")
        time.sleep(1)
        name = input("Are you " + p2.name + " Y/N ")
        if name == "Y":
            print("Welcome " + p2.name)
            time.sleep(1)
            print("Starting...")
            time.sleep(3)
            print("Driving at 10 mph")
        elif name == "N":
            print("Access Denied ")

IDR()

change_speed = input("Increase speed? (Y/N): ")
speed = 10

if change_speed == "Y":
    print("Increased speed, speed = " + str(speed))
    speed = 20
elif change_speed == "N":
    Speed = 10

    while True:
        gear = input("Change gear here: ")
        time.sleep(1.2)

def gear():
    if gear == '1':
        speed = 10
        print("Speed is " + str(speed) + " mph")
    elif gear == '2':
        speed = 20
        print("Speed is " + str(speed) + " mph")

    elif gear == 3:
        speed = 30
        print("...")
# i will update code soon :)