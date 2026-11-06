import time
import psutil

from prometheus_client import start_http_server
from prometheus_client.core import CounterMetricFamily, REGISTRY


class CPUCollector(object):
    def collect(self):
        c = CounterMetricFamily(
            'cpu_exporter_cpu_usage_seconds_total',
            'The total number of CPU seconds used per mode.',
            labels=['mode']
        )
        for mode, usage_seconds in psutil.cpu_times()._asdict().items():
            c.add_metric([mode], usage_seconds)
        yield c


REGISTRY.register(CPUCollector())

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        time.sleep(1)
