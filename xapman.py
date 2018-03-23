import XAPX00
from copy import copy
channel_data = {"XAP800": {1: {"ig": "I", "og": "O", "itype": "Mic", "otype": "Output"},
                           2: {"ig": "I", "og": "O", "itype": "Mic", "otype": "Output"},
                           3: {"ig": "I", "og": "O", "itype": "Mic", "otype": "Output"},
                           4: {"ig": "I", "og": "O", "itype": "Mic", "otype": "Output"},
                           5: {"ig": "I", "og": "O", "itype": "Mic", "otype": "Output"},
                           6: {"ig": "I", "og": "O", "itype": "Mic", "otype": "Output"},
                           7: {"ig": "I", "og": "O", "itype": "Mic", "otype": "Output"},
                           8: {"ig": "I", "og": "O", "itype": "Mic", "otype": "Output"},
                           9: {"ig": "I", "og": "O", "itype": "Line", "otype": "Output"},
                           10: {"ig": "I", "og": "O", "itype": "Line", "otype": "Output"},
                           11: {"ig": "I", "og": "O", "itype": "Line", "otype": "Output"},
                           12: {"ig": "I", "og": "O", "itype": "Line", "otype": "Output"},
                           "A": {"ig": "P", "og": "P", "itype": "Processing", "otype": "Processing"},
                           "B": {"ig": "P", "og": "P", "itype": "Processing", "otype": "Processing"},
                           "C": {"ig": "P", "og": "P", "itype": "Processing", "otype": "Processing"},
                           "D": {"ig": "P", "og": "P", "itype": "Processing", "otype": "Processing"},
                           "E": {"ig": "P", "og": "P", "itype": "Processing", "otype": "Processing"},
                           "F": {"ig": "P", "og": "P", "itype": "Processing", "otype": "Processing"},
                           "G": {"ig": "P", "og": "P", "itype": "Processing", "otype": "Processing"},
                           "H": {"ig": "P", "og": "P", "itype": "Processing", "otype": "Processing"},
                           "O": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "P": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "Q": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "R": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "S": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "T": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "U": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "V": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "W": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "X": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "Y": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "Z": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"}
                },
                "XAP400": {1: {"ig": "I", "og": "O", "itype": "Mic", "otype": "Output"},
                           2: {"ig": "I", "og": "O", "itype": "Mic", "otype": "Output"},
                           3: {"ig": "I", "og": "O", "itype": "Mic", "otype": "Output"},
                           4: {"ig": "I", "og": "O", "itype": "Mic", "otype": "Output"},
                           5: {"ig": "I", "og": "O", "itype": "Line", "otype": "Output"},
                           6: {"ig": "I", "og": "O", "itype": "Line", "otype": "Output"},
                           7: {"ig": "I", "og": "O", "itype": "Line", "otype": "Output"},
                           8: {"ig": "I", "og": "O", "itype": "Line", "otype": "Output"},
                           "A": {"ig": "P", "og": "P", "itype": "Processing", "otype": "Processing"},
                           "B": {"ig": "P", "og": "P", "itype": "Processing", "otype": "Processing"},
                           "C": {"ig": "P", "og": "P", "itype": "Processing", "otype": "Processing"},
                           "D": {"ig": "P", "og": "P", "itype": "Processing", "otype": "Processing"},
                           "O": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "P": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "Q": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "R": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "S": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "T": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "U": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "V": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "W": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "X": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "Y": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"},
                           "Z": {"ig": "E", "og": "E", "itype": "Expansion", "otype": "Expansion"}
                }}
matrix_y = {"XAP800": {1: None,
                       2: None,
                       3: None,
                       4: None,
                       5: None,
                       6: None,
                       7: None,
                       8: None,
                       9: None,
                       10: None,
                       11: None,
                       12: None,
                       "O": None,
                       "P": None,
                       "Q": None,
                       "R": None,
                       "S": None,
                       "T": None,
                       "U": None,
                       "V": None,
                       "W": None,
                       "X": None,
                       "Y": None,
                       "Z": None,
                       "A": None,
                       "B": None,
                       "C": None,
                       "D": None,
                       "E": None,
                       "F": None,
                       "G": None,
                       "H": None},
            "XAP400": {1: None,
                       2: None,
                       3: None,
                       4: None,
                       5: None,
                       6: None,
                       7: None,
                       8: None,
                       "O": None,
                       "P": None,
                       "Q": None,
                       "R": None,
                       "S": None,
                       "T": None,
                       "U": None,
                       "V": None,
                       "W": None,
                       "X": None,
                       "Y": None,
                       "Z": None,
                       "A": None,
                       "B": None,
                       "C": None,
                       "D": None}
            }

