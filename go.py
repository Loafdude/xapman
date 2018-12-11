import xapman

xap = xapman.connect()

while 1:
    xap.comms.listen()