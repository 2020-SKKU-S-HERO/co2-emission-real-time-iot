import paho.mqtt.client as mqtt
from datetime import datetime

host = "34.64.238.233"
port = 1883
topic = "emission/co2"


def publish_to_server(date_time: str, emissions: float) -> None:
    """ 서버에 있는 브로커로 데이터를 발행한다.

    Args:
        date_time: 날짜와 시간 (format: YY-MM-DD hh:mm:ss)
        emissions: 배출량
    """
    payload = f"{date_time}|{str(emissions)}"
    mqtt_client = mqtt.Client("")
    mqtt_client.connect(host, port)
    mqtt_client.publish(topic, payload)
    mqtt_client.loop(2)


# test
now = datetime.now()
current_time_str = f"{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}"
publish_to_server(current_time_str, 3500)