matrix = {"XAP800": {1: copy(copy(matrix_y['XAP800'])),
                     2: copy(matrix_y['XAP800']),
                     3: copy(matrix_y['XAP800']),
                     4: copy(matrix_y['XAP800']),
                     5: copy(matrix_y['XAP800']),
                     6: copy(matrix_y['XAP800']),
                     7: copy(matrix_y['XAP800']),
                     8: copy(matrix_y['XAP800']),
                     9: copy(matrix_y['XAP800']),
                     10: copy(matrix_y['XAP800']),
                     11: copy(matrix_y['XAP800']),
                     12: copy(matrix_y['XAP800']),
                     "O": copy(matrix_y['XAP800']),
                     "P": copy(matrix_y['XAP800']),
                     "Q": copy(matrix_y['XAP800']),
                     "R": copy(matrix_y['XAP800']),
                     "S": copy(matrix_y['XAP800']),
                     "T": copy(matrix_y['XAP800']),
                     "U": copy(matrix_y['XAP800']),
                     "V": copy(matrix_y['XAP800']),
                     "W": copy(matrix_y['XAP800']),
                     "X": copy(matrix_y['XAP800']),
                     "Y": copy(matrix_y['XAP800']),
                     "Z": copy(matrix_y['XAP800']),
                     "A": copy(matrix_y['XAP800']),
                     "B": copy(matrix_y['XAP800']),
                     "C": copy(matrix_y['XAP800']),
                     "D": copy(matrix_y['XAP800']),
                     "E": copy(matrix_y['XAP800']),
                     "F": copy(matrix_y['XAP800']),
                     "G": copy(matrix_y['XAP800']),
                     "H": copy(matrix_y['XAP800'])},
          "XAP400": {1: copy(matrix_y['XAP400']),
                     2: copy(matrix_y['XAP400']),
                     3: copy(matrix_y['XAP400']),
                     4: copy(matrix_y['XAP400']),
                     5: copy(matrix_y['XAP400']),
                     6: copy(matrix_y['XAP400']),
                     7: copy(matrix_y['XAP400']),
                     8: copy(matrix_y['XAP400']),
                     "O": copy(matrix_y['XAP400']),
                     "P": copy(matrix_y['XAP400']),
                     "Q": copy(matrix_y['XAP400']),
                     "R": copy(matrix_y['XAP400']),
                     "S": copy(matrix_y['XAP400']),
                     "T": copy(matrix_y['XAP400']),
                     "U": copy(matrix_y['XAP400']),
                     "V": copy(matrix_y['XAP400']),
                     "W": copy(matrix_y['XAP400']),
                     "X": copy(matrix_y['XAP400']),
                     "Y": copy(matrix_y['XAP400']),
                     "Z": copy(matrix_y['XAP400']),
                     "A": copy(matrix_y['XAP400']),
                     "B": copy(matrix_y['XAP400']),
                     "C": copy(matrix_y['XAP400']),
                     "D": copy(matrix_y['XAP400'])}
          }
