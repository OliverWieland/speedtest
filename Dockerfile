FROM python:3
RUN pip install paho-mqtt
ADD speedtest2mqtt.py /
ADD speedtest /
RUN chmod +x /speedtest
CMD [ "python", "./speedtest2mqtt.py" ]