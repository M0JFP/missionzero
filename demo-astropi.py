import os
import datetime
from time import sleep
from gpiozero import Button
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(270)
buttonu = Button(26)
buttonl = Button(19)
buttonr = Button(20)
buttond = Button(13)
leftb = Button(21)
rightb = Button(16)

def take_photo():
        sense.show_message("Photo")
        os.system("raspistill -rot 90 -o /home/pi/raspberryjam/image.jpg")


def take_temp():
	sense.show_message("Temp")
	sense.clear()
	temp = sense.get_temperature()
	temp = round(temp, 1)
	print(temp)
	colour = (255, 0, 0)
	sense.show_message(str(temp), text_colour=colour)

def take_pressure():
        sense.show_message("Pressure")
        sense.clear()
        pressure = sense.get_pressure()
        print (pressure)
        colour = (255, 0, 0)
        sense.show_message(str(pressure), text_colour=colour)


def take_humidity(): 
        sense.show_message("Humidity")
        sense.clear()
        humidity = sense.get_humidity()
        print (humidity)
        colour = (255, 0, 0)
        sense.show_message(str(humidity), text_colour=colour)

def smile():
        sense.set_pixel(2, 2, (0, 0, 255))
        sense.set_pixel(4, 2, (0, 0, 255))
        sense.set_pixel(3, 4, (100, 0, 0))
        sense.set_pixel(1, 5, (255, 0, 0))
        sense.set_pixel(2, 6, (255, 0, 0))
        sense.set_pixel(3, 6, (255, 0, 0))
        sense.set_pixel(4, 6, (255, 0, 0))
        sense.set_pixel(5, 5, (255, 0, 0))

def email():
        sense.show_message("*")

def web():
        sense.show_message("http://chertseyradioclub.blogspot.co.uk")


buttonu.when_pressed = take_photo
buttond.when_pressed = take_temp
buttonl.when_pressed = take_pressure
buttonr.when_pressed = smile
leftb.when_pressed = email
rightb.when_pressed = web