matrix_array = {'XAP800': [{"c": 1, "og": "O", "ig": "I"},
                        {"c": 2, "og": "O", "ig": "I"},
                        {"c": 3, "og": "O", "ig": "I"},
                        {"c": 4, "og": "O", "ig": "I"},
                        {"c": 5, "og": "O", "ig": "I"},
                        {"c": 6, "og": "O", "ig": "I"},
                        {"c": 7, "og": "O", "ig": "I"},
                        {"c": 8, "og": "O", "ig": "I"},
                        {"c": 9, "og": "O", "ig": "I"},
                        {"c": 10, "og": "O", "ig": "I"},
                        {"c": 11, "og": "O", "ig": "I"},
                        {"c": 12, "og": "O", "ig": "I"},
                        {"c": "O", "og": "E", "ig": "E"},
                        {"c": "P", "og": "E", "ig": "E"},
                        {"c": "Q", "og": "E", "ig": "E"},
                        {"c": "R", "og": "E", "ig": "E"},
                        {"c": "S", "og": "E", "ig": "E"},
                        {"c": "T", "og": "E", "ig": "E"},
                        {"c": "U", "og": "E", "ig": "E"},
                        {"c": "V", "og": "E", "ig": "E"},
                        {"c": "W", "og": "E", "ig": "E"},
                        {"c": "X", "og": "E", "ig": "E"},
                        {"c": "Y", "og": "E", "ig": "E"},
                        {"c": "Z", "og": "E", "ig": "E"},
                        {"c": "A", "og": "P", "ig": "P"},
                        {"c": "B", "og": "P", "ig": "P"},
                        {"c": "C", "og": "P", "ig": "P"},
                        {"c": "D", "og": "P", "ig": "P"},
                        {"c": "E", "og": "P", "ig": "P"},
                        {"c": "F", "og": "P", "ig": "P"},
                        {"c": "G", "og": "P", "ig": "P"},
                        {"c": "H", "og": "P", "ig": "P"}],
                'XAP400': [{"c": 1, "og": "O", "ig": "I"},
                        {"c": 2, "og": "O", "ig": "I"},
                        {"c": 3, "og": "O", "ig": "I"},
                        {"c": 4, "og": "O", "ig": "I"},
                        {"c": 5, "og": "O", "ig": "I"},
                        {"c": 6, "og": "O", "ig": "I"},
                        {"c": 7, "og": "O", "ig": "I"},
                        {"c": 8, "og": "O", "ig": "I"},
                        {"c": "O", "og": "E", "ig": "E"},
                        {"c": "P", "og": "E", "ig": "E"},
                        {"c": "Q", "og": "E", "ig": "E"},
                        {"c": "R", "og": "E", "ig": "E"},
                        {"c": "S", "og": "E", "ig": "E"},
                        {"c": "T", "og": "E", "ig": "E"},
                        {"c": "U", "og": "E", "ig": "E"},
                        {"c": "V", "og": "E", "ig": "E"},
                        {"c": "W", "og": "E", "ig": "E"},
                        {"c": "X", "og": "E", "ig": "E"},
                        {"c": "Y", "og": "E", "ig": "E"},
                        {"c": "Z", "og": "E", "ig": "E"},
                        {"c": "A", "og": "P", "ig": "P"},
                        {"c": "B", "og": "P", "ig": "P"},
                        {"c": "C", "og": "P", "ig": "P"},
                        {"c": "D", "og": "P", "ig": "P"}]}

class XapConnection(object):
    """Xap Serial Connection Wrapper
    """
    def __repr__(self):
        return "XapConnection: " + self.serial_path

    def __init__(self, serial_path="/dev/ttyUSB0",
                 baudrate=38400,
                 mqtt_path="home/HA/AudioMixers/",
                 device_type="XAP800"):
        self.mqtt_path  = mqtt_path
        self.baudrate   = baudrate
        self.units = []
        self.serial_path = serial_path
        print("Preparing XAP devices to be interrogated")
        self.comms = XAPX00.XAPX00(comPort=serial_path, baudRate=38400, XAPType=device_type)
        self.comms.convertDb = 0
        self.comms.connect()
        self.scanDevices()
        print("Scanning Expansion Bus and allocating channels...")
        self.expansion_bus_allocator = ExpansionBusAllocator(self)
        print("Expansion Bus Status: " + self.expansion_bus_allocator.statusReport())

    def scanDevices(self):
        '''Scan for XAP units'''
        self.units = []
        print("Scanning for devices...")
        delay = self.comms._maxrespdelay
        self.comms._maxrespdelay = 0.1 # reduce timeout delay when searching for non-existant devices
        for u in range(8):
            uid = self.comms.getUniqueId(u)
            if uid != None:
                unit = {'id': str(u), 'UID':uid, 'version':self.comms.getVersion(u), "type": self.comms.getUnitType(u)}
                print("Found " + unit['type'] + " at ID " + unit['id'] + " - " + unit['UID'] + "  Ver. " + unit['version'] )
                self.units.append(XapUnit(self, XAP_unit=u))
        print("Found " + str(len(self.units)) + " units.")
        self.comms._maxrespdelay = delay
        return self.units

    def addChannelRoute(self):
        ''''''
        return

