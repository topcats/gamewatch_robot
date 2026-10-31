import json
import os

class appconf:
    """ App Lib: Configuration Functions """

    defaultconfig = { "ZWave": {"enabled": False} , "zwave-scenes": { "red": "", "green": "", "blue": "", "yellow": "", "off": "" } }

    def __init__(self, configfile):
        """ Initialize Configuration Functions """
        self.configfile = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'+configfile))
        pass


    def loadConfig(self):
        """
        Load Configuration from JSON file

        :return: Configuration Dictionary
        :rtype: dict
        """
        try:
            with open(self.configfile, 'r') as fp:
                config = json.load(fp)
            return config
        except Exception as e:
            print('disp_conf.loadConfig failed: ' + str(e))
            return self.defaultconfig


    def saveConfig(self, config):
        """
        Save Configuration to JSON file

        :param config: Configuration Dictionary
        :type config: dict
        """
        try:
            with open(self.configfile, 'w') as f:
                json.dump(config, f, indent=4)
        except Exception as e:
            print('disp_conf.saveConfig failed: ' + str(e))
            pass
