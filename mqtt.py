import paho.mqtt.client as mqtt
import os

MQTT_HOST = os.environ['MQTT_HOST']
MQTT_PORT = os.environ['MQTT_PORT']

class MQTT(mqtt.Client):

    def on_connect(self, mqttc, obj, flags, rc):
        for s in self.subscriptions:
            self.subscribe(s)
        #print("rc: "+str(rc))

    def on_publish(self, mqttc, obj, mid):
        noop = 1
        #print("mid: " + str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        noop = 1
        #print("Subscribed: " + str(mid) + " " + str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        noop = 1
        #print(string)

    def conn(self):
        self.connect(MQTT_HOST, int(MQTT_PORT), 60)

    def run(self):
        self.subscribe("$SYS/#", 0)

        rc = 0
        while rc == 0:
            rc = self.loop()
        return rc