class XapUnit(object):
    """Xap Unit Wrapper
       The following are not implemented;
       Presets, Macros, Serial Strings, Preset/Macro Locking, Master Mode, gateing report
    """
    def __repr__(self):
        return "Unit: " + self.device_type + " (ID " + str(self.device_id) + ")"

    def __init__(self, xap_connection,
                 XAP_unit=0):
        self.connection = xap_connection
        self.comms = xap_connection.comms
        self.device_id = XAP_unit
        self.device_type = xap_connection.comms.getUnitType(XAP_unit)
        self.serial_number = None
        self.FW_version = None
        self.DSP_version = None
        self.label = None
        self.modem_mode = None
        self.modem_pass = None
        self.modem_init_string = None
        self.program_strings = None
        self.safety_mute = None
        self.panel_timeout = None
        self.panel_lockout = None
        self.output_channels = None
        self.input_channels = None
        self.processing_channels = None
        self.expansion_busses = None
        self.refreshData()
        self.scanOutputChannels()
        self.scanInputChannels()
        self.scanExpansionBus()

    def refreshData(self):
        '''Fetch all data XAP Unit'''
        self.getID()
        self.getFW()
        self.getDSP()
        self.getLabel()
        self.getSerialNumber()
        self.getModemMode()
        self.getModemInit()
        self.getModemPass()
        self.getSafetyMute()
        self.getPanelTimeout()
        self.getPanelLock()
        return True

    def scanOutputChannels(self):
        '''Fetch all output channels from Unit'''
        self.output_channels = {}
        if self.device_type == "XAP800":
            r = range(1,13) # XAP800 units have 12 output channels
        else:
            r = range(1, 8)  # XAP400 units have 8 output channels
        for c in r:
            self.output_channels[c] = OutputChannel(self, channel=c)
        return

    def scanInputChannels(self):
        '''Fetch all output channels from Unit'''
        self.input_channels = {}
        if self.device_type == "XAP800":
            r = range(1,13) # XAP800 units have 12 input channels
        else:
            r = range(1, 8)  # XAP400 units have 8 input channels
        for c in r:
            self.input_channels[c] = InputChannel(self, channel=c)
        return

    def scanExpansionBus(self):
        '''Fetch all expansion busses from Unit'''
        self.expansion_busses = {}
        r = ['O', 'P' , 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for c in r:
            self.expansion_busses[c] = ExpansionBus(self, channel=c)
        return

    def getID(self):
        '''Fetch ID from XAP Unit'''
        id = self.comms.getDeviceID(unitCode=self.device_id)
        return id
        
    def getFW(self):
        '''Fetch FW Version from XAP Unit'''
        FW = self.comms.getVersion(unitCode=self.device_id)
        self.FW_version = FW
        return FW
        
    def getDSP(self):
        '''Fetch DSP Version from XAP Unit'''
        DSP = self.comms.getDSPVersion(unitCode=self.device_id)
        self.DSP_version = DSP
        return DSP
        
    def getSerialNumber(self):
        '''Fetch Unique ID from XAP Unit'''
        serial = self.comms.getUniqueId(unitCode=self.device_id)
        self.serial_number = serial
        return serial
        
    def getLabel(self):
        '''Fetch Label from XAP Unit'''
        label = self.comms.getLabel(0, "U", unitCode=self.device_id)
        self.label = label
        return label

    def setLabel(self, label):
        '''Fetch Label from XAP Unit'''
        label = self.comms.setLabel(0, "U", label, unitCode=self.device_id)
        self.label = label
        return label

    def getModemMode(self):
        '''Fetch Modem Mode from XAP Unit'''
        mode = self.comms.getModemMode(unitCode=self.device_id)
        self.modem_mode = mode
        return mode
        
    def setModemMode(self, isEnabled):
        '''Set Modem Mode to XAP Unit'''
        mode = self.comms.setModemMode(isEnabled, unitCode=self.device_id)
        self.modem_mode = mode
        return mode
        
    def getModemInit(self):
        '''Fetch Modem Init String from XAP Unit'''
        string = self.comms.getModemInitString(unitCode=self.device_id)
        self.modem_init_string = string
        return string
        
    def setModemInit(self, string):
        '''Set Modem Init String to XAP Unit'''
        string = self.comms.setModemInitString(string, unitCode=self.device_id)
        self.modem_init_string = string
        return string
        
    def getModemPass(self):
        '''Fetch Modem Init String from XAP Unit'''
        string = self.comms.getModemModePassword(unitCode=self.device_id)
        self.modem_pass = string
        return string
        
    def setModemPass(self, string):
        '''Set Modem Init String to XAP Unit'''
        string = self.comms.setModemModePassword(string, unitCode=self.device_id)
        self.modem_pass = string
        return string
        
    def getSafetyMute(self):
        '''Fetch safety mute status from XAP Unit'''
        status = self.comms.getSafetyMute(unitCode=self.device_id)
        self.safety_mute = status
        return status
        
    def setSafetyMute(self, isEnabled):
        '''Set safety mute status to XAP Unit'''
        status = self.comms.setSafetyMute(isEnabled, unitCode=self.device_id)
        self.safety_mute = status
        return status
        
    def getPanelTimeout(self):
        '''Fetch panel timout in min from XAP Unit'''
        minutes = self.comms.getScreenTimeout(unitCode=self.device_id)
        self.panel_timeout = minutes
        return minutes
        
    def setPanelTimeout(self, minutes):
        '''Set panel timout in min to XAP Unit'''
        minutes = self.comms.setScreenTimeout(minutes, unitCode=self.device_id)
        self.panel_timeout = minutes
        return minutes
        
    def getPanelLock(self):
        '''Fetch panel lock from XAP Unit'''
        status = self.comms.getFrontPanelLock(unitCode=self.device_id)
        self.panel_lockout = status
        return status
        
    def setPanelLock(self, isEnabled):
        '''Set panel lock to XAP Unit'''
        status = self.comms.setFrontPanelLock(isEnabled, unitCode=self.device_id)
        self.panel_lockout = status
        return status

class OutputChannel(object):
    """XAP Output Channel Wrapper"""

    def __repr__(self):
        return "Output: " + str(self.unit.device_id) + ":" + str(self.channel) + " | " + self.label

    def __init__(self, unit, channel):
        self.unit = unit
        self.connection = unit.connection
        self.comms = unit.comms
        self.channel = channel
        self.group = channel_data[unit.device_type][channel]['og']
        self.type = channel_data[unit.device_type][channel]['otype']
        self.gain = None #
        self.prop_gain = None #
        self.gain_min = None #
        self.gain_max = None #
        self.mute = None #
        self.label = None #
        self.sources = None
        self.filters = None
        self.constant_gain = None # Also known as Number of Mics (NOM)
        self.refreshData()

    def refreshData(self):
        '''Fetch all data Channel Data'''
        self.getLabel()
        self.getMaxGain()
        self.getMinGain()
        self.getMute()
        self.getProportionalGain()
        self.getGain()
        return True

    def getLabel(self):
        '''Fetch Label from XAP Unit'''
        label = self.comms.getLabel(self.channel, "O", unitCode=self.unit.device_id)
        self.label = label
        return label
    
    def setLabel(self, label):
        '''Fetch Label from XAP Unit'''
        label = self.comms.setLabel(self.channel, "O", label, unitCode=self.unit.device_id)
        self.label = label
        return label

    def getMaxGain(self):
        '''Fetch Max Gain for Channel'''
        gain_max = self.comms.getMaxGain(self.channel, "O", unitCode=self.unit.device_id)
        self.gain_max = gain_max
        return gain_max

    def setMaxGain(self, gain_max):
        '''Set Max Gain for Channel'''
        gain_max = self.comms.setMaxGain(self.channel, "O", gain_max, unitCode=self.unit.device_id)
        self.gain_max = gain_max
        return gain_max

    def getMinGain(self):
        '''Fetch Max Gain for Channel'''
        gain_min = self.comms.getMinGain(self.channel, "O", unitCode=self.unit.device_id)
        self.gain_min = gain_min
        return gain_min

    def setMinGain(self, gain_min):
        '''Set Max Gain for Channel'''
        gain_min = self.comms.setMinGain(self.channel, "O", gain_min, unitCode=self.unit.device_id)
        self.gain_min = gain_min
        return gain_min

    def getMute(self):
        '''Fetch mute status for Channel'''
        mute = self.comms.getMute(self.channel, "O", unitCode=self.unit.device_id)
        self.mute = mute
        return mute

    def setMute(self, mute):
        '''Set mute status for Channel'''
        mute = self.comms.setMute(self.channel, "O", mute, unitCode=self.unit.device_id)
        self.mute = mute
        return mute

    def getProportionalGain(self):
        '''Fetch gain 0-1 proportional to max_gain for Channel'''
        prop_gain = self.comms.getPropGain(self.channel, "O", unitCode=self.unit.device_id)
        self.prop_gain = prop_gain
        return prop_gain

    def setProportionalGain(self, prop_gain):
        '''Set gain 0-1 proportional to max_gain for Channel'''
        prop_gain = self.comms.setPropGain(self.channel, "O", prop_gain, unitCode=self.unit.device_id)
        self.prop_gain = prop_gain
        return prop_gain

    def getGain(self):
        '''Fetch absolute gain for Channel'''
        gain = self.comms.getGain(self.channel, "O", unitCode=self.unit.device_id)
        self.gain = gain
        return gain

    def setGain(self, gain, isAbsolute=1):
        '''Set absolute gain for Channel'''
        gain = self.comms.setGain(self.channel, "O", gain, unitCode=self.unit.device_id, isAbsolute=isAbsolute)
        self.gain = gain
        return gain

class InputChannel(object):
    """XAP Input Channel Wrapper"""

    def __repr__(self):
        return "Input: " + str(self.unit.device_id) + ":" + str(self.channel) + " | " + self.label

    def __init__(self, unit, channel):
        self.unit = unit
        self.connection = unit.connection
        self.comms = unit.comms
        self.channel = channel
        self.group = channel_data[unit.device_type][channel]['ig']
        self.type = channel_data[unit.device_type][channel]['itype']
        self.gain           = None #
        self.gain_min       = None #
        self.gain_max       = None #
        self.mute           = None #
        self.label          = None #
        self.mic            = None
        self.AGC                = None # True or False - Automatic Gain Control
        self.AGC_target         = None # -30 to 20dB
        self.AGC_threshold      = None # -50 to 0dB
        self.AGC_attack         = None # 0.1 to 10.0s in .1 increments
        self.AGC_gain           = None # 0.0 to 18.0dB
        self.refreshData()

    #         # Microphone Input Only
    #         self.gain_mic           = None
    #         self.phantom_power      = None
    #         self.NC                 = None # True or False - Noise Cancellation
    #         self.NC_depth           = None # 6 to 15dB
    #         self.AEC                = None # True or False - Acoutstic Echo Canceller
    #         self.AEC_PA_reference   = None # None or OutputChannel
    #         self.NLP                = None # False = Off, Soft, Medium, Aggresive - Non-Linear Processing
    #         self.filters            = None # Max 4. List of filters?
    #         self.bypass_filters     = None # True or False
    #         self.gating             = None # False, Manual On, Manual Off
    #         self.gate_holdtime      = None # 0.10 - 8.00s
    #         self.gate_override      = None # True or False
    #         self.gate_ratio         = None # 0-50dB
    #         self.gate_group         = None # 1-4 and A-D (gate group)
    #         self.gate_chairman      = None # True or False
    #         self.gate_attenuation   = None # 0-60dB
    #         self.gate_decay         = None # Slow, Medium, Fast
    #         self.adaptive_ambient   = None # True or False
    #         self.ambient_level      = None # -80.0 to 0.0dB
    #         self.PA_adaptive        = None # True or False

    def refreshData(self):
        '''Fetch all data Channel Data'''
        self.getType()
        self.getLabel()
        self.getMaxGain()
        self.getMinGain()
        self.getMute()
        self.getProportionalGain()
        self.getGain()
        return True

    def getType(self):
        if self.unit.device_type == "XAP800":
            mic_channels = 8 # XAP800 has 8 Mic Channels
        else:
            mic_channels = 4 # XAP400 has 4 Mic Channels
        if self.channel <= mic_channels:
            self.type = "Mic"
            self.mic = True
        else:
            self.type = "Line"
            self.mic = False
        return

    def getLabel(self):
        '''Fetch Label from XAP Unit'''
        label = self.comms.getLabel(self.channel, "I", unitCode=self.unit.device_id)
        self.label = label
        return label

    def setLabel(self, label):
        '''Fetch Label from XAP Unit'''
        label = self.comms.setLabel(self.channel, "I", label, unitCode=self.unit.device_id)
        self.label = label
        return label

    def getMaxGain(self):
        '''Fetch Max Gain for Channel'''
        gain_max = self.comms.getMaxGain(self.channel, "I", unitCode=self.unit.device_id)
        self.gain_max = gain_max
        return gain_max

    def setMaxGain(self, gain_max):
        '''Set Max Gain for Channel'''
        gain_max = self.comms.setMaxGain(self.channel, "I", gain_max, unitCode=self.unit.device_id)
        self.gain_max = gain_max
        return gain_max

    def getMinGain(self):
        '''Fetch Max Gain for Channel'''
        gain_min = self.comms.getMinGain(self.channel, "I", unitCode=self.unit.device_id)
        self.gain_min = gain_min
        return gain_min

    def setMinGain(self, gain_min):
        '''Set Max Gain for Channel'''
        gain_min = self.comms.setMinGain(self.channel, "I", gain_min, unitCode=self.unit.device_id)
        self.gain_min = gain_min
        return gain_min

    def getMute(self):
        '''Fetch mute status for Channel'''
        mute = self.comms.getMute(self.channel, "I", unitCode=self.unit.device_id)
        self.mute = mute
        return mute

    def setMute(self, mute):
        '''Set mute status for Channel'''
        mute = self.comms.setMute(self.channel, "I", mute, unitCode=self.unit.device_id)
        self.mute = mute
        return mute

    def getProportionalGain(self):
        '''Fetch gain 0-1 proportional to max_gain for Channel'''
        prop_gain = self.comms.getPropGain(self.channel, "I", unitCode=self.unit.device_id)
        self.prop_gain = prop_gain
        return prop_gain

    def setProportionalGain(self, prop_gain):
        '''Set gain 0-1 proportional to max_gain for Channel'''
        prop_gain = self.comms.setPropGain(self.channel, "I", prop_gain, unitCode=self.unit.device_id)
        self.prop_gain = prop_gain
        return prop_gain

    def getGain(self):
        '''Fetch absolute gain for Channel'''
        gain = self.comms.getGain(self.channel, "I", unitCode=self.unit.device_id)
        self.gain = gain
        return gain

    def setGain(self, gain, isAbsolute=1):
        '''Set absolute gain for Channel'''
        gain = self.comms.setGain(self.channel, "I", gain, unitCode=self.unit.device_id, isAbsolute=isAbsolute)
        self.gain = gain
        return gain

class MatrixLink(object):
    """XAP Matrix Link Manager"""

    def __repr__(self):
        return "Matrix: "

    def __init__(self, connection, source, dest, gatemode=False):
        self.connection = connection
        self.comms = connection.comms
        self.source = source
        self.dest = dest
        self.gatemode = gatemode
        self.state = None
        self.enabled = False

    def linkChannels(self):
        if self.source.unit != self.dest.unit:
            print("Cannot directly link channels across different units. Use another method.")
            return None
        else:
            if self.gatemode == False:
                if self.source.type == "Mic":
                    self.state = 3 # Gate Off
                else:
                    self.state = 1
            else:
                if self.source.type == "Mic":
                    self.state = 4 # Gate On
                else:
                    self.state = 1
            route = self.comms.setMatrixRouting(inChannel=self.source.channel, inGroup=self.source.group,
                                                outChannel=self.dest.channel, outGroup=self.dest.group,
                                                state=self.state, unitCode=self.dest.unit.device_id)
            if route == self.state:
                self.enabled = True
            else:
                self.enabled = False
        return route

    def unlinkChannels(self):
        self.state = 0
        route = self.comms.setMatrixRouting(inChannel=self.source.channel, inGroup=self.source.group,
                                            outChannel=self.dest.channel, outGroup=self.dest.group,
                                            state=self.state, unitCode=self.dest.unit.device_id)
        self.enabled = False
        return route

class MatrixLink2(object):
    """XAP Matrix Link Manager"""

    def __repr__(self):
        return "Matrix: "

    def __init__(self, connection, source, dest):
        self.connection = connection
        self.comms = connection.comms
        self.source = source
        self.dest = dest
        self.expansion = None

    def linkChannels(self):
        if self.source.unit != self.dest.unit:
            return
            # Check if source is already available on expansion bus
            # If not find free expansion bus and assign
            # Link expansion -> Dest
        else:
            return
            # Link Source -> Dest
        return


class ExpansionBus(object):
    """XAP Expansion Bus Wrapper"""

    def __repr__(self):
        return "ExpansionBus: Channel " + self.channel

    def __init__(self, unit, channel):
        self.unit = unit
        self.connection = unit.connection
        self.comms = unit.comms
        self.input_label = None
        self.output_label = None
        self.channel = channel
        self.inUse = False
        self.refreshData()

    def refreshData(self):
        '''Fetch all data Channel Data'''
        self.getInputLabel()
        self.getOutputLabel()
        return True

    def getInputLabel(self):
        '''Fetch Label from XAP Unit'''
        label = self.comms.getLabel(self.channel, "E", inout=1, unitCode=self.unit.device_id)
        self.input_label = label
        return label

    def setInputLabel(self, label):
        '''Fetch Label from XAP Unit'''
        label = self.comms.setLabel(self.channel, "E", label, inout=1, unitCode=self.unit.device_id)
        self.input_label = label
        return label

    def getOutputLabel(self):
        '''Fetch Label from XAP Unit'''
        label = self.comms.getLabel(self.channel, "E", inout=0, unitCode=self.unit.device_id)
        self.output_label = label
        return label

    def setOutputLabel(self, label):
        '''Fetch Label from XAP Unit'''
        label = self.comms.setLabel(self.channel, "E", label, inout=0, unitCode=self.unit.device_id)
        self.output_label = label
        return label

class ExpansionBusAllocator(object):
        """XAP Input Channel Manager"""

        def __repr__(self):
            return "ExpansionBusAllocator: " + self.statusReport()

        def __init__(self, connection, reserved_channels=None):
            self.connection = connection
            self.comms = connection.comms
            self.reserved_channels = []
            self.buslist = {"O": None, "P": None, "Q": None, "R": None, "S": None, "T": None, "U": None, "V": None, "W": None, "X": None, "Y": None, "Z": None}
            if reserved_channels:
                self.reserved_channels = reserved_channels
                for channel in self.reserved_channels:
                    self.buslist.pop(channel, None)
            for channel, status in self.buslist.items():
                if channel not in self.reserved_channels:
                    if self.getChannelUsage(channel)['inUse']:
                        self.buslist[channel] = True
                    else:
                        self.buslist[channel] = False

        def statusReport(self):
            inUse = 0
            available = 0
            reserved = len(self.reserved_channels)
            for channel, status in self.buslist.items():
                if status == False:
                    available += 1
                elif status == True:
                    inUse += 1
            return "Available: " + str(available) + " InUse: " + str(inUse) + " Reserved: " + str(reserved)

        def getChannelUsage(self, channel):
            inUse = False
            inUseList = []
            for unit in self.connection.units:
                for c in matrix_array[unit.device_type]:
                    if channel == c['c'] and c['og'] == "E":
                        continue
                    if self.comms.getMatrixRouting(inChannel=channel, outChannel=c['c'], inGroup="E", outGroup=c['og'], unitCode=unit.device_id) != "0":
                        inUse = True
                        inUseList.append("Output Unit: " + str(unit.device_id) + " Channel: " + str(c['c']) + " -> ExpansionBus: " + channel)
                    if self.comms.getMatrixRouting(inChannel=c['c'], outChannel=channel, inGroup=c['ig'], outGroup="E", unitCode=unit.device_id) != "0":
                        inUse = True
                        inUseList.append("Input Unit: " + str(unit.device_id) + " Channel: " + str(c['c']) + " -> ExpansionBus: " + channel)
            return {'inUseList': inUseList, 'inUse': inUse}

        def requestExpChannel(self):
            return



#
#
#
#
#
#
#
#
#
# class ProcessingChannel(object):
#     self.label          = None
#     self.delay = None
#     self.mute = None
#     self.compressor = None # True or False
#     self.compressor_group = None #
#     self.compressor_post_gain = None #
#     self.compressor_threshold = None
#     self.compressor_ratio = None
#     self.compressor_attack = None
#     self.compressor_release = None
#     self.filters = None
#     self.delay = None
#     self.gain = None
#
#
# class GatingGroup(object):
#     self.max_mics = None # 1 to 64
#     self.first_mic_priority = None # True or False
#     self.last_mic_mode = None # True, False
#     self.last_mic_group = None # 1-8
#
#
#
# class Filter(object):
#     self.type = None # All Pass, High Pass, Low Pass, Notch, PEQ
#     self.frequency = None
#     self.gain = None
#     self.Q = None
#     self.bandwidth = None
#     self.bypass = None
#     self.phase = None
#