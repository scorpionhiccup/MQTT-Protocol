# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
	'''
		Callback for when the client receives a 
		CONNACK response from the server.	
	'''
	print("Connected with result code "+str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe("sensor-data-topic")

# 
def on_message(client, userdata, msg):
	'''
		The callback for when a PUBLISH message 
		is received from the server.
	'''
	print "Topic: ", msg.topic+'\nMessage: '+str(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches
# callbacks and handles reconnecting.
# Other loop*() functions are available that give a threaded 
# interface and a manual interface.
client.loop_forever()

