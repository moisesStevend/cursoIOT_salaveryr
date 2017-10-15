#!/usr/bin/env python

import time
import paho.mqtt.client as mqtt

#time.sleep(60)

def on_connect(client, userdata, flags, rc):
  print("Empezamos a conectarnos con calidad "+str(rc))
  client.subscribe("topico_meza123")

def on_message(client, userdata, msg):
  print msg.payload
  if (msg.payload == "finish"):
    print("acabo!")
    client.disconnect()

client = mqtt.Client()
client.connect("test.mosquitto.org",1883)
client.loop_start()

client.on_connect = on_connect
client.on_message = on_message

while True:
        #men = raw_input("mensaje: ")

        client.publish("moisesmezaupc", "test****");
        time.sleep(1)   #if men=='salir':
        #       break
        #pass

client.loop_stop()
client.disconnect()

