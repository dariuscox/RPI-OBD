"""
Daniel Cox
Ryan Lachacz

The main program for RPI - OBD
"""

import obd
from obd import OBDStatus
import time

connection = obd.OBD()
print("Connected")

r =  connection.query(obd.commands.RPM)

if not r.is_null():
    print(r.value)

def new_rpm(r):
    print("RPM: ", r.value, sep=' ', end='\r', flush=True)

uin = input("What would you like to see: ")
if(uin == "rpm"):
    connection = obd.Async()
    connection.watch(obd.commands.RPM, callback=new_rpm)
    connection.start()
# the callback will now be fired upon receipt of new values
    time.sleep(60)
    connection.stop()
