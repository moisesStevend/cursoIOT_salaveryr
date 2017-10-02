import paho.mqtt.client as paho
import time

client = paho.Client(protocol=paho.MQTTv31)
client.connect("192.168.2.82", 1883)
client.loop_start()
client.publish("mytesttopic", str("foo"), qos=2)
time.sleep(1)  # Give the client loop time to proess the message
