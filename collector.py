import logging
import time

import os
# import epics

from datetime import datetime, timedelta
from prometheus_client import Summary
from prometheus_client.core import GaugeMetricFamily, REGISTRY


class PvCollector(object):
    def __init__(self, config):
        # self.
        self.systems = config['system']
        for value in self.systems:
            # system = value
            for alert_item in value:
                for pvs in alert_item:
                    alerts = AlertItem(value, alert_item, pvs)


class AlertItem():
    def __init__(self, system, alert_item, pvs):
        self.system = system
        self.alert_item = alert_item
        self.pvs = pvs
        self.last_value = None
        for pv in pvs:
            self.registerPV(pv,alert_item,system)

    def registerPV(self,pv=None, alert_item=None, system=None):
        regpv = epics.PV(pv)
        regpv.add_callback(self.onChanges)

    def onChanges(self, pv=None, value=None, char_value=None, **kw):

        self.last_value = value
        logger.info("PV " + pvname + " value changed to " + str(value))





    def collect(self):
        pass





