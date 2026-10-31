#!/usr/bin/python3
import sys
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

# IMPORTS
from app.conf import appconf
from app.zwavectrl import zwavectrl

# GLOBAL VARIABLES
CONFIG_FILENAME = 'conf/system.json'

# Sub Main for Config
SYSTEM_CONFIG = appconf(CONFIG_FILENAME).loadConfig()

# -- MAIN --

# read arguments
if len(sys.argv) > 1:
    print("Colour argument:", sys.argv[1])
    colourname = sys.argv[1].lower()

    # Fire if enabled
    if (SYSTEM_CONFIG["ZWave"]["enabled"] == True):
        if 'oZWaveCtrl' not in globals():
            oZWaveCtrl = zwavectrl(SYSTEM_CONFIG["ZWave"]["username"], SYSTEM_CONFIG["ZWave"]["password"], SYSTEM_CONFIG["ZWave"]["url"], SYSTEM_CONFIG["zwave-scenes"])

        oZWaveCtrl.SetLightColour(colourname)
