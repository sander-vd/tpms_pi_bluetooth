# tpms_pi_bluetooth
Tire pressure monitor sensor for Raspberry Pi
With help from Tatsuya-8888 / https://qiita.com/Tatsuya-8888/items/756dce5270966d4bf460 (Japanese)

An example of a while loop to get info from TPMS sensor
When using bluetoothctl the sensor outputs these strings:

[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0x0100	

[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0x84 

[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0x2A

[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0xCA

[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0x40

[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0x08

[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0xDF 



[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0x46 

[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0x23 

[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0x04 

[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0x00



[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0xb2

[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0x08



[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0x00 

[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0x00 



[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0x38

[CHG] Device 84:2A:CA:40:08:DF ManufacturerData Key: 0x00



The above is the full output of one sensor:

Line 1              identifier

Line 2  - 7         mac adress of sensor

Line 8  - 11        tire pressure

Line 12 - 13        tire temperature

Line 14 - 15        no idea

Line 16 - 17        battery percentage



How to use:
Fill in codes delivered with sensors as an array in "registereddevices"

Example: 
registereddevices = ['1564DF', '1234DF', '3456GF', '2344DS']

from command line: sudo python3 tpsm.py 

There are many of the tpms sensors on the market, please see the JPG for the model that I used. 
I believe that it is usually refered to as Bluetooth 4.0 TPMS.
Other sensors could work as well depending on the output given. 

