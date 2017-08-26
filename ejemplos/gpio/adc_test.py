import machine
import time

adc = machine.ADC(0)
p2=machine.Pin(2,machine.Pin.OUT)

while True:
    try:
        lect=adc.read()
        print(lect)
        if(lect<700):
            p2.value(0)
        else:
            p2.value(1)
        time.sleep(0.5)
    except:
        break
