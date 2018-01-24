# -*- coding: utf-8 -*-
# 15/6/27
# create by: snower

from __future__ import absolute_import, division, print_function, with_statement

import sys
import argparse
import multiprocessing
from ..forsun import Forsun, config

parser = argparse.ArgumentParser(description='High-performance timing scheduling service')
parser.add_argument('--bind', dest='bind_host', default="0.0.0.0", help='bind host (default: 0.0.0.0)')
parser.add_argument('--port', dest='bind_port', default=6458, type=int, help='bind port (default: 6458)')
parser.add_argument('--demon', dest='demon', default=False, type=bool, help='run demon mode')
parser.add_argument('--log', dest='log_file', default='/var/log/forsun.log', type=str, help='log file')
parser.add_argument('--log-level', dest='log_level', default='INFO', type=str, help='log level (defaul: INFO)')
parser.add_argument('--driver', dest='driver', default='redis', type=str, help='store driver (defaul: redis)')
parser.add_argument('--driver-redis-host', dest='driver_redis_host', default='127.0.0.1', type=str, help='store reids driver host (defaul: 127.0.0.1)')
parser.add_argument('--driver-redis-port', dest='driver_redis_port', default=6379, type=int, help='store reids driver port (defaul: 6379)')
parser.add_argument('--driver-redis-db', dest='driver_redis_db', default=0, type=int, help='store reids driver db (defaul: 0)')
parser.add_argument('--driver-redis-prefix', dest='driver_redis_prefix', default='forsun', type=str, help='store reids driver key prefix (defaul: forsun)')
parser.add_argument('--driver-redis-server-id', dest='driver_redis_server_id', default=0, type=int, help='store reids driver server id (defaul: 0)')

def main():
    args = parser.parse_args()

    config.set("LOG_FILE", args.log_file)
    config.set("LOG_LEVEL", args.log_level)

    config.set("BIND_ADDRESS", args.bind_host)
    config.set("PORT", args.bind_port)

    config.set("STORE_DRIVER", args.driver)
    config.set("STORE_REDIS_HOST", args.driver_redis_host)
    config.set("STORE_REDIS_PORT", args.driver_redis_port)
    config.set("STORE_REDIS_DB", args.driver_redis_db)
    config.set("STORE_REDIS_PREFIX", args.driver_redis_prefix)
    config.set("STORE_REDIS_SERVER_ID", args.driver_redis_server_id)

    forsun = Forsun()
    if args.demon:
        multiprocessing.Process(target = forsun.serve, name=" ".join(sys.argv))
    else:
        forsun.serve()

if __name__ == "__main__":
    main()