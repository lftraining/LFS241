FROM docker.io/python:3.13
WORKDIR /usr/src/lab-app/
RUN pip install --no-cache-dir prometheus_client
COPY ./server.py .
EXPOSE 12345
CMD ["python","server.py"]