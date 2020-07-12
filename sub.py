import paho.mqtt.client as mqtt

host = "localhost"
port = 1883
topic = "mqtt/myiot/#"


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(topic)


def on_message(client, userdata, msg):
    print(f"{msg.topic} {str(msg.payload)}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host, port, 60)
client.loop_forever()

