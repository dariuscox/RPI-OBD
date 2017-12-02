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
def new_speed(r):
    print("Speed: ", r.value.to("mph"), sep=' ', end='\r', flush=True)
def new_ctemp(r):
    print("Coolant Temperature: ", r.value, sep=' ', end='\r', flush=True)
def new_fstat(r):
    print("Fuel Status: ", r.value, sep=' ', end='\r', flush=True)

def main():
    while True:
        uin = input("What would you like to see: ")
        if(uin == "rpm"):
            connection = obd.Async()
            connection.watch(obd.commands.RPM, callback=new_rpm)
            connection.start()
        # the callback will now be fired upon receipt of new values
            time.sleep(60)
            connection.stop()
        if(uin == "speed"):
            connection = obd.Async()
            connection.watch(obd.commands.SPEED, callback=new_speed)
            connection.start()
        # the callback will now be fired upon receipt of new values
            time.sleep(60)
            connection.stop()
        if(uin == "ctemp"):
            connection = obd.Async()
            connection.watch(obd.commands.COOLANT_TEMP, callback=new_ctemp)
            connection.start()
        # the callback will now be fired upon receipt of new values
            time.sleep(60)
            connection.stop()
        if(uin == "fstat"):
            connection = obd.Async()
            connection.watch(obd.commands.FUEL_STATUS, callback=new_fstat)
            connection.start()
        # the callback will now be fired upon receipt of new values
            time.sleep(60)
            connection.stop()
        if(uin == "stop"):
            break
main()
