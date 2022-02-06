import RPi.GPIO as GPIO

class Fan(object):
    def init(self,pin,board=GPIO.BCM):
        self.pin = pin
        self.board=board
        self.on=False
        
        #Set up the board and GPIO
        GPIO.setmode(self.board)
        GPIO.setup(self.pin,GPIO.OUT)

    def PowerOn(self):
        GPIO.output(self.pin,GPIO.HIGH)

    def PowerOn(self):
        GPIO.output(self.pin,GPIO.LOW)

    def cleanup(self):
        GPIO.setup(self.pin,GPIO.IN)