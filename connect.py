import paho.mqtt.client as mqtt
import pymongo
import json
import time
import datetime
import os
def on_message(client, userdata, message):
    messages = str(message.payload.decode("utf-8"))
    print(messages)
    global mycol
    #print(mycol)
    y = json.loads(messages)
    current_time = datetime.datetime.now()
    if str(message.topic)[-1] == str(5):
        name = "Temperature and atmosphere moisture"
    elif str(message.topic)[-1] == str(6):
        name = "Light Intensity"
    elif str(message.topic)[-1] == str(7):
        name = "Soil moisture"
    myquery = {"id": y["device_id"]}
    newvalue = {"$push": {"log":{"value" : y["value"],"time": current_time}}}
    mycol.update_one(myquery, newvalue)
    #print(1)
    # cursor = mydb.devices.find() 
    # for record in cursor: 
    #     print(record) 


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
if __name__ == "__main__":
    mongo_uri = os.environ.get("MONGODB_URI")
    myclient = pymongo.MongoClient(mongo_uri + "?retryWrites=false")
    mydb = myclient["heroku_v9nz7rkl"]
    mycol = mydb["devices"] 
    broker_address="13.76.250.158"
    print("creating new instance")
    client = mqtt.Client("A1") #create new instance
    client.on_message=on_message #attach function to callback
    client.username_pw_set("BKvm2", "Hcmut_CSE_2020")
    print("connecting to broker")
    client.connect(broker_address, port=1883) #connect to broker
    print("Subscribing to topic","Topic/#")

    #print(mydb.list_collection_names())
    client.subscribe([("Topic/#",1)])
    client.loop_forever() #start the loop

    #print("Publishing message to topic","house/bulbs/bulb1")
    #client.publish("forecast/getdata","OjjjjjjjFF")
    #stop the loop
