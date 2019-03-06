FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV MQTT_HOST=127.0.0.1
ENV MQTT_PORT=1883
ENV MQTT_ROOT="Home/Audio"
ENV SERIAL_PORT="/dev/tyyS0"
ENV BAUD_RATE=38400
ENV RAMP_RATE=6

CMD [ "python", "./go.py" ]
