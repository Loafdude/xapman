import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

class MQTT(mqtt.Client):

    def on_connect(self, mqttc, obj, flags, rc):
        for s in self.subscriptions:
            self.subscribe(s)
        print("rc: "+str(rc))

    def on_publish(self, mqttc, obj, mid):
        print("mid: " + str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    def conn(self):
        self.connect("10.9.8.184", 1883, 60)

    def run(self):
        self.subscribe("$SYS/#", 0)

        rc = 0
        while rc == 0:
            rc = self.loop()
        return rc

