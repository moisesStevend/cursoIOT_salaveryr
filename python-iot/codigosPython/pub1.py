#!/usr/bin/env python

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
  print("Empezamos a conectarnos con calidad "+str(rc))
  client.subscribe("xpotron2017")

def on_message(client, userdata, msg):
  print msg.payload
  if (msg.payload == "finish"):
    print("acabo!")
    client.disconnect()
    
client = mqtt.Client()
client.connect("test.mosquitto.org",1883)#('127.0.0.1',1883)	#"test.mosquitto.org",1883)
client.loop_start()

client.on_connect = on_connect
client.on_message = on_message

while True:
	men = raw_input("mensaje: ")
	client.publish("inTopic", men);
	#if men=='salir':
	#	break
	#pass

client.loop_stop()
client.disconnect()
#client.loop_forever()

