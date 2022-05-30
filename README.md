# xapman
Clearone Gentner XAP800 & XAP400 to MQTT Bridge

Nearly every function is accessible and able to be queried.


You can run it like this at a linux command prompt

```
export MQTT_HOST='10.9.9.100'
export MQTT_PORT='1883'
export MQTT_ROOT='Home/Audio/'
export SERIAL_PORT='/dev/ttyS0'
export BAUD_RATE=38400
export RAMP_RATE=6
/usr/bin/python3 /usr/xapman/go.py
```

Here are some examples of changing values in the matrix

Ramp Gain Value:
```
topic: "Home/Audio/GreatMatrix/Outputs/LvRm Front Right/rampToDb"
payload: "[-8]"
```
Which runs the command "rampToDb" on matrix named "GreatMatrix" on channel named "LvRm Front Right" to a value of -8

Mute Channel:
```
topic: "Home/Audio/GreatMatrix/Outputs/LvRm Front Right/setMute"
payload: "[1]"
```

Matrix link / unlink:
```
topic: "Home/Audio/GreatMatrix/Matrix/Src:House Left(Y)/Dest:LvRm Proc Left(A)/linkChannels"
payload: "[]"

topic: "Home/Audio/GreatMatrix/Matrix/Src:House Left(Y)/Dest:LvRm Proc Left(A)/unlinkChannels"
payload: "[]"
```

Change Volume (Attenuation actually) on Matrix Link to -2
```
topic: "Home/Audio/GreatMatrix/Matrix/Src:House Left(Y)/Dest:LvRm Pro Sub(C)/setAttenuation"
payload: "[-2]"
```
