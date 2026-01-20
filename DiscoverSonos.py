from queue import Empty

import soco
import russound 

from pprint import pprint
from soco.events import event_listener

#device = soco.discovery.by_name('Kitchen')
#sub = device.avTransport.subscribe()

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s: %(message)s"
)


russ = russound.Russound('192.168.1.213', 9621)
russ.connect()
zone = '1'
result = russ.get_source(1, zone)

def startListening():
    while True:
        try:
            event = sub.events.get(timeout=1.0)
            pprint(event.variables)
        except Empty:
            print("Empty")
            pass
        except KeyboardInterrupt:
            sub.unsubscribe()
            event_listener.stop()
            break