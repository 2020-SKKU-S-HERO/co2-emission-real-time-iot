#구글 클라우드 플랫폼 및 MQTT 설명

## 구글 클라우드 플랫폼

구글 클라우드 플랫폼에 리눅스 서버를 구축하였다.

### 접속 방법

ssh를 사용하여 접속할 수 있다. ras key는 rsa-gcp-key 파일을 사용한다.  
rsa-gcp-key 파일이 있는 곳에서 터미널을 열고 다음의 쉘 명령어를 입력한다.

```shell script
ssh -i ./rsa-gcp-key shero@34.64.176.192
```

해당 명령어를 입력하면 rsa-key에 대한 비밀번호를 입력하라고 한다.  
비밀번호는 'shero'이다.

## MQTT

MQTT는 IoT를 위한 통신 프로토콜로 저전력, 낮은 패킷량으로 통신한다는 점이 특징이다.  
MQTT는 일반적인 통신과 다르게, 중간에 통신을 중계하는 브로커가 존재한다.

![](.readme_images/mqtt_des.png)

### 파이썬 사용 예시

#### 선행 조건

먼저 mqtt를 설치해야 한다.

```shell script
pip3 install paho-mqtt
```

#### 브로커에 연결

먼저 mqtt.client를 임포트한다.

```python
import paho.mqtt.client as client
```

mqtt 클라이언트를 만든다.

```python
mqtt_client = mqtt.Client()
```

브로커에 연결한다.

```python
mqtt_client.connect(host)
```

#### 브로커에 메세지 보내기

브로커에 연결 후, publish 메서드를 통해 메세지를 보낼 수 있다.  
topic은 서로 같거냐 상위의 topic에게 메세지가 전달된다.  
예를 들면 abc/123 으로 메세지를 보내면 abc, abc/123 토픽을 구독하는 프로그램에게 메세지가 전달된다.  
payload는 보낼 메세지이다.

```python
mqtt_client.publish(topic, payload)
```

#### 브로커로부터 메세지 받기

client 객체에 콜백 함수를 지정할 수 있다. 브로커와 연결에 성공하면 구독하는 콜백 함수를 지정한다.

```python
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(topic)

mqtt_client.on_connect = on_connect()
```

브로커로부터 메세지를 받으면 호출되는 콜백 함수를 지정한다.

```python
def on_message(client, userdata, msg):
    print(f"{msg.topic} {str(msg.payload)}")

mqtt_client.on_message = on_message
```

## 현재 상태

로컬에서는 mqtt와 mosquitto(브로커)를 통해 메세지 교환이 되는 것을 확인했다.  
구글 클라우드 플랫폼의 리눅스 서버에 mosquitto 서비스로 켜두었다.  
그러나 컴퓨터에서 리눅스 서버에 켜진 mosquitto로 연결 시도를 했지만 되지 않는다.  
현재 다음의 시도를 해본 상태이다.

* 구글 클라우드 플랫폼 방화벽 설정
>구글 클라우드 플랫폼에서 mqtt가 사용하는 포트인 1883에 대해 방화벽 허용 설정을 하였다.  
>그러나 해결되지는 않았다.
* mqtt 통신을 할 때 rsa 키를 담기
>구글 클라우드 플랫폼에 ssh접속할 때 rsa키를 요구한다.  
>따라서 mqtt 통신 때도 보안때문에 필요할 것으로 추측되나 구글링을 해보아도 방법을 알 수가 없다.

## 유력한 해결 방법

mosqutto 브로커 서버를 리눅스 서버가 아닌 라즈베리파이에 실행하는 방법이다.  
그에 대한 테스트로 컴퓨터에 서버를 켜두고 구글 클라우드 플랫폼에서 이쪽 컴퓨터로 연결하도록 해서  
테스트하는 방법이 있지만, 공유기 설정이 까다로워서 외부에서 이쪽 컴퓨터로 접속할 방법이 없다.