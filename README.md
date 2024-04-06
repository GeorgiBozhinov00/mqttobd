# MqttOBD - Raspberry Pi
 A simple python script using [**PythonOBD**] (https://python-obd.readthedocs.io) and [**mosquitto/mqtt**]
# Requirements
 Microcontroller that supports **Wi-Fi** and can run **python**. In my case I have used a **Raspberry Pi** with Bluetooth and Wi-Fi supported.
 An OBD connector that can connect to the microcontroller. **ELM327** works just fine. If you are going to use ELM327 make sure that the microcontroller has **Bluetooth**.
## Usage~
 Copy the repository and change the values of the following variables "broker_address", "port", "topic"
Plug in the ELM327 in your veichle
Open terminal 
```
sudo bluetoothctl

```
agent on

```
default-agent
