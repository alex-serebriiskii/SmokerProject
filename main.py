import sys
import time
from max6675 import MAX6675,MAX6675Error
def main():
    print("main")


if __name__ == "__main__":

    # default example
    cs_pin = 24
    clock_pin = 23
    data_pin = 22
    units = "c"
    thermocouple = MAX6675(cs_pin, clock_pin, data_pin, units)
    running = True
    tc = ""
    while(running):
        try:            
            try:
                tc = thermocouple.get()        
            except MAX6675Error as e:
                tc = "Error: "+ e.value
                running = False
            print("tc: {}".format(tc))
            time.sleep(1)
        except KeyboardInterrupt:
            running = False
    thermocouple.cleanup()
