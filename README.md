# speedtest2mqtt
Performs a speedtest and returns the results via MQTT

## Prerequisites
- speedtest-cli from Ookla (https://www.speedtest.net/apps/cli)
- A MQTT server (e.g. mosquitto)

## Usage
- set the environment variables (see Dockerfile)
- call the script
- send the payload 'true' to the topic *speedtest/cmd*
- get the results from the topic *speedtest*
