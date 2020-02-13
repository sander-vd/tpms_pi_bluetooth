"""An example of a while loop to get info from TPMS sensor
When using bluetoothctl the sensor outputs these strings:
[CHG] Device 81:EA:CA:40:08:DF ManufacturerData Key: 0x0100				

With help from Tatsuya-8888 / https://qiita.com/Tatsuya-8888/items/756dce5270966d4bf460 (Japanese)

How to use:

Fill in codes delivered with sensors as an array in "registereddevices" 
Example: 
registereddevices = ['1564DF', '1234DF', '3456GF', '2344DS']

"""


from bluepy.btle import Scanner
import re


def hex2int(_HEX):
  _BIN=bytes.fromhex(_HEX)
  _Rev=_BIN[::-1]
  _HEX=_Rev.hex()
  return int(_HEX,16)

# Fill list with used sensors
registereddevices = ['4008DF']

knownddevices = []

while True:
	scan = Scanner(0)
	devs = scan.scan(10.0)


	for device in devs:
		if device.addr in knownddevices:

			for (Code,desc,value) in device.getScanData():
				# Check if string is indeed 36 characters long
				count = len(value)
				if count == 36:

					# Check if mac adress is in string
					mac = (device.addr.replace(':', ''))
					m = re.search('/*{0}'.format(mac), value)

					if m:

						press = value[16:22]
						temp = value[24:28]
						bat = value[32:36]

						try:
							# Convert values to readable format.
							press = hex2int(press) / 100000
							temp = hex2int(temp) / 100
							bat = hex2int(bat)
							print("Pressure ", press, " Bar")
							print("Temperature ", temp, " C")
							print("Battery Level ", bat, " %")
						except:
							pass

		else:
			for (Code,desc,value) in device.getScanData():
				# Check if devices is actually the TPMS
				m = re.search('TPMS2_\w\w\w\w\w\w', value)
				# Check if the sensor is in our list above
				if m:
					devicename = m.group(0)[6:]
					if devicename in registereddevices:
						knownddevices.append(device.addr)
						print("Found device ", device.addr, " Name is ", devicename)
