import paho.mqtt.client as paho
import time
import random

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
broker_address="13.76.87.87" 
client = paho.Client()
client.on_publish = on_publish
client.connect(broker_address, 1883)
client.loop_start()

while True:
    message = "{ \"device_id\":\"d5_1\", \"value\":[\"%.2f\",\"%.2f\"] }"%(random.uniform(10,40), random.uniform(20,100)) 
    client.publish("test/device_5", message, qos=1)
    message = "{ \"device_id\":\"d6_1\", \"value\":[\"%.2d\"] }"%(random.randint(0,1023)) 
    client.publish("test/device_6", message, qos=1)
    message = "{ \"device_id\":\"d7_1\", \"value\":[\"%.2d\",\"%.2d\"] }"%(random.randint(0,1),random.randint(0,1023)) 
    client.publish("test/device_7", message, qos=1)
    time.sleep(300)