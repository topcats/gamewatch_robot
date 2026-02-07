import threading
from util.helper_coding import helper_coding
from util.zWaveApi3 import zWaveApi3 as zWaveApi

class zwavectrl:
    """ APP Lib: ZWave Functions """

    __resettime = 10

    def __init__(self, username, password, url, scenedata):
        """
        Initialize ZWave App Functions

        :param username: ZWave Username
        :type username: string
        :param password: ZWave Password (encoded)
        :type password: string
        :param url: ZWave URL
        :type url: string
        :param scenedata: ZWave Scene ID list
        :type offsceneid: dict
        """
        self.username = username
        self.password = password
        self.url = url
        self.scenedata = scenedata
        self.oZWave = None
        pass


    def __getPassword(self):
        """
        Decrypt ZWave Password

        :return: Decrypted ZWave Password
        :rtype: string
        """
        decryptedpassword = helper_coding().decode(self.password)
        return decryptedpassword


    def __doaction(self, zID):
        """
        Fire ZWave Action

        :param zID: ZWave Device ID
        :type zID: string
        """

        # Check if ZWave API Object already exists, if not create it
        if self.oZWave is None:
            oZWave = zWaveApi(self.username, self.__getPassword(), self.url)

        # Fire ZWave Action
        oZWave.setDeviceCommand(zID, "on")


    def __turnoff(self):
        """
        Turn off ZWave Devices after reset time
        """
        try:
            zID = self.scenedata["off"]
            if zID != "":
                self.__doaction(zID)
        except Exception as e:
            print("Error in ZWave __turnoff: " + str(e))


    def SetLightColour(self, colourname):
        """
        Set Game Light State

        :param colourname: Light colour name
        :type colourname: string

        """
        try:
            zID = self.scenedata[colourname]
            print ("ZWave SetLightColour: " + colourname + " -> " + zID)
            if zID != "":
                self.__doaction(zID)
                threading.Timer(self.__resettime, self.__turnoff).start() 
        except Exception as e:
            print("Error in ZWave SetLightColour: " + str(e))
