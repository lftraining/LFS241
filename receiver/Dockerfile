FROM docker.io/python:3.13
WORKDIR /usr/src/webhook-receiver/
COPY ./webhook_receiver.py .
EXPOSE 9595
CMD ["python", "webhook_receiver.py"]
