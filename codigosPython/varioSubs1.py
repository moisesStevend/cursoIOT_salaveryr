#!/usr/bin/env python

import paho.mqtt.client as mqtt
import json

global client2
global Client

def on_connect(client, userdata, flags, rc):
  print("Empezamos a conectarnos con calidad "+str(rc))
  client.subscribe("moisesmezaupcs")

def on_message(client, userdata, msg):
  print msg.payload
  if (msg.payload == "finish"):
    print("acabo!")
    client.disconnect()
    
def on_connect2(client, userdata, flags, rc):
  print("Empezamos a conectarnos con calidad 2"+str(rc))
  client.subscribe("P1A2")


def on_message2(client, userdata, msg):
  Client.publish("moisesmezaupcs", json.dumps({"data":json.dumps(msg.payload)}));
  #print  msg.payload
    
Client = mqtt.Client()
client2 = mqtt.Client()

client2.connect("smartcacao.ddns.net",1883,60)
Client.connect("192.168.43.79",1883,60)

client2.loop_start()
Client.loop_start()

Client.on_connect = on_connect
Client.on_message = on_message

client2.on_connect = on_connect2
client2.on_message = on_message2

while True:
	men = raw_input("mensaje: ")
	Client.publish("moisesmezaupcs", men);
	#if men=='salir':
	#	break
	#pass

client.loop_stop()
client.disconnect()
#client.loop_forever()
