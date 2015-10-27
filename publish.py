# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("publisher")
mqttc.connect("localhost", 1883)
# mqttc.publish("Sensor-data-Topic", "Sensor Data: Hello, World!")
# To enable message retention.
mqttc.publish("Sensor-data-Topic", "Sensor Data: Hello, World!", 0, True)
mqttc.loop(2) 
