# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("publisher")
mqttc.connect("localhost", 1883)
mqttc.publish("sensor-data-topic", "Sensor Data: Hello, World!")
mqttc.loop(2) 
