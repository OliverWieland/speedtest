FROM python:3
ADD speedtest2mqtt.py /
ADD speedtest /
RUN chmod +x /speedtest
RUN pip install paho-mqtt
CMD [ "python", "./speedtest2mqtt.py" ]