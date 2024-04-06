import obd
import paho.mqtt.client as mqtt
import time

# Establish OBD connection
connection = obd.OBD() # auto-connects to USB or RF port

# MQTT broker IP and port
broker_address = "7.tcp.eu.ngrok.io"
port = 11340

# MQTT topic
oboroti = "oboroti"

# Function to read and publish OBD data to MQTT
def publish_obd_data():
    while True:
        # Query OBD data
        temperature = connection.query(obd.commands[1][5]).value
        rpm = connection.query(obd.commands[1][12]).value

        # Publish the data to MQTT topics
        mqttc.publish(oboroti, str(temperature)+"C")
        print(f"Published {temperature} to topic: {oboroti}")
        
        mqttc.publish(oboroti, str(rpm)+"RPM")
        print(f"Published {rpm} to topic: {oboroti}")
        
        # Wait before publishing the next data
        time.sleep(3)

# MQTT connection setup
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect(broker_address, port)

# Start MQTT loop in a separate thread
mqttc.loop_start()

# Call the function to read and publish OBD data
publish_obd_data()
