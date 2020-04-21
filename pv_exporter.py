
import sys
import time
import yaml
import logging
import signal

from pormetheus_client import Counter, Gauge, start_http_server
from prometheus_client.core import CollectorRegistry
from pv_exporter.collector import PvCollector, CollectorConfig

def shutdown():
    logging.info('service shutting down...')
    sys.exit(1)

def signal_handler():
    shutdown()

def main():
    signal.signal(signal.SIGTERM, signal_handler)
    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser(description="epics pv_exporter for Prome theus.")
    parser.add_argument('-c', '--config-file', default='pv_exporter.yml',
                        help='path to configuration file.')
    parser.add_argument('-p', '--port', default=9991,
                        help='exporter exposed port')
    args = parser.parse_args()

    with open(args.config_file, 'r') as config_file:
        cfg = yaml.load(config_file, Loader=yaml.FullLoader)
    #collector_config = CollectorConfig(**cfg)
    collector = PvCollector()






if __name__ == '__main__':
    main()