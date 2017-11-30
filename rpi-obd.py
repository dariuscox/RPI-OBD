"""
Daniel Cox
Ryan Lachacz

The main program for RPI - OBD
"""

import obd
from obd import OBDStatus

connection = obd.OBD()

if connection.status == OBDStatus.CAR_CONNECTED:
    print ("Success")
else:
    print ("you failed at life")
