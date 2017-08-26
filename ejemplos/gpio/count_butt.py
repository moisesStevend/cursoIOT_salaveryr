import machine
import time

def num_bin(num):
    return ((num&2)>>1), num&1

p2=machine.Pin(2,machine.Pin.OUT)
p16=machine.Pin(16,machine.Pin.OUT)
p0=machine.Pin(0,machine.Pin.IN, machine.Pin.PULL_UP)

count=0
p2.value(1)
p16.value(1)

while True:
    try:
        if(p0.value()==0):
            time.sleep(0.3)
            count+=1
            msb,lsb=num_bin(count)
            print(msb,lsb)
            p16.value(not lsb)
            p2.value(not msb)
    except:
        break

p2.value(1)
p16.value(1)
