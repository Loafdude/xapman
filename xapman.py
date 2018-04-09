import XAPX00
from copy import deepcopy

channel_data = {"XAP800": {1: {"ig": "M", "og": "O", "itype": "Mic", "otype": "Output"},
                           2: {"ig": "M", "og": "O", "itype": "Mic", "otype": "Output"},
                           3: {"ig": "M", "og": "O", "itype": "Mic", "otype": "Output"},
                           4: {"ig": "M", "og": "O", "itype": "Mic", "otype": "Output"},
                           5: {"ig": "M", "og": "O", "itype": "Mic", "otype": "Output"},
                           6: {"ig": "M", "og": "O", "itype": "Mic", "otype": "Output"},
                           7: {"ig": "M", "og": "O", "itype": "Mic", "otype": "Output"},
                           8: {"ig": "M", "og": "O", "itype": "Mic", "otype": "Output"},
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
                "XAP400": {1: {"ig": "M", "og": "O", "itype": "Mic", "otype": "Output"},
                           2: {"ig": "M", "og": "O", "itype": "Mic", "otype": "Output"},
                           3: {"ig": "M", "og": "O", "itype": "Mic", "otype": "Output"},
                           4: {"ig": "M", "og": "O", "itype": "Mic", "otype": "Output"},
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

gating_groups = {1: None,
                 2: None,
                 3: None,
                 4: None,
                 "A": None,
                 "B": None,
                 "C": None,
                 "D": None}

local_gating_groups = [1, 2, 3, 4]

filter_data = {"Mic": {1: None,
                       2: None,
                       3: None,
                       4: None},
               "Processing": {1: None,
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
                              13: None,
                              14: None,
                              15: None},
               "Line": None,
               "Expansion": None
               }

filter_types = {None: "Not Configured",
                1: "All Pass",
                2: "Low Pass",
                3: "High Pass",
                4: "Low Shelving",
                5: "High Shelving",
                6: "Parametric EQ",
                7: "CD Horn",
                8: "Bessel Crossover",
                9: "Butterworth Crossover",
                10: "Linkwitz-Riley Crossover",
                11: "Notch"}

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
                       "D": None}}

matrix = {"XAP800": {1: deepcopy(matrix_y['XAP800']),
                     2: deepcopy(matrix_y['XAP800']),
                     3: deepcopy(matrix_y['XAP800']),
                     4: deepcopy(matrix_y['XAP800']),
                     5: deepcopy(matrix_y['XAP800']),
                     6: deepcopy(matrix_y['XAP800']),
                     7: deepcopy(matrix_y['XAP800']),
                     8: deepcopy(matrix_y['XAP800']),
                     9: deepcopy(matrix_y['XAP800']),
                     10: deepcopy(matrix_y['XAP800']),
                     11: deepcopy(matrix_y['XAP800']),
                     12: deepcopy(matrix_y['XAP800']),
                     "O": deepcopy(matrix_y['XAP800']),
                     "P": deepcopy(matrix_y['XAP800']),
                     "Q": deepcopy(matrix_y['XAP800']),
                     "R": deepcopy(matrix_y['XAP800']),
                     "S": deepcopy(matrix_y['XAP800']),
                     "T": deepcopy(matrix_y['XAP800']),
                     "U": deepcopy(matrix_y['XAP800']),
                     "V": deepcopy(matrix_y['XAP800']),
                     "W": deepcopy(matrix_y['XAP800']),
                     "X": deepcopy(matrix_y['XAP800']),
                     "Y": deepcopy(matrix_y['XAP800']),
                     "Z": deepcopy(matrix_y['XAP800']),
                     "A": deepcopy(matrix_y['XAP800']),
                     "B": deepcopy(matrix_y['XAP800']),
                     "C": deepcopy(matrix_y['XAP800']),
                     "D": deepcopy(matrix_y['XAP800']),
                     "E": deepcopy(matrix_y['XAP800']),
                     "F": deepcopy(matrix_y['XAP800']),
                     "G": deepcopy(matrix_y['XAP800']),
                     "H": deepcopy(matrix_y['XAP800'])},
          "XAP400": {1: deepcopy(matrix_y['XAP400']),
                     2: deepcopy(matrix_y['XAP400']),
                     3: deepcopy(matrix_y['XAP400']),
                     4: deepcopy(matrix_y['XAP400']),
                     5: deepcopy(matrix_y['XAP400']),
                     6: deepcopy(matrix_y['XAP400']),
                     7: deepcopy(matrix_y['XAP400']),
                     8: deepcopy(matrix_y['XAP400']),
                     "O": deepcopy(matrix_y['XAP400']),
                     "P": deepcopy(matrix_y['XAP400']),
                     "Q": deepcopy(matrix_y['XAP400']),
                     "R": deepcopy(matrix_y['XAP400']),
                     "S": deepcopy(matrix_y['XAP400']),
                     "T": deepcopy(matrix_y['XAP400']),
                     "U": deepcopy(matrix_y['XAP400']),
                     "V": deepcopy(matrix_y['XAP400']),
                     "W": deepcopy(matrix_y['XAP400']),
                     "X": deepcopy(matrix_y['XAP400']),
                     "Y": deepcopy(matrix_y['XAP400']),
                     "Z": deepcopy(matrix_y['XAP400']),
                     "A": deepcopy(matrix_y['XAP400']),
                     "B": deepcopy(matrix_y['XAP400']),
                     "C": deepcopy(matrix_y['XAP400']),
                     "D": deepcopy(matrix_y['XAP400'])}}


class connect(object):
    """Xap Serial Connection Wrapper
    """
    def __repr__(self):
        return "XapConnection: " + self.serial_path

    def __init__(self, serial_path="/dev/ttyUSB0",
                 baudrate=38400,
                 mqtt_path="home/HA/AudioMixers/",
                 device_type="XAP800",
                 ramp_rate=6,
                 init=True):

        self.mqtt_path = mqtt_path
        self.baudrate = baudrate
        self.ramp_rate = ramp_rate
        self.serial_path = serial_path
        self.initialize = init  # Do not scan devices for data
        self.units = {}
        print("Preparing XAP devices to be interrogated")
        self.comms = XAPX00.XAPX00(comPort=serial_path, baudRate=38400, XAPType=device_type, object=self)
        self.comms.convertDb = 0
        self.comms.connect()
        self.scanDevices()
        print("Scanning Expansion Bus and allocating channels...")
        self.expansion_bus = ExpansionBusManager(self)
        if init:
            print("  ExBus Status: " + self.expansion_bus.statusReport())

    def scanDevices(self):
        """Scan for XAP units"""
        self.units = {}
        print("Scanning for devices...")
        delay = self.comms._maxrespdelay
        self.comms._maxrespdelay = 0.1  # reduce timeout delay when searching for non-existant devices
        for u in range(8):
            self.comms.write_to_object = False
            uid = self.comms.getUniqueId(u)
            if uid != None:
                unit = {'id': str(u), 'UID':uid, 'version':self.comms.getVersion(u), "type": self.comms.getUnitType(u)}
                print("Found " + unit['type'] + " at ID " + unit['id'] + " - " + unit['UID'] + "  Ver. " + unit['version'] )
                self.comms.write_to_object = True
                self.units[u] = XapUnit(self, XAP_unit=u)
                self.units[u].initialize()
        if self.initialize:
            self.comms.write_to_object = True
        print("Found " + str(len(self.units)) + " units.")
        self.comms._maxrespdelay = delay
        return self.units

    def addChannelRoute(self, source, dest):
        """Link Channels - Calculates Expansion Bus if needed
        Tries to use Expansion Bus Efficiently

        Logic:
        Unit 0 Channel 1 to Unit 1 Channel 2
        If source channel is connected to ExBus alone, use that existing channel
        If destination channel is connected to only 1 output, use that existing channel
        Otherwise procure a new channel if available
        """
        if source.unit.device_id == dest.unit.device_id:
            source.unit.matrix[source.channel][dest.channel].linkChannels()
            return "Linked Input: " + str(source.channel) + " to Output: " + str(dest.channel)
        else:
            usable_bus = None
            for exbus in source.getExBus():
                if self.expansion_bus.getChannelUsage(exbus)['input'] == 1:
                    usable_bus = exbus
                    break
            if usable_bus is None:
                for exbus in dest.getExBus():
                    if self.expansion_bus.getChannelUsage(exbus)['output'] == 1:
                        usable_bus = exbus
                        break
            if usable_bus is None:
                usable_bus = self.expansion_bus.requestExpChannel()  # Get a ExBus
                if usable_bus is False:
                    raise NoExpansionBusAvailable("There is no Expansion Bus Channels Available")
            source.unit.matrix[source.channel][usable_bus].linkChannels()
            dest.unit.matrix[usable_bus][dest.channel].linkChannels()
            self.expansion_bus.getChannelUsage(usable_bus)
            return "Linked Input: " + str(source.channel) + " to Output: " + str(dest.channel) + " Via ExBus: " + str(usable_bus)


    def delChannelRoute(self, source, dest):
        """unLink Channels - Releases Expansion Bus if possible"""
        if source.unit.device_id == dest.unit.device_id:
            source.unit.matrix[source.channel][dest.channel].unlinkChannels()
            return "UnLinked Input: " + str(source.channel) + " to Output: " + str(dest.channel)
        else:
            released = ""
            exBus = source.getExBus()
            if self.expansion_bus.getChannelUsage(exBus)['output'] <= 1:
                source.unit.matrix[source.channel][exBus].unlinkChannels()
                released = " Released ExBus: " + str(exBus)
            dest.unit.matrix[exBus][dest.channel].unlinkChannels()
            self.expansion_bus.getChannelUsage(exBus)
            return "UnLinked Input: " + str(source.channel) + " to Output: " + str(dest.channel) + released


class XapUnit(object):
    """Xap Unit Wrapper
       The following are not implemented;
       Presets, Macros, Serial Strings, Preset/Macro Locking, Master Mode, gateing report
    """
    def __repr__(self):
        return "Unit: " + self.device_type + " (ID " + str(self.device_id) + ")"

    def __init__(self, xap_connection, XAP_unit=0):
        self.__setattr__ = self.setattr
        self.connection = xap_connection
        self.comms = xap_connection.comms
        self.device_id = XAP_unit
        self.device_type = xap_connection.comms.getUnitType(XAP_unit)
        self.serial_number = None
        self.FW_version = None
        self.DSP_version = None
        self.label = None
        self.master_mode = None
        self.master_mode_string = None
        self.modem_mode = None
        self.modem_pass = None
        self.modem_init_string = None
        self.baudrate = None
        self.flowcontrol = None
        self.program_strings = None
        self.safety_mute = None
        self.panel_timeout = None
        self.panel_lockout = None
        self.panel_passcode = None
        self.output_channels = None
        self.input_channels = None
        self.processing_channels = None
        self.expansion_busses = None
        self.matrix = None
        self.gating_groups = deepcopy(gating_groups)
        for group, data in self.gating_groups.items():
            self.gating_groups[group] = GatingGroup(group, self.comms, self)

    def setattr(self, name, value):
        print("ding ding")
        print(str(name) + " <- " + str(value))
        super().__setattr__(name, value)

    def initialize(self):
        if self.connection.initialize is True:
            self.refreshData()
            self.scanOutputChannels()
            self.scanInputChannels()
            self.scanMatrix()
            print("  Scanning Output Channels...")
            for id, channel in self.output_channels.items():
                channel.initialize()
            print("  Scanning Input Channels...")
            for id, channel in self.input_channels.items():
                channel.initialize()
            print("  Scanning Matrix...")
            for y, row in self.matrix.items():
                for x, matrix_item in row.items():
                    if matrix_item:
                        matrix_item.initialize()
            print("  Scanning Gating Groups...")
            for group, data in self.gating_groups.items():
                self.gating_groups[group].initialize()

    def refreshData(self):
        """Fetch all data XAP Unit"""
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

    def clearMatrix(self):
        for inChannel, row in self.matrix.items():
            for outChannel, object in row.items():

                if (channel_data[self.device_type][outChannel]['otype'] == "Expansion" or channel_data[self.device_type][outChannel]['otype'] == "Processing") and inChannel == outChannel:
                    continue
                else:
                    if object.state != 0:
                        object.unlinkChannels()
        return

    def scanMatrix(self):
        self.matrix = deepcopy(matrix[self.device_type])
        for inChannel, row in self.matrix.items():
            for outChannel, object in row.items():
                if inChannel == outChannel and channel_data[self.device_type][outChannel]['otype'] != "Output":
                    continue
                else:
                    self.matrix[inChannel][outChannel] = MatrixLink(self.connection, self.input_channels[inChannel],
                                                                    self.output_channels[outChannel])
        return

    def scanOutputChannels(self):
        """Fetch all output channels from Unit"""
        self.output_channels = {}
        for channel, data in channel_data[self.device_type].items():
            self.output_channels[channel] = OutputChannel(self, channel=channel)
        return

    def scanInputChannels(self):
        """Fetch all output channels from Unit"""
        self.input_channels = {}
        for channel, data in channel_data[self.device_type].items():
            self.input_channels[channel] = InputChannel(self, channel=channel)
        return

    def getID(self):
        """Fetch ID from XAP Unit"""
        uid = self.comms.getDeviceID(unitCode=self.device_id)
        return uid
        
    def getFW(self):
        """Fetch FW Version from XAP Unit"""
        FW = self.comms.getVersion(unitCode=self.device_id)
        return FW
        
    def getDSP(self):
        """Fetch DSP Version from XAP Unit"""
        DSP = self.comms.getDSPVersion(unitCode=self.device_id)
        return DSP
        
    def getSerialNumber(self):
        """Fetch Unique ID from XAP Unit"""
        serial = self.comms.getUniqueId(unitCode=self.device_id)
        return serial
        
    def getLabel(self):
        """Fetch Label from XAP Unit"""
        label = self.comms.getLabel(0, "U", unitCode=self.device_id)
        self.label = label
        return label

    def setLabel(self, label):
        """Fetch Label from XAP Unit"""
        label = self.comms.setLabel(0, "U", label, unitCode=self.device_id)
        self.label = label
        return label

    def getModemMode(self):
        """Fetch Modem Mode from XAP Unit"""
        mode = self.comms.getModemMode(unitCode=self.device_id)
        return mode
        
    def setModemMode(self, isEnabled):
        """Set Modem Mode to XAP Unit"""
        mode = self.comms.setModemMode(isEnabled, unitCode=self.device_id)
        return mode
        
    def getModemInit(self):
        """Fetch Modem Init String from XAP Unit"""
        string = self.comms.getModemInitString(unitCode=self.device_id)
        return string
        
    def setModemInit(self, string):
        """Set Modem Init String to XAP Unit"""
        string = self.comms.setModemInitString(string, unitCode=self.device_id)
        return string
        
    def getModemPass(self):
        """Fetch Modem Init String from XAP Unit"""
        string = self.comms.getModemModePassword(unitCode=self.device_id)
        return string
        
    def setModemPass(self, string):
        """Set Modem Init String to XAP Unit"""
        string = self.comms.setModemModePassword(string, unitCode=self.device_id)
        return string
        
    def getSafetyMute(self):
        """Fetch safety mute status from XAP Unit"""
        status = self.comms.getSafetyMute(unitCode=self.device_id)
        return status
        
    def setSafetyMute(self, isEnabled):
        """Set safety mute status to XAP Unit"""
        status = self.comms.setSafetyMute(isEnabled, unitCode=self.device_id)
        return status
        
    def getPanelTimeout(self):
        """Fetch panel timout in min from XAP Unit"""
        minutes = self.comms.getScreenTimeout(unitCode=self.device_id)
        return minutes
        
    def setPanelTimeout(self, minutes):
        """Set panel timout in min to XAP Unit"""
        minutes = self.comms.setScreenTimeout(minutes, unitCode=self.device_id)
        return minutes
        
    def getPanelLock(self):
        """Fetch panel lock from XAP Unit"""
        status = self.comms.getFrontPanelLock(unitCode=self.device_id)
        return status
        
    def setPanelLock(self, isEnabled):
        """Set panel lock to XAP Unit"""
        status = self.comms.setFrontPanelLock(isEnabled, unitCode=self.device_id)
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
        self.ramp_rate = self.connection.ramp_rate
        self.gain = None
        self.gain_string = None
        self.gain_min = None
        self.gain_min_string = None
        self.gain_max = None
        self.gain_max_string = None
        self.number_of_mic_attenuation = None
        self.mute = None
        self.label = None
        self.level = None
        self.level_metering_point = None
        self.sources = None
        self.filters = None
        self.exBus = None
        self.constant_gain = None # Also known as Number of Mics (NOM)

    def initialize(self):
        """Fetch all data Channel Data"""
        self.getLabel()
        self.getMaxGain()
        self.getMinGain()
        self.getMute()
        self.getGain()
        return True

    def getLabel(self):
        """Fetch Label from XAP Unit"""
        label = self.comms.getLabel(self.channel, channel_data[self.unit.device_type][self.channel]['og'],
                                    unitCode=self.unit.device_id, inout=0)
        self.label = label
        return label
    
    def setLabel(self, label):
        """Fetch Label from XAP Unit"""
        label = self.comms.setLabel(self.channel, channel_data[self.unit.device_type][self.channel]['og'], label,
                                    unitCode=self.unit.device_id, inout=0)
        self.label = label
        return label

    def getMaxGain(self):
        """Fetch Max Gain for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        gain_max = self.comms.getMaxGain(self.channel, channel_data[self.unit.device_type][self.channel]['og'], unitCode=self.unit.device_id)
        return gain_max

    def setMaxGain(self, gain_max):
        """Set Max Gain for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        gain_max = self.comms.setMaxGain(self.channel, channel_data[self.unit.device_type][self.channel]['og'], gain_max, unitCode=self.unit.device_id)
        return gain_max

    def getMinGain(self):
        """Fetch Max Gain for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        gain_min = self.comms.getMinGain(self.channel, channel_data[self.unit.device_type][self.channel]['og'], unitCode=self.unit.device_id)
        return gain_min

    def setMinGain(self, gain_min):
        """Set Max Gain for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        gain_min = self.comms.setMinGain(self.channel, channel_data[self.unit.device_type][self.channel]['og'], gain_min, unitCode=self.unit.device_id)
        return gain_min

    def getMute(self):
        """Fetch mute status for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        mute = self.comms.getMute(self.channel, channel_data[self.unit.device_type][self.channel]['og'], unitCode=self.unit.device_id)
        return mute

    def setMute(self, mute):
        """Set mute status for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        mute = self.comms.setMute(self.channel, channel_data[self.unit.device_type][self.channel]['og'], mute, unitCode=self.unit.device_id)
        return mute

    def setProportionalGain(self, prop_gain):
        """Set gain 0-1 proportional to max_gain for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        prop_gain = self.comms.setPropGain(self.channel, channel_data[self.unit.device_type][self.channel]['og'], prop_gain, unitCode=self.unit.device_id)
        return prop_gain

    def rampToDb(self, targetDb, rate=False):
        """Ramp Gain to specified DB"""
        if not rate:
            rate = self.ramp_rate
        ramp = self.comms.ramp(self.channel, self.group, rate, targetDb)
        return ramp

    def rampToPercent(self, targetPercent, rate=False):
        """Ramp Gain to specified % between min and max gain"""
        if not rate:
            rate = self.ramp_rate
        if targetPercent < 0 or targetPercent > 1:
            raise NotSupported("Percentage must be between 0 and 1")
        targetDb = (self.gain_max - self.gain_min) * targetPercent
        ramp = self.comms.ramp(self.channel, self.group, rate, targetDb)
        return ramp

    def getGain(self):
        """Fetch absolute gain for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        gain = self.comms.getGain(self.channel, channel_data[self.unit.device_type][self.channel]['og'], unitCode=self.unit.device_id)
        return gain

    def setGain(self, gain, isAbsolute=1):
        """Set absolute gain for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        gain = self.comms.setGain(self.channel, channel_data[self.unit.device_type][self.channel]['og'], gain, unitCode=self.unit.device_id, isAbsolute=isAbsolute)
        return gain

    def getExBus(self):
        exBus = []
        for channel, data in channel_data[self.unit.device_type].items():
            if data['otype'] == "Expansion":
                if self.unit.matrix[channel][self.channel] is not None:
                    if self.unit.matrix[channel][self.channel].enabled:
                        exBus.append(channel)
        self.exBus = exBus
        return exBus


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
        self.gain = None
        self.gain_string = None
        self.gain_min = None
        self.gain_max = None
        self.gain_min_string = None
        self.gain_max_string = None
        self.mute = None
        self.label = None
        self.level = None
        self.mic = None
        self.exBus = None
        self.AGC = None  # True or False - Automatic Gain Control
        self.AGC_target = None  # -30 to 20dB
        self.AGC_threshold = None  # -50 to 0dB
        self.AGC_attack = None  # 0.1 to 10.0s in .1 increments
        self.AGC_gain = None  # 0.0 to 18.0dB
        self.AGC_target_string = None  # -30 to 20dB
        self.AGC_threshold_string = None  # -50 to 0dB
        self.AGC_attack_string = None  # 0.1 to 10.0s in .1 increments
        self.AGC_gain_string = None  # 0.0 to 18.0dB
        self.filters = deepcopy(filter_data[self.type])

    # Microphone Input Only
        self.phantom_power = None
        self.NC = None  # True or False - Noise Cancellation
        self.NC_depth = None  # 6 to 15dB
        self.AEC = None  # True or False - Acoutstic Echo Canceller
        self.AEC_PA_reference = None  # None or OutputChannel
        self.NLP = None  # False = Off, Soft, Medium, Aggresive - Non-Linear Processing
        self.NLP_string = None  # False = Off, Soft, Medium, Aggresive - Non-Linear Processing
        self.adaptive_ambient = None  # True or False
        self.ambient_level = None  # -80.0 to 0.0dB
        self.ambient_level_string = None  # -80.0 to 0.0dB
        self.PA_adaptive = None  # True or False
        self.gating = None  # False, Manual On, Manual Off
        self.gating_string = None
        self.gate_holdtime = None  # 0.10 - 8.00s
        self.gate_holdtime_string = None  # 0.10 - 8.00s
        self.gate_override = None  # True or False
        self.gate_ratio = None  # 0-50dB
        self.gate_open = None  # True False
        self.gate_group = None  # 1-4 and A-D (gate group)
        self.gate_chairman = None  # True or False
        self.gate_decay = None  # Slow, Medium, Fast
        self.gate_decay_string = None  # Slow, Medium, Fast
        self.gain_coarse = None
        self.gain_coarse_string = None
        self.gate_attenuation = None  # 0-60dB
        self.gate_attenuation_string = None  # 0-60dB

    # Processing Input Only
        self.delay = None
        self.delay_time_string = None
        self.delay_time = None
        self.compressor = None # True or False
        self.compressor_group = None #
        self.compressor_gain = None #
        self.compressor_threshold = None
        self.compressor_ratio = None
        self.compressor_attack = None
        self.compressor_release = None
        self.compressor_gain_string = None #
        self.compressor_threshold_string = None
        self.compressor_ratio_string = None
        self.compressor_attack_string = None
        self.compressor_release_string = None

    def initialize(self):
        """Fetch all data Channel Data"""
        self.getLabel()
        self.getMaxGain()
        self.getMinGain()
        self.getMute()
        self.getProportionalGain()
        self.getGain()
        self.getAGC()
        self.getAGCLevels()
        if self.filters:
            for node, filter in self.filters.items():
                self.filters[node] = Filter(self.unit, self, node)
        if self.type == "Mic":
            self.getPhantomPower()
            self.getNoiseCancellation()
            self.getNoiseCancellationDepth()
            self.getAutoEchoCanceller()
            self.getReferenceChannel()
            self.getNLP()
            self.getAdaptiveAmbient()
            self.getAmbientLevel()
            self.getPAAdaptive()
            self.getGateMode()
            self.getGateHoldTime()
            self.getGateOverride()
            self.getGateRatio()
            self.getGateGroup()
            self.getChairmanOverride()
            self.getGateDecay()
            self.getCoarseGain()
        elif self.type == "Processing":
            self.getCompressor()
            self.getCompressorGroup()
            self.getCompressorStatus()
            self.getDelayStatus()
            self.getDelay()
        return True

    def getLabel(self):
        """Fetch Label from XAP Unit"""
        label = self.comms.getLabel(self.channel, self.group,
                                    unitCode=self.unit.device_id, inout=1)
        self.label = label
        return label

    def setLabel(self, label):
        """Fetch Label from XAP Unit"""
        label = self.comms.setLabel(self.channel, self.group, label,
                                    unitCode=self.unit.device_id, inout=1)
        self.label = label
        return label

    def getMaxGain(self):
        """Fetch Max Gain for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        gain_max = self.comms.getMaxGain(self.channel, self.group, unitCode=self.unit.device_id)
        return gain_max

    def setMaxGain(self, gain_max):
        """Set Max Gain for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        gain_max = self.comms.setMaxGain(self.channel, self.group, gain_max, unitCode=self.unit.device_id)
        return gain_max

    def getMinGain(self):
        """Fetch Max Gain for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        gain_min = self.comms.getMinGain(self.channel, self.group, unitCode=self.unit.device_id)
        return gain_min

    def setMinGain(self, gain_min):
        """Set Max Gain for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        gain_min = self.comms.setMinGain(self.channel, self.group, gain_min, unitCode=self.unit.device_id)
        return gain_min

    def getMute(self):
        """Fetch mute status for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        mute = self.comms.getMute(self.channel, self.group, unitCode=self.unit.device_id)
        return mute

    def setMute(self, mute):
        """Set mute status for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        mute = self.comms.setMute(self.channel, self.group, mute, unitCode=self.unit.device_id)
        return mute

    def getProportionalGain(self):
        """Fetch gain 0-1 proportional to max_gain for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        prop_gain = self.comms.getPropGain(self.channel, self.group, unitCode=self.unit.device_id)
        return prop_gain

    def setProportionalGain(self, prop_gain):
        """Set gain 0-1 proportional to max_gain for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        prop_gain = self.comms.setPropGain(self.channel, self.group, prop_gain, unitCode=self.unit.device_id)
        return prop_gain

    def getGain(self):
        """Fetch absolute gain for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        gain = self.comms.getGain(self.channel, self.group, unitCode=self.unit.device_id)
        return gain

    def setGain(self, gain, isAbsolute=1):
        """Set absolute gain for Channel"""
        if self.group == "E":  # Expansion Bus is Not Compatible with this function
            return None
        gain = self.comms.setGain(self.channel, self.group, gain, unitCode=self.unit.device_id, isAbsolute=isAbsolute)
        return gain

    def getAGC(self):
        """Fetch Automatic Gain Control for Channel"""
        if self.group == "E" or self.group == "P":  # Expansion Bus & Processing are Not Compatible with this function
            return None
        AGC = self.comms.getAutoGainControl(self.channel, group=self.group, unitCode=self.unit.device_id)
        return AGC

    def setAGC(self, AGC):
        """Set Automatic Gain Control for Channel"""
        if self.group == "E" or self.group == "P":  # Expansion Bus & Processing are Not Compatible with this function
            return None
        AGC = self.comms.setAutoGainControl(self.channel, AGC, group=self.group, unitCode=self.unit.device_id)
        return AGC

    def getAGCLevels(self):
        """Fetch Automatic Gain Control for Channel"""
        if self.group == "E" or self.group == "P":  # Expansion Bus & Processing are Not Compatible with this function
            return None
        AGC = self.comms.getAutoGainControlLevel(self.channel, group=self.group, unitCode=self.unit.device_id)
        return AGC

    def setAGCLevels(self, threshold, target, attack, gain):
        """Set Automatic Gain Control for Channel"""
        if self.group == "E" or self.group == "P":  # Expansion Bus & Processing are Not Compatible with this function
            return None
        AGC = self.comms.setAutoGainControlLevel(self.channel, threshold, target, attack, gain, group=self.group, unitCode=self.unit.device_id)
        return AGC

    def getPhantomPower(self):
        """Fetch Phantom Power for Channel"""
        if channel_data[self.unit.device_type][self.channel]['itype'] != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        pp = self.comms.getPhantomPower(self.channel, unitCode=self.unit.device_id)
        return pp

    def setPhantomPower(self, isEnabled):
        """Set Phantom Power for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        pp = self.comms.setPhantomPower(self.channel, isEnabled, unitCode=self.unit.device_id)
        return pp

    def getNoiseCancellation(self):
        """Fetch Noise Cancellation for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        nc = self.comms.getNoiseCancellation(self.channel, self.group, unitCode=self.unit.device_id)
        return nc

    def setNoiseCancellation(self, isEnabled):
        """Set Noise Cancellation for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        nc = self.comms.setNoiseCancellation(self.channel, self.group, isEnabled, unitCode=self.unit.device_id)
        return nc

    def getNoiseCancellationDepth(self):
        """Fetch Noise Cancellation for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        nc = self.comms.getNoiseCancellationDepth(self.channel, self.group, unitCode=self.unit.device_id)
        return nc

    def setNoiseCancellationDepth(self, depth):
        """Set Noise Cancellation for Channel
        depth - 6-15dB
        """
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        nc = self.comms.setNoiseCancellationDepth(self.channel, self.group, depth, unitCode=self.unit.device_id)
        return nc

    def getAutoEchoCanceller(self):
        """Fetch AEC for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        aec = self.comms.getEchoCanceller(self.channel, unitCode=self.unit.device_id)
        return aec

    def setAutoEchoCanceller(self, isEnabled):
        """Set AEC for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        aec = self.comms.setEchoCanceller(self.channel, isEnabled, unitCode=self.unit.device_id)
        return aec

    def getReferenceChannel(self):
        """Fetch Reference Channel - Used for AEC and PA"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        rc = self.comms.getMicEchoCancellerReferenceOutput(self.channel, unitCode=self.unit.device_id)
        return rc

    def setReferenceChannel(self, ref_channel):
        """Set Reference Channel - Used for AEC and PA"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        if ref_channel.unit.device_id != self.unit.device_id:
            raise NotSupported("Cannot reference channel on another unit")
        rc = self.comms.setMicEchoCancellerReferenceOutput(self.channel, ref_channel.group, ref_channel.channel, unitCode=self.unit.device_id)
        return self.AEC_PA_reference

    def getNLP(self):
        """Fetch NLP for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        nlp = self.comms.getNonlinearProcessingMode(self.channel, unitCode=self.unit.device_id)
        return nlp

    def setNLP(self, mode):
        """Set NLP for Channel"""
        if channel_data[self.unit.device_type][self.channel]['itype'] != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        if str(mode) not in ['0', '1', '2', '3']:
            raise NotSupported("Invalid Mode (" + str(mode) + ")")
        nlp = self.comms.setNonlinearProcessingMode(self.channel, mode, unitCode=self.unit.device_id)
        return nlp

    def getAdaptiveAmbient(self):
        """Fetch Adaptive Ambient for Channel"""
        if channel_data[self.unit.device_type][self.channel]['itype'] != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        aa = self.comms.getAdaptiveAmbient(self.channel, unitCode=self.unit.device_id)
        return aa

    def setAdaptiveAmbient(self, isEnabled):
        """Set Adaptive Ambient for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        aa = self.comms.setAdaptiveAmbient(self.channel, isEnabled, unitCode=self.unit.device_id)
        return aa

    def getAmbientLevel(self):
        """Fetch Ambient Level for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        aa = self.comms.getAmbientLevel(self.channel, unitCode=self.unit.device_id)
        return aa

    def setAmbientLevel(self, level):
        """Set Ambient Level for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        aa = self.comms.setAmbientLevel(self.channel, level, unitCode=self.unit.device_id)
        return aa

    def getPAAdaptive(self):
        """Fetch PA Adaptive Mode for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        paa = self.comms.getPaAdaptiveMode(self.channel, unitCode=self.unit.device_id)
        return paa

    def setPAAdaptive(self, level):
        """Set PA Adaptive Mode for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        paa = self.comms.setPaAdaptiveMode(self.channel, level, unitCode=self.unit.device_id)
        return paa

    def getGateMode(self):
        """Fetch Gate Mode for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        gmode = self.comms.getGatingMode(self.channel, unitCode=self.unit.device_id)
        return gmode

    def setGateMode(self, mode):
        """Set Gate Mode for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        if str(mode) not in ['1', '2', '3']:
            raise NotSupported("Invalid Mode")
        gmode = self.comms.setGatingMode(self.channel, mode, unitCode=self.unit.device_id)
        return gmode

    def getGateHoldTime(self):
        """Fetch Gate Hold Time for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        gmode = self.comms.getHoldTime(self.channel, unitCode=self.unit.device_id)
        return gmode

    def setGateHoldTime(self, time):
        """Set Gate Hold Time for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        if float(time) > 8 or float(time) < 0.1:
            raise NotSupported("Time must be between 0.10 and 8.00s")
        hold = self.comms.setHoldTime(self.channel, time, unitCode=self.unit.device_id)
        return hold

    def getGateOverride(self):
        """Fetch Gate Override for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        override = self.comms.getGatingOverride(self.channel, unitCode=self.unit.device_id)
        return override

    def setGateOverride(self, isEnabled):
        """Set Gate Override for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        ratio = self.comms.setGatingOverride(self.channel, isEnabled, unitCode=self.unit.device_id)
        return ratio

    def getGateRatio(self):
        """Fetch Gate Ratio for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        ratio = self.comms.getGateRatio(self.channel, unitCode=self.unit.device_id)
        return ratio

    def setGateRatio(self, ratio):
        """Set Gate Ratio for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        ratio = self.comms.setGateRatio(self.channel, ratio, unitCode=self.unit.device_id)
        return ratio

    def getGateGroup(self):
        """Fetch Gate Group for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        group = self.comms.getGatingGroup(self.channel, unitCode=self.unit.device_id)
        return group

    def setGateGroup(self, group):
        """Set Gate Group for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        if str(group) not in ['1', '2', '3', '4', 'A', 'B', 'C', 'D']:
            raise NotSupported("Invalid Group")
        group = self.comms.setGatingGroup(self.channel, group, unitCode=self.unit.device_id)
        return group

    def getChairmanOverride(self):
        """Fetch Chairman Override for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        chairman = self.comms.getChairmanOverride(self.channel, unitCode=self.unit.device_id)
        return chairman

    def setChairmanOverride(self, isEnabled):
        """Set Chairman Override for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        chairman = self.comms.setChairmanOverride(self.channel, isEnabled, unitCode=self.unit.device_id)
        return chairman

    def getGateDecay(self):
        """Fetch Gate Decay for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        decay = self.comms.getDecayRate(self.channel, unitCode=self.unit.device_id)
        return self.gate_decay_string

    def setGateDecay(self, mode):
        """Set Gate Decay for Channel"""
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        if str(mode) not in ['1', '2', '3']:
            raise NotSupported("Invalid Mode")
        decay = self.comms.setDecayRate(self.channel, mode, unitCode=self.unit.device_id)
        return self.gate_decay_string

    def getCoarseGain(self, help=False, translation=False):
        if help:
            return ("Coarse Gain\n"
                    "Only supported by Mic channels\n"
                    "This command sets the coarse gain adjustment on the input channels 1-8.\n"
                    "The three returns are (0) 0dB, (2) 25dB, and (1) 55dB.")
        if translation:
            return {"unit": "dB", 'type': "replacement", 0: "0", 1: "55", 2: "25"}
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        gain_coarse = self.comms.getMicInputGain(self.channel, unitCode=self.unit.device_id)
        return gain_coarse

    def setCoarseGain(self, mode, help=False, translation=False):
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        if str(mode) not in ['0', '1', '2']:
            raise NotSupported("Invalid Mode")
        gain_coarse = self.comms.setMicInputGain(self.channel, mode, unitCode=self.unit.device_id)
        return gain_coarse

    def getGateAttenuation(self, help=False, translation=False):
        if help:
            return ("Gate Attenuation\n"
                    "Only supported by Mic channels\n"
                    "This command reports the gated off attenuation value for a mic channel.\r"
                    "Valid values range from 0dB to 50dB")
        if translation:
            return {"unit": "dB", 'type': "value", "min": 0, 'max': 50, 'increments': 1}
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        gate_attenuation = self.comms.getOffAttenuation(self.channel, unitCode=self.unit.device_id)
        return gate_attenuation

    def setGateAttenuation(self, value):
        if self.type != "Mic":  # Only Mics are Compatible with this function
            raise NotSupported("Only MIC channels support this function")
        if value > 50 or value < 0:
            raise NotSupported("Value must range between 0 and 50")
        gate_attenuation = self.comms.setOffAttenuation(self.channel, value, unitCode=self.unit.device_id)
        return gate_attenuation

    def getDelay(self):
        """Get Delay for Channel"""
        if self.type != "Processing":  # Only Processing Channels are Compatible with this function
            raise NotSupported("Only Processing channels support this function")
        delay = self.comms.getDelay(self.channel, unitCode=self.unit.device_id)
        return delay

    def setDelay(self, delay):
        """Set Delay for Channel"""
        if self.type != "Processing":  # Only Processing Channels are Compatible with this function
            raise NotSupported("Only Processing channels support this function")
        delay = self.comms.setDelay(self.channel, delay, unitCode=self.unit.device_id)
        return delay

    def getDelayStatus(self):
        """Get Delay for Channel"""
        if self.type != "Processing":  # Only Processing Channels are Compatible with this function
            raise NotSupported("Only Processing channels support this function")
        delay = self.comms.getDelayStatus(self.channel, unitCode=self.unit.device_id)
        return delay

    def setDelayStatus(self, isEnabled):
        """Set Delay for Channel"""
        if self.type != "Processing":  # Only Processing Channels are Compatible with this function
            raise NotSupported("Only Processing channels support this function")
        delay = self.comms.setDelayStatus(self.channel, isEnabled, unitCode=self.unit.device_id)
        return delay

    def getCompressorStatus(self):
        """Get Compressor Status for Channel"""
        if self.type != "Processing":  # Only Processing Channels are Compatible with this function
            raise NotSupported("Only Processing channels support this function")
        comp = self.comms.getCompressorStatus(self.channel, unitCode=self.unit.device_id)
        return comp

    def setCompressorStatus(self, isEnabled):
        """Set Compressor Status for Channel"""
        if self.type != "Processing":  # Only Processing Channels are Compatible with this function
            raise NotSupported("Only Processing channels support this function")
        comp = self.comms.setCompressorStatus(self.channel, isEnabled, unitCode=self.unit.device_id)
        return comp

    def getCompressorGroup(self):
        """Get Compressor Group for Channel"""
        if self.type != "Processing":  # Only Processing Channels are Compatible with this function
            raise NotSupported("Only Processing channels support this function")
        comp = self.comms.getCompressorGroup(self.channel, unitCode=self.unit.device_id)
        if comp is 0:
            comp = None
        return comp

    def setCompressorGroup(self, group):
        """Set Compressor Group for Channel"""
        if self.type != "Processing":  # Only Processing Channels are Compatible with this function
            raise NotSupported("Only Processing channels support this function")
        if group is None:
            group = 0
        comp = self.comms.setCompressorGroup(self.channel, group, unitCode=self.unit.device_id)
        if comp is 0:
            comp = None
        return comp

    def getCompressor(self):
        if self.type != "Processing":  # Only Processing Channels are Compatible with this function
            raise NotSupported("Only Processing channels support this function")
        comp = self.comms.getCompressor(self.channel, unitCode=self.unit.device_id)
        return comp

    def setCompressor(self, threshold, ratio, attack, release, gain):
        if self.type != "Processing":  # Only Processing Channels are Compatible with this function
            raise NotSupported("Only Processing channels support this function")
        comp = self.comms.setCompressor(self.channel, threshold, ratio, attack, release, gain, unitCode=self.unit.device_id)
        return comp

    def getExBus(self):
        exBus = []
        for channel, data in channel_data[self.unit.device_type].items():
            if data['itype'] == "Expansion":
                if self.unit.matrix[self.channel][channel] is not None:
                    if self.unit.matrix[self.channel][channel].enabled:
                        exBus.append(channel)
        self.exBus = exBus
        return exBus


class MatrixLink(object):
    """XAP Matrix Link Manager"""

    def __repr__(self):
        if self.state == "0":
            return "Matrix: OFF"
        elif self.state == "1":
            return "Matrix: ON"
        elif self.state == "3":
            return "Matrix: ON"
        elif self.state == "4":
            return "Matrix: GATED-ON"

    def __init__(self, connection, source, dest, gatemode=False):
        self.connection = connection
        self.comms = connection.comms
        self.source = source
        self.dest = dest
        self.gatemode = None
        self.type = None
        self.state = None
        self.attenuation = None
        self.attenuation_string = None
        self.enabled = False

    def initialize(self):
        self.getStatus()
        self.getAttenuation()

    def getType(self):
        if self.state == "0":
            self.type = "OFF"
        elif self.state == "1" or self.state == "3":
            self.type = "ON"
        elif self.state == "4":
            self.type = "GATED"
        return self.type

    def getStatus(self):
        state = self.comms.getMatrixRouting(inChannel=self.source.channel, inGroup=self.source.group,
                                            outChannel=self.dest.channel, outGroup=self.dest.group,
                                            unitCode=self.dest.unit.device_id)
        return state

    def getAttenuation(self):
        attn = self.comms.getMatrixLevel(inChannel=self.source.channel, inGroup=self.source.group,
                                         outChannel=self.dest.channel, outGroup=self.dest.group,
                                         unitCode=self.dest.unit.device_id)
        return

    def setAttenuation(self, level):
        attn = self.comms.getMatrixLevel(inChannel=self.source.channel, inGroup=self.source.group,
                                         outChannel=self.dest.channel, outGroup=self.dest.group,
                                         unitCode=self.dest.unit.device_id, level=level)
        return

    def linkChannels(self):
        if self.source.unit != self.dest.unit:
            print("Cannot directly link channels across different units. Use another method.")
            return None
        else:
            if self.gatemode == False:
                if self.source.type == "Mic":
                    self.state = "3"  # Gate Off
                else:
                    self.state = "1"
            else:
                if self.source.type == "Mic":
                    self.state = "4"  # Gate On
                else:
                    self.state = "1"
            route = self.comms.setMatrixRouting(inChannel=self.source.channel, inGroup=self.source.group,
                                                outChannel=self.dest.channel, outGroup=self.dest.group,
                                                state=self.state, unitCode=self.dest.unit.device_id)
        self.recalcuateExBusUsage()
        return route

    def unlinkChannels(self):
        self.state = self.comms.setMatrixRouting(inChannel=self.source.channel, inGroup=self.source.group,
                                            outChannel=self.dest.channel, outGroup=self.dest.group,
                                            state="0", unitCode=self.dest.unit.device_id)
        if channel_data[self.source.unit.device_type][self.source.channel]['itype'] == "Expansion":
            self.connection.expansion_bus.getChannelUsage(self.source.channel)
        if channel_data[self.dest.unit.device_type][self.dest.channel]['otype'] == "Expansion":
            self.connection.expansion_bus.getChannelUsage(self.dest.channel)
        self.recalcuateExBusUsage()
        return self.state

    def recalcuateExBusUsage(self):
        if self.source.type == "Expansion":
            self.connection.expansion_bus.getChannelUsage(self.source.channel)
        if self.dest.type == "Expansion":
            self.connection.expansion_bus.getChannelUsage(self.dest.channel)
        return


class ExpansionBusManager(object):
        """XAP Bus Wide Expansion Channel Manager"""

        def __repr__(self):
            return "ExpansionBusAllocator: " + self.statusReport()

        def __init__(self, connection, reserved_channels=[]):
            self.connection = connection
            self.comms = connection.comms
            self.reserved_channels = reserved_channels
            self.units = connection.units
            if self.connection.initialize:
                self.initialize()


        def initialize(self):
            self.busUsed = {"O": None, "P": None, "Q": None, "R": None, "S": None, "T": None, "U": None, "V": None, "W": None, "X": None, "Y": None, "Z": None}
            if len(self.reserved_channels) > 0:
                for channel in self.reserved_channels:
                    self.busUsed.pop(channel, None)
            for channel, status in self.busUsed.items():
                if channel not in self.reserved_channels:
                    if self.getChannelUsage(channel)['inUse']:
                        self.busUsed[channel] = True
                    else:
                        self.busUsed[channel] = False

        def statusReport(self):
            inUse = 0
            available = 0
            reserved = len(self.reserved_channels)
            for channel, status in self.busUsed.items():
                if status == False:
                    available += 1
                elif status == True:
                    inUse += 1
            return "Available: " + str(available) + " InUse: " + str(inUse) + " Reserved: " + str(reserved)

        def refreshData(self):
            for channel, status in self.busUsed.items():
                self.getChannelUsage(channel)

        def getChannelUsage(self, channel, OutputOnly=False):
            inUse = False
            output = 0
            input = 0
            for id, unit in self.units.items():
                for y_channel, data in channel_data[unit.device_type].items():
                    if y_channel == channel:
                        continue
                    if not OutputOnly:
                        if unit.matrix[y_channel][channel].enabled:
                            inUse = True
                            input += 1
                    if unit.matrix[channel][y_channel].enabled:
                        inUse = True
                        output  += 1
            self.busUsed[channel] = inUse
            return {'inUse':inUse, "input": input, "output": output}

        def requestExpChannel(self):
            for channel, status in self.busUsed.items():
                if status == False:
                    return channel
            return False


class GatingGroup(object):

    def __repr__(self):
        return "GatingGroup: " + str(self.group)

    def __init__(self, group, comms, unit):
        self.group = group
        self.comms = comms
        self.unit = unit
        self.label = None
        self.max_mics = None # 1 to 8
        self.first_mic_priority = None # True or False
        self.last_mic = None # True, False

    def initialize(self):
        self.getFirstMicPriority()
        self.getLastMicOn()
        self.getMaxMics()

    def getFirstMicPriority(self):
        fmp = self.comms.getFirstMicPriorityMode(self.group, unitCode=self.unit.device_id)
        return fmp

    def setFirstMicPriority(self, isEnabled):
        if self.group in local_gating_groups:
            fmp = self.comms.setFirstMicPriorityMode(self.group, isEnabled, unitCode=self.unit.device_id)
        else:
            for id, unit in self.unit.connection.units.items():
                fmp = self.comms.setFirstMicPriorityMode(self.group, isEnabled, unitCode=unit.device_id)
                unit.gating_groups[self.group].first_mic_priority = fmp
        return fmp

    def getLastMicOn(self):
        lmo = self.comms.getLastMicOnMode(self.group, unitCode=self.unit.device_id)
        return lmo

    def setLastMicOn(self, mode):
        if self.group in local_gating_groups:
            lmo = self.comms.setLastMicOnMode(self.group, mode, unitCode=self.unit.device_id)
        else:
            for id, unit in self.unit.connection.units.items():
                lmo = self.comms.setLastMicOnMode(self.group, mode, unitCode=unit.device_id)
                unit.gating_groups[self.group].last_mic = lmo
        return lmo

    def getMaxMics(self):
        maxmics = self.comms.getMaxActiveMics(self.group, unitCode=self.unit.device_id)
        return maxmics

    def setMaxMics(self, maxmics):
        if self.group in local_gating_groups:
            maxmics = self.comms.setMaxActiveMics(self.group, maxmics, unitCode=self.unit.device_id)
        else:
            for id, unit in self.unit.connection.units.items():
                maxmics = self.comms.setMaxActiveMics(self.group, maxmics, unitCode=unit.device_id)
                unit.gating_groups[self.group].max_mics = maxmics
        return maxmics


class Filter(object):

    def __repr__(self):
        return "Filter: " + self.type_string + " | Node " + str(self.node)

    def __init__(self, unit, channel, node):
        self.unit = unit
        self.connection = unit.connection
        self.comms = unit.comms
        self.node = node
        self.channel = channel
        self.type = None
        self.type_string = None
        self.frequency = None
        self.gain = None
        self.bandwidth = None
        self.frequency_string = None
        self.gain_string = None
        self.bandwidth_string = None
        self.enabled = None

        self.Q = None
        self.phase = None

    def initialize(self):
        self.getFilter()
        self.getEnabled()

    def getFilter(self):
        filter = self.comms.getFilter(self.channel.channel, self.channel.group, self.node, unitCode=self.unit.device_id)
        return filter

    def setFilter(self):
        print("Not Yet Implemented")
        pass

    def getEnabled(self):
        enabled = self.comms.getFilterEnabled(self.channel.channel, self.channel.group, self.node, unitCode=self.unit.device_id)
        return enabled

    def setEnabled(self, isEnabled):
        enabled = self.comms.setFilterEnabled(self.channel.channel, self.channel.group, self.node, isEnabled, unitCode=self.unit.device_id)
        return enabled


class NoExpansionBusAvailable(Exception):
    pass


class NotSupported(Exception):
    pass
#
    # label for gating groups
    # how to run functions on attribute change
#