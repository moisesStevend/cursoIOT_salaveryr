import machine
import time

global p

def bin_pin(num):
    msb,lsb=((num&2)>>1),num&1
    p[0].value(not lsb)
    p[1].value(not msb)
    '''
    nB=bin(num)[2:][::-1]
    lsb=int(nB[0])
    msb=int(nB[1])
    p[0].value(lsb)
    p[1].value(msb)
    print(p[0].value(),':',p[0].value())
    print('\n')
    '''
pines_num=[2,16]
p=[None]*len(pines_num)

for i in pines_num:
    p[pines_num.index(i)]=machine.Pin(i,machine.Pin.OUT)
'''
for i in p:
    print('p:',i)
'''
count=0
print('while')

while True:
    try:
        bin_pin(count)
        print(bin(count))
        count+=1
        time.sleep(0.5)
        if(count==4):
            count=0
    except:
        break
p[0].value(0)
p[1].value(0)
