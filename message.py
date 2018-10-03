from sense_emu import SenseHat
sense = SenseHat()
blue = (0,0,255)
yellow = (255,255,0)

sense.show_message("Egham Raspberry Jam is awesome", text_colour=yellow, back_colour=blue)
