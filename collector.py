import logging
import time


import os
#import epics

from datetime import datetime, timedelta
from prometheus_client import Summary
from prometheus_client.core import GaugeMetricFamily, REGISTRY


class PvCollector(object):
    def __init__(self,config):
        #self.
        self.systems = config['system']
        for value in self.systems:
            #system = value
            for alert_item in value:
                for pvs in alert_item:
                    alerts = AlertItem(value,alert_item,pvs)
        





class AlertItem():
    def __init__(self,system,alert_item,pvs):
        self.system = system
        self.alert_item = alert_item
        self.pvs = pvs











    def collect(self):
        pass






