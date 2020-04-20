import logging
import time
import os
import epics

from datetime import datetime, timedelta
from prometheus_client import Summary
from prometheus_client.core import GaugeMetricFamily, REGISTRY



class CollectorConfig(object):
    def __init__(self):
        #https://github.com/aylei/aliyun-exporter/blob/6e2728b3fb90fa3edd794da297f977a34f947cf9/aliyun_exporter/collector.py#L57
