# MQTT: The Standard for IoT messaging

MQTT is an OASIS standard messaging protocol for the Internet of Things (IoT). It is designed as an extremely lightweight publish/subscribe messaging transport that is ideal for connecting remote devices with a small code footprint and minimal network bandwidth. MQTT today is used in a wide variety of industries, such as automotive, manufacturing, telecommunications, oil and gas, etc.

Also, MQTT is a lightweight publish/subscribe messaging protocol designed for M2M (machine to machine) telemetry in low bandwidth environments.

In this section, we will setup the environment required to test MQ-Telemetry protocol. Follow below steps as mentioned.

The key players in MQTT are **MQTT Clients** and **MQTT broker**.

## Software requirements:

* 1. AWS Cloud
* 2. Ubuntu 18.0.x EC2 instance
* 2. MQTT broker
* 3. MQTT Client (Paho MQTT python client)

We will now setup each software requirement.

## 1. Setup MQTT Broker

Out of all the available open source MQTT brokers in the market, we consider **'Eclipse Mosquitto'**.

[Refer here](https://mosquitto.org/) for Eclipse Mosquitto.

## 2. Setup MQTT Client

From the available open source for MQTT clients, we consider **'Paho MQTT Python Client'**.

[Refer here](https://www.eclipse.org/paho/index.php?page=clients/python/index.php) for Paho MQTT python client.