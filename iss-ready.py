from time import sleep
from sense_emu import SenseHat
sense = SenseHat()
#rotate scren for astro-pi use
sense.set_rotation(270)

red = (255,0,0)
green = (0,255,0)
sense.show_message("Hello ISS from Egham Raspberry Jam", text_colour=red, back_colour=green)
w = (255, 255, 255)
b = (0, 0, 0)
y = (255, 255, 0)
g = (0, 255, 0)
picture = [
            b, b, w, w, w, w, b, b,
            b, w, b, b, b, b, w, b,
            b, w, b, w, w, b, w, b,
            b, w, b, b, b, b, w, b,
            b, b, w, w, w, w, b, b,
            b, b, w, w, w, w, b, b,
            b, w, w, w, w, w, w, b,
            b, w, w, w, w, w, w, b
        ]
hot = [
        b, b, b, b, b, y, y, b,
        b, b, b, b, y, y, y, y,
        b, b, b, b, b, y, y, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g
      ]
cold = [
        b, b, w, b, b, b, w, b,
        b, b, b, b, b, w, b, b,
        b, w, b, b, b, b, b, w,
        b, b, b, b, w, b, b, b,
        w, b, b, w, b, b, w, b,
        b, b, b, b, b, b, b, b,
        w, w, w, w, w, w, w, w,
        w, w, w, w, w, w, w, w
      ]
sense.set_pixels(picture)
sleep(2)
temp = sense.get_temperature()
temp = round( sense.get_temperature(), 1 )
sense.show_message( "Temp is " + str(temp) + "C", text_colour=g, back_colour=w)
temp = sense.get_temperature()
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
