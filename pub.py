import paho.mqtt.client as mqtt

host = "34.64.176.192"
port = 1883
topic = "mqtt/myiot/paho"
payload = "This is Pub client."

mqtt = mqtt.Client("")
mqtt.connect(host, port)
mqtt.publish(topic, payload)
print("The message is published.")
mqtt.loop(2)
