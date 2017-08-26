import urequests
import machine
import time

#curl 'https://api.thingspeak.com/channels/322066/feeds.json?api_key=URPK2ZSQE4B6LUQ2&results=10&timezone=America%2FLima'
adc = machine.ADC(0)
#lect=adc.read()
#r=urequests.get("http://api.thingspeak.com/update?api_key=S3ORW0BUEFUAXQI7&field1=-3&field2=-5")
#print r.status_code
while True:
    try:
        try:
            lect=adc.read()
        except:
            lect=500
        r=urequests.get("https://api.thingspeak.com/update?api_key=S3ORW0BUEFUAXQI7&field2="+str(lect))
        print(lect)
        if(r.status_code==200):
            print("code 200")
            time.sleep(60)
        else:
            print(r.status_code)

    except:
        print("error")
        time.sleep(60)
