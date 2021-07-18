#!/usr/bin/python3

from threading import Lock
import signal

lock = Lock()
lock.acquire()
signal.signal(signal.SIGTERM, lambda a,b: lock.release())
lock.acquire()
