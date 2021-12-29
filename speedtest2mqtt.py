import os
import subprocess
import logging
#import json
import paho.mqtt.client as mqtt

try:
    MQTT_HOST = os.environ['MQTT_HOST']
except KeyError:
    MQTT_HOST = 'localhost'
try:
    MQTT_PORT = os.environ['MQTT_PORT']
except KeyError:
    MQTT_PORT = 1883
try:
    MQTT_TOPIC = os.environ['MQTT_TOPIC']
except KeyError:
    MQTT_TOPIC = 'speedtest'

def call_speedtest():
    logging.info("Performing speedtest")
    speedtest = subprocess.Popen(["./speedtest", "--accept-license", "--accept-gdpr", "-fjson"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = speedtest.communicate()
    out = out.decode("utf8")
    err = err.decode("utf8")

    if out == "":
        logging.info("Speedtest failed with error")
        out = "\"\""
        err = "true"
    else:
        logging.info("Speedtest ok")
        err = "false"
    client.publish(MQTT_TOPIC, "{\"out\":%s, \"err\":\"%s\"}" % (out, err))


def on_connect(client, obj, flacs, rc):
    logging.info("MQTT connected")
    client.publish(MQTT_TOPIC + '/online', True, qos=1, retain=True)
    
def on_message(client, userdata, message):
    logging.info("MQTT message received")

    topic = message.topic
    payload = message.payload.decode("utf-8")
    logging.debug("Topic: %s\nPayload: %s",  topic, payload)
    if topic == "%s/cmd" % MQTT_TOPIC:
        if payload == "true":
            call_speedtest()

logging.basicConfig(level=logging.INFO)
logging.info("Starting speedtest2mqtt")
client = mqtt.Client("speedtest")
client.on_connect=on_connect
client.on_message=on_message
client.will_set(MQTT_TOPIC + '/online', False, qos=1, retain=True)
client.connect(MQTT_HOST, MQTT_PORT)
client.subscribe("%s/cmd" % MQTT_TOPIC)

client.loop_forever()