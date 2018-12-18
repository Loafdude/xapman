import xapman
xap = xapman.connect()

while 1:
    xap.comms.mqtt_process_cmds()
    xap.comms.listen()