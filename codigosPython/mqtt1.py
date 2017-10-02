import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
	client.subscribe("labotec/iot2")
    client.subscribe("labotec/iot")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client("pc-ubuntu")
client.connect("192.168.1.62",1883,60)
client.loop_start()

client.on_connect = on_connect
client.on_message = on_message

data2={
		'temperatura':23,
		'humedad':20,
	}

while True:
    data=raw_input("se enviara: ")
    client.publish('labotec/iot',json.dumps(data2)) #envio por json
	#client.publish('labotec/iot',data)  # envio por teclado
