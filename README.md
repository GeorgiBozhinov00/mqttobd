# MqttOBD - Raspberry Pi
### A simple python script to read and post vehicle information using [**PythonOBD**](https://python-obd.readthedocs.io) and [**mosquitto/mqtt**](https://mosquitto.org)
# Requirements
 Microcontroller that supports **Wi-Fi** and can run **python**. In my case I have used a **Raspberry Pi** with Bluetooth and Wi-Fi supported.
 An OBD connector that can connect to the microcontroller. **ELM327** works just fine. If you are going to use ELM327 make sure that the microcontroller has **Bluetooth**.
# Usage~
1. Copy the repository and change the values of the following variables "broker_address", "port", "topic". If you would like to add more values to be read check [this](https://python-obd.readthedocs.io/en/latest/Command%20Tables/)
2. Plug in the ELM327 in your vehicle
3. Open terminal 
A) To turn on bluetooth:
```
sudo bluetoothctl
```
B) Turn on the agent in order to pair
```
agent on
```
C) Scan for devices
```
scan on
```
D) When you find the device copy the mac address XX:XX:XX:XX:XX:XX
```
pair **yourDeviceMacAddress**
```
E) In order to save the device to known devices you can trust it
```
trust **yourDeviceMacAddress**
```
F) Exit the bluetoothctl terminal 

G) Reserve a rfcomm for the bluetooth device

```
rfcomm bind /dev/rfcomm0 **yourDeviceMacAddress**
```
H) The last step is to start the python script and enjoy.
```
sudo python3 mqttobd.py
```




