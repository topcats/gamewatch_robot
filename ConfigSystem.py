#!/usr/bin/python3
import sys
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

# IMPORTS
from app.conf import appconf
from util.helper_coding import helper_coding

# GLOBAL VARIABLES
CONFIG_FILENAME = 'conf/system.json'

# Sub Main for Config
SYSTEM_CONFIG = appconf(CONFIG_FILENAME).loadConfig()


def doValueBool(section, key, prompt):
    global SYSTEM_CONFIG
    if key is None:
        if not section in SYSTEM_CONFIG:
            SYSTEM_CONFIG[section] = ''
        existingValue = SYSTEM_CONFIG[section]
    else:
        if not section in SYSTEM_CONFIG:
            SYSTEM_CONFIG[section] = {}
        if not key in SYSTEM_CONFIG[section]:
            SYSTEM_CONFIG[section][key] = None
        existingValue = SYSTEM_CONFIG[section][key]

    newvalue = bool(input(prompt+' ['+str(existingValue)+'] ? ') or existingValue) or None
    if key is None:
        SYSTEM_CONFIG[section] = newvalue
    else:
        SYSTEM_CONFIG[section][key] = newvalue


def doValueInt(section, key, prompt):
    global SYSTEM_CONFIG
    if key is None:
        if not section in SYSTEM_CONFIG:
            SYSTEM_CONFIG[section] = ''
        existingValue = SYSTEM_CONFIG[section]
    else:
        if not section in SYSTEM_CONFIG:
            SYSTEM_CONFIG[section] = {}
        if not key in SYSTEM_CONFIG[section]:
            SYSTEM_CONFIG[section][key] = None
        existingValue = SYSTEM_CONFIG[section][key]

    newvalue = int(input(prompt+' ['+str(existingValue)+'] ? ') or existingValue) or None
    if key is None:
        SYSTEM_CONFIG[section] = newvalue
    else:
        SYSTEM_CONFIG[section][key] = newvalue


def doValueStr(section, key, prompt):
    global SYSTEM_CONFIG
    if key is None:
        if not section in SYSTEM_CONFIG:
            SYSTEM_CONFIG[section] = ''
        existingValue = SYSTEM_CONFIG[section]
    else:
        if not section in SYSTEM_CONFIG:
            SYSTEM_CONFIG[section] = {}
        if not key in SYSTEM_CONFIG[section]:
            SYSTEM_CONFIG[section][key] = None
        existingValue = SYSTEM_CONFIG[section][key]
    # Process Input
    existingValueDisp = existingValue if existingValue is not None else ''
    newvalue = input(prompt+' ['+existingValueDisp+'] ? ') or existingValue
    if key is None:
        SYSTEM_CONFIG[section] = newvalue
    else:
        SYSTEM_CONFIG[section][key] = newvalue


def doValuePwd(section, key, prompt):
    global SYSTEM_CONFIG
    if key is None:
        if not section in SYSTEM_CONFIG:
            SYSTEM_CONFIG[section] = ''
        existingValue = SYSTEM_CONFIG[section]
    else:
        if not section in SYSTEM_CONFIG:
            SYSTEM_CONFIG[section] = {}
        if not key in SYSTEM_CONFIG[section]:
            SYSTEM_CONFIG[section][key] = None
        existingValue = SYSTEM_CONFIG[section][key]
    decryptedpassword = helper_coding().decode(existingValue)
    # Process Input
    newvalue = input(prompt+' [########] ? ') or decryptedpassword
    if key is None:
        SYSTEM_CONFIG[section] = helper_coding().encode(newvalue)
    else:
        SYSTEM_CONFIG[section][key] = helper_coding().encode(newvalue)



print('TheOwls GameWatch Robot Setup')
print('from https://github.com/topcats/gamewatch_robot')
print()

print('Setup config (y) ?')
nulyi = input('')
if nulyi ==  '' or nulyi == 'y':
    #all ok
    print('')
else:
    quit()

#Z-Wave
print('Z-Wave')
doValueBool('ZWave', 'enabled', 'Z-Wave Control Enabled (0 will disable)')
doValueStr('ZWave', 'url', 'Automation API Base URL Address')
doValueStr('ZWave', 'username', 'Username')
doValuePwd('ZWave', 'password', 'Password')

print('Z-Wave - Scenes')
doValueStr('zwave-scenes', 'red', 'Scene Red')
doValueStr('zwave-scenes', 'green', 'Scene Green')
doValueStr('zwave-scenes', 'blue', 'Scene Blue')
doValueStr('zwave-scenes', 'yellow', 'Scene Yellow')
doValueStr('zwave-scenes', 'off', 'Scene Off')


#Save it
print()
print('New Config')
nulyi = input('All Ok (Enter y to save) ?')
if nulyi == 'y':
    appconf(CONFIG_FILENAME).saveConfig(SYSTEM_CONFIG)
    print('Saved')
