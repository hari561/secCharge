"""
This script is developed according to python 3.6.
This script publishes topic 'python/mqtt' every second to the MQTT broker resided at '18.219.133.173' in AWS Cloud by connecting through 'TCP' protocol.
The authentication on MQTT client is ensured through username/password of the MQTT broker.

Note: At present the MQTT broker accepts connection ONLY through the port '1883' (TCP).

"""

# python 3.6

import random
import time

import paho.mqtt.client as mqtt

broker = "18.219.133.173"
port = 1883
topic = "python/mqtt"

client_id = 'python-mqtt-client1'

username = 'hari'
password = 'hari'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        print('rc ::: ', rc)
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt.Client(client_id)
    print('client instance created::: ', client);
    client.username_pw_set(username, password)
    print('client user_pass::: ', client);
    client.on_connect = on_connect
    print('client on_connect::: ', on_connect);
    client.connect(broker, port)
    print('client connect::: ', client);
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = "messages " + str(msg_count)
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print("Send "+msg+" to topic "+topic)
        else:
            print("Failed to send message to topic "+ topic)
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
