import logging
import time

import os
import re
# import epics

from datetime import datetime, timedelta
from prometheus_client import Summary
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from epics import caget

class AlertItem(self,sys,item,pv):
    def __init__(self):
        self.systems = sys
        self.alert_item = item
        self.pv = pv
    def set_system(self,sys):
        self.systems = sys
    def set_alert_item(self,item):
        self.alert_item = item
    def set_pv(self,pv):
        self.pv = pv

class PvCollector(object):
    def __init__(self, config):
        self.alerts=[]
        self.systems = config['system']
        for value in self.systems:
            # system = value
            for alert_item in value:
                for pvs in alert_item:
                    alert = AlertItem(value, alert_item, pvs)
                    self.alerts.append(alert)

    def metric_generator(self,alert,value):
        # prometheus metric中只有[a-zA-Z0-9:_]是合法的metric name
        name = alert.pv
        metric_name = re.sub('[^a-zA-Z0-9:_]','_',name) #替换为下划线
        gauge = GaugeMetricFamily(metric_name,['system','alert_item'])
        gauge.add_metric([alert.systems,alert.alert_item],value)
        yield gauge

    def collect(self):
        for alert in self.alerts:
            pv = alert.pv
            try:
                value = epics.caget(pv)
            except:
                logging.error("Failed to get pv value: "+pv)
            yield from metric_generator(alert,value)





# class AlertItem():
#     def __init__(self, system, alert_item, pvs):
#         self.system = system
#         self.alert_item = alert_item
#         self.pvs = pvs
#         self.last_value = None
#         for pv in pvs:
#             self.registerPV(pv,alert_item,system)
#
#     def registerPV(self,pv=None, alert_item=None, system=None):
#         regpv = epics.PV(pv)
#         regpv.add_callback(self.onChanges)
#
#     def onChanges(self, pv=None, value=None, char_value=None, **kw):
#
#         self.last_value = value
#         logger.info("PV " + pvname + " value changed to " + str(value))





