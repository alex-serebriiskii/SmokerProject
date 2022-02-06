import sys
def main():
    low=int(sys.argv[1])
    high=int(sys.argv[2])
    critlow=int(sys.argv[3])
    crithigh=int(sys.argv[4])
    cycles=int(sys.argv)
    print("main")


if __name__ == "__main__":

    # default example
    cs_pin = 24
    clock_pin = 23
    data_pin = 22
    units = "c"
    thermocouple = MAX6675(cs_pin, clock_pin, data_pin, units)
    running = True
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