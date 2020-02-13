# tpms_pi_bluetooth
Tire pressure monitor sensor for Raspberry Pi

An example of a while loop to get info from TPMS sensor
When using bluetoothctl the sensor outputs these strings:
[CHG] Device 81:EA:CA:40:08:DF ManufacturerData Key: 0x0100				


How to use:
Fill in codes delivered with sensors as an array in "registereddevices"

Example: 
registereddevices = ['1564DF', '1234DF', '3456GF', '2344DS']
