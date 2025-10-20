import pandas as pd
import time
from paho.mqtt import client as mqtt_client
import json

broker = "localhost"
port = 1883
topic = "ecosynth/sensors"

client = mqtt_client.Client("EcoSynthSim")
client.connect(broker, port)

data = pd.read_csv("../backend/data/sensor_data.csv")

for _, row in data.iterrows():
    payload = row.to_dict()
    client.publish(topic, json.dumps(payload))
    print(f"Published: {payload}")
    time.sleep(1)
