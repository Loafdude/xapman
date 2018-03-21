import XAPX00

class XapConnection(object):
    """Xap Serial Connection Wrapper
    """
    
    def __init__(self, serial_path="/dev/ttyUSB0",
                 baudrate=38400,
                 mqtt_path="home/HA/AudioMixers/",
                 device_type="XAP800"):
        self.mqtt_path  = mqtt_path
        self.baudrate   = baudrate
        self.units = []
        self.connection = XAPX00.XAPX00(comPort=serial_path, baudRate=38400, XAPType=device_type)
        self.connection.connect()

        print("Searching for devices...")
        delay = self.connection._maxrespdelay
        self.connection._maxrespdelay = 0.1
        for u in range(8):
            uid = self.connection.getUniqueId(u)
            if uid != None:
                unit = {'id': str(u), 'UID':uid, 'version':xap.getVersion(u)}
                print("Found unit " + unit['id'] + " - " + unit['UID'] + "  Ver. " + unit['version'] )
                self.units.append(unit)




        

class XapUnit(object):
    """Xap Unit Wrapper
       The following are not implemented;
       Presets, Macros, Serial Strings, Preset/Macro Locking, Master Mode, gateing report
    """
    
    def __init__(self, xap_connection,
                 mqtt_path="home/HA/AudioMixers/",
                 alt_mqtt_paths=[],
                 XAP_unit=0):
        self.connection = xap_connection
        self.device_id = XAP_unit
        self.mqtt_path      = mqtt_path
        self.alt_mqtt_paths = alt_mqtt_paths
        self.serial_number = None #
        self.FW_version = None #
        self.DSP_version = None #
        self.modem_mode  = None #
        self.modem_pass  = None #
        self.modem_init_string = None #
        self.program_strings = None
        self.safety_mute = None #
        self.panel_timeout = None #
        self.panel_lockout = None #
    
    def getID(self):
        '''Fetch ID from XAP Unit'''
        id = self.connection.getDeviceID(unitCode=self.device_id)
        return id
        
    def getFW(self):
        '''Fetch FW Version from XAP Unit'''
        FW = self.connection.getVersion(unitCode=self.device_id)
        self.FW_version = FW
        return FW
        
    def getDSP(self):
        '''Fetch DSP Version from XAP Unit'''
        DSP = self.connection.getDSPVersion(unitCode=self.device_id)
        self.DSP_version = DSP
        return DSP
        
    def getSerialNumber(self):
        '''Fetch Unique ID from XAP Unit'''
        serial = self.connection.getUniqueId(unitCode=self.device_id)
        self.serial_number = serial
        return serial
        
    def getModemMode(self):
        '''Fetch Modem Mode from XAP Unit'''
        mode = self.connection.getModemMode(unitCode=self.device_id)
        self.modem_mode = mode
        return mode
        
    def setModemMode(self, isEnabled):
        '''Set Modem Mode to XAP Unit'''
        mode = self.connection.setModemMode(isEnabled, unitCode=self.device_id)
        self.modem_mode = mode
        return mode
        
    def getModemInit(self):
        '''Fetch Modem Init String from XAP Unit'''
        string = self.connection.getModemInitString(unitCode=self.device_id)
        self.modem_init_string = string
        return string
        
    def setModemInit(self, string):
        '''Set Modem Init String to XAP Unit'''
        string = self.connection.setModemInitString(string, unitCode=self.device_id)
        self.modem_init_string = string
        return string
        
    def getModemPass(self):
        '''Fetch Modem Init String from XAP Unit'''
        string = self.connection.getModemModePassword(unitCode=self.device_id)
        self.modem_pass = string
        return string
        
    def setModemPass(self, string):
        '''Set Modem Init String to XAP Unit'''
        string = self.connection.setModemModePassword(string, unitCode=self.device_id)
        self.modem_pass = string
        return string
        
    def getSafetyMute(self):
        '''Fetch safety mute status from XAP Unit'''
        status = self.connection.getSafetyMute(unitCode=self.device_id)
        self.safety_mute = status
        return status
        
    def setSafetyMute(self, isEnabled):
        '''Set safety mute status to XAP Unit'''
        status = self.connection.setSafetyMute(isEnabled, unitCode=self.device_id)
        self.safety_mute = status
        return status
        
    def getPanelTimeout(self):
        '''Fetch panel timout in min from XAP Unit'''
        minutes = self.connection.getScreenTimeout(unitCode=self.device_id)
        self.panel_timeout = minutes
        return minutes
        
    def setPanelTimeout(self, minutes):
        '''Set panel timout in min to XAP Unit'''
        minutes = self.connection.setScreenTimeout(minutes, unitCode=self.device_id)
        self.panel_timeout = minutes
        return minutes
        
    def getPanelLock(self):
        '''Fetch panel lock from XAP Unit'''
        status = self.connection.getFrontPanelLock(unitCode=self.device_id)
        self.panel_lockout = status
        return status
        
    def setPanelLock(self, isEnabled):
        '''Set panel lock to XAP Unit'''
        status = self.connection.setFrontPanelLock(isEnabled, unitCode=self.device_id)
        self.panel_lockout = status
        return status

class OutputChannel(object):
    """XAP Output Channel Wrapper"""
    
    def __init__(self, unit,
                 mqtt_path="home/HA/AudioMixer/Outputs/",
                 alt_mqtt_paths=[],
                 XAP_unit=0,
                 XAP_channel=1):
        self.title          = None
        self.unit           = unit
        self.mqtt_path      = mqtt_path
        self.alt_mqtt_paths = alt_mqtt_paths
        self.XAP_channel    = XAP_channel
        self.gain           = None
        self.gain_min       = None
        self.gain_max       = None
        self.mute           = None
        self.label          = None
        self.sources        = None
        self.filters        = None
        self.constant_gain  = None # Also known as Number of Mics (NOM)
        
    def getLabel(self):
        '''Fetch Label from XAP Unit'''
        label = self.unit.connection.getLabel(self.XAP_channel, "O", unitCode=self.unit.device_id)
        self.label = label
        return label
    
    def setLabel(self, label):
        '''Fetch Label from XAP Unit'''
        label = self.unit.connection.setLabel(self.XAP_channel, "O", label, unitCode=self.unit.device_id)
        self.label = label
        return label
        
# class InputChannel(object):
#     """XAP Input Channel Wrapper"""
#
#     def __init__(self, xap_connection, title
#                  mqtt_path="home/HA/AudioMixer/Inputs",
#                  alt_mqtt_paths=[],
#                  XAP_Unit=0,
#                  XAP_Channel=1,
#                  AutoApplyLabel=True):
#
#         self.title          = title
#         self.mqtt_path      = mqtt_path
#         self.alt_mqtt_paths = alt_mqtt_paths
#         self.gain           = None
#         self.gain_min       = None
#         self.gain_max       = None
#         self.mute           = None
#         self.label          = None
#         self.type               = None # LineLevel or Microphone
#         self.AGC                = None # True or False - Automatic Gain Control
#         self.AGC_target         = None # -30 to 20dB
#         self.AGC_threshold      = None # -50 to 0dB
#         self.AGC_attack         = None # 0.1 to 10.0s in .1 increments
#         self.AGC_gain           = None # 0.0 to 18.0dB
#
#         # Microphone Input Only
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
# class ExpansionChannel(object):
#     self.input_label          = None
#     self.output_label          = None
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