FROM docker.io/python:3.13
WORKDIR /usr/src/cpu-exporter/
RUN pip install --no-cache-dir prometheus_client psutil
COPY ./cpu_exporter.py .
EXPOSE 8000
CMD ["python", "cpu_exporter.py"]
