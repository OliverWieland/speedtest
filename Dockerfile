FROM python:3
ADD speedtest.py /
ADD speedtest /
RUN chmod +x /speedtest
RUN pip install paho-mqtt
CMD [ "python", "./speedtest.py" ]