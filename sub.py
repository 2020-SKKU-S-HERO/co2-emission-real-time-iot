import paho.mqtt.client as mqtt
from mysql import *

host = "localhost"
port = 1883
topic = "emission/co2"


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(topic)


def on_message(client, userdata, msg):
    # b'~' 꼴 문자열 전처리
    payload_str = str(msg.payload).replace("b'", "")
    payload_str = payload_str.replace("'", "")
    str_list = payload_str.split("|")
    print(str_list)

    data = Data(str_list[0], float(str_list[1]))
    insert_into_db(data)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host, port, 60)
client.loop_forever()

