import random
from datetime import datetime
from sys import stderr
from time import sleep

import requests

next_id = 1

while True:
    value = random.random() * 50.0 - 25.0
    if value < -20 or value > 15:
        alert = True
    else:
        alert = False
    reading = {
        "id": next_id,
        "type": "temperature",
        "value": value,
        "alert": alert,
        "timestamp": datetime.now().isoformat()
    }
    print(f"sending reading: {reading}")
    try:
        requests.request("post", "http://localhost:5000/sensor-readings", json=reading)
    except:
        print("request failed", file=stderr)

    next_id += 1
    sleep(1.0)
