#/****************************************************************************/
#/* RPiPIC                                                                   */
#/* ------------------------------------------------------------------------ */
#/* V1.01 - 2017-05-13 - Jason Birch                                         */
#/* V1.02 - 2017-12-30 - Support for PIC18F device programming.              */
#/* ------------------------------------------------------------------------ */
#/* Python PIC Microcontroller Programmer.                                   */
#/*                                                                          */
#/* Currently supported devices:                                             */
#/*                                                                          */
#/* 12F629          12F675          12F683                                   */
#/*                                                                          */
#/* 16F88           16F627          16F628A         16F630          16F684   */
#/* 16F690          16F876A         16F877A         16F886          16F887   */
#/* 16F18313        16F18323        16F18324        16F18344        16F18325 */
#/* 16F18345        16F18326        16F18346                                 */
#/*                                                                          */
#/* 18F2420         18F2455         18F2520         18F2550         18F4420  */
#/* 18F4455         18F4520         18F4550                                  */
#/*                                                                          */
#/* Additional devices can be added in the PIC_DEVICES.py file.              */
#/****************************************************************************/



Linux Packages For PIC Microchip Development
============================================
apt-get install gpsim
apt-get install gputils
apt-get install sdcc



Tools From Linux Packages For PIC Microchip Development
=======================================================
Cross compile a PIC Microchip assembly text file.
gpasm -w 1 -c [FILE_NAME].asm

Link a PIC Microchip object file and produce a Intel HEX formatted object file.
gplink -o [FILE_NAME].hex [FILE_NAME].o

Simulate a compiled PIC Microchip code file for debugging.
gpsim -s [FILE_NAME].cod

PIC Microchip disassembler.
gpdasm

Discard symbols from a PIC Microchip object file.
gpstrip

PIC Microchip object file viewer.
gpvo

PIC Microchip cod file viewer.
gpvc

PIC Microchip object library manager.
gplib



PIC Microchip Hardware Requirements
===================================
VPP 12.75V 100 mA
Varies from device to device, see device specifications.

VDD >=2.0V <=6.5V += 0.25V 40 mA
Officially Microchip specifies to verify the device is programmed by verifying
at each voltage between 2V and 6.5V in steps of 0.25V. When not verified in
this way the device is considered programmed for development purposes.

While programming a device it maybe required to pull a pin named PGM low using
a high value resistor, to prevent it floating and interfering with the
programming process.


Raspberry Pi GPIO Requirements
-----------------------------
OUTPUT      VDD Switch
OUTPUT      PRG Switch
OUTPUT      Data Out
INPUT       Data In
OUTPUT      Clock



RPiPIC PIC Microchip Programmer Commands
========================================
./RPiPIC.py -P
Power on current device.

./RPiPIC.py -O
Power off current device.

./RPiPIC.py -L
List currently supported PIC devices.

./RPiPIC.py -C [PIC_DEVICE]
Display device memory checksum.

./RPiPIC.py -D [PIC_DEVICE] <MEMORY_AREA>
Read memory from device and display.

./RPiPIC.py -B [PIC_DEVICE]
Blank check device.

./RPiPIC.py -E [PIC_DEVICE] <NO_STORE>
Erase all device memory.
If 'NO_STORE' is specified non data and program memory is not retained.

./RPiPIC.py -EC [PIC_DEVICE]
Erase all device config.

./RPiPIC.py -R [PIC_DEVICE] [FILE_NAME]
Read memory from device and save to .hex file.

./RPiPIC.py -W [PIC_DEVICE] [FILE_NAME]
Read .hex file and write to device memory.

./RPiPIC.py -V [PIC_DEVICE] [FILE_NAME]
Read memory from device and read .hex file, then verify data.

./RPiPIC.py -LM [PIC_DEVICE]
List device memory areas.

./RPiPIC.py -LD [PIC_DEVICE] [MEMORY_AREA] [DATA]
Load data into a device memory area.
EXAMPLES:
./RPiPIC.py -LD 16F684 CONFIG:BOR_CAL 23F8
./RPiPIC.py -LD 16F684 CONFIG:CAL 3FFF
./RPiPIC.py -LD 16F684 CONFIG:ID 0005000100020001



Project Files
-------------
A full write up for this project can be found at the web site:
http://www.newsdownload.co.uk/

├── GNU-GeneralPublicLicense.txt
├── README.txt           - This file.
├── RPiPIC.py            - PIC Microchip programmer application.
├── PIC_DEVICES.py       - Definitions of supported PIC Microchip devices.
├── HEX_File.py          - Intel HEX file format handler.
├── PIC_API.py           - API level PIC Microchip device control.
├── PIC.py               - Low level PIC Microchip device control.
└── TEST_ASM             - Example projects for supported PIC Microchip devices.
    ├── INCLUDE          - PIC Microchip device asm include files.
    │   ├── P12F629.INC
    │   ├── P12F675.INC
    │   ├── P12F683.INC
    │   ├── P16F88.INC
    │   ├── P16F627.INC
    │   ├── P16F628A.INC
    │   ├── P16F630.INC
    │   ├── P16F684.INC
    │   ├── P16F690.INC
    │   ├── P16F876A.INC
    │   ├── P16F877a.INC
    │   ├── P16F886.INC
    │   ├── P16F887.INC
    │   ├── P16F18346.INC
    │   ├── P18F2420.INC
    │   ├── P18F2455.INC
    │   ├── P18F2520.INC
    │   ├── P18F4520.INC
    │   └── P18F4550.INC
    ├── PIC12F629        - Example application for a PIC Microchip PIC12F629
    │   ├── Build.sh
    │   ├── PIC12F629.asm
    ├── PIC12F675        - Example application for a PIC Microchip PIC12F675
    │   ├── Build.sh
    │   ├── PIC12F675.asm
    ├── PIC12F683        - Example application for a PIC Microchip PIC12F683
    │   ├── Build.sh
    │   ├── PIC12F683.asm
    ├── PIC16F88         - Example application for a PIC Microchip PIC16F88
    │   ├── Build.sh
    │   ├── PIC16F88.asm
    ├── PIC16F627        - Example application for a PIC Microchip PIC16F627
    │   ├── Build.sh
    │   ├── PIC16F627.asm
    ├── PIC16F628A       - Example application for a PIC Microchip PIC16F628A
    │   ├── Build.sh
    │   ├── PIC16F628A.asm
    ├── PIC16F630        - Example application for a PIC Microchip PIC16F630
    │   ├── Build.sh
    │   ├── PIC16F630.asm
    ├── PIC16F684        - Example application for a PIC Microchip PIC16F684
    │   ├── Build.sh
    │   ├── PIC16F684.asm
    ├── PIC16F690        - Example application for a PIC Microchip PIC16F690
    │   ├── Build.sh
    │   ├── PIC16F690.asm
    ├── PIC16F876A       - Example application for a PIC Microchip PIC16F876A
    │   ├── Build.sh
    │   ├── PIC16F876A.asm
    ├── PIC16F886        - Example application for a PIC Microchip PIC16F886
    │   ├── Build.sh
    │   ├── PIC16F886.asm
    ├── PIC16F876A       - Example application for a PIC Microchip PIC16F876A
    │   ├── Build.sh
    │   ├── PIC16F876A.asm
    ├── PIC16F877A       - Example application for a PIC Microchip PIC16F877A
    │   ├── Build.sh
    │   ├── PIC16F877A.asm
    ├── PIC18F2520       - Example application for a PIC Microchip PIC18F2520
    │   ├── Build.sh
    │   ├── PIC18F2520.asm
    ├── PIC18F4550       - Example application for a PIC Microchip PIC18F4550
    │   ├── Build.sh
    │   ├── PIC18F4550.asm
    └── PIC16F18346      - Example application for a PIC Microchip PIC16F18346
        ├── Build.sh
        └── PIC16F18346.asm



Configuration
-------------
The only configuration required is to edit the GPIO pin allocation in the
PIC.py project file to the GPIO allocation used.



Adding Devices
--------------
The file PIC_DEVICES.py contains definitions of the memory map for each
supported PIC device. PIC devices can be added by creating an additional memory
map for the device. There are a few reasons why a particular PIC device may not
work with the current release of this software.

1. There are several programming process specifications, the specifications
   for most of the PIC12F, PIC16F and PIC18F, are currently implemented.
   However some devices may have processes not currently supported.

2. The process of adding a device is to define the memory map of the device in
   the application. It is possible that the current data definitions in the
   application may not be sufficient to properly define a memory map for a
   specific device.

An example memory map would be:

PIC_DEVICE.append([
"16F630",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,
                                                0x0000, 0x0080, 0x4200, 0x0000],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,
                                                0x0000, 0x03FF, 0x0000, 0x0000],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ST|PICMEM_RE|PICMEM_OSC_CAL,
                                                0x03FF, 0x0001, 0x03FF, 0x3FFF],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,
                                                0x0000, 0x0004, 0x4000, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,
                                                0x2000, 0x0004, 0x4000, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,
                                                0x2006, 0x0001, 0x4006, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CONFIG,
                                                0x0007, 0x0001, 0x400E, 0x3000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CONFIG,
                                                0x2007, 0x0001, 0x400E, 0x3000],
   ]
])

The device name is specified first, then within that definition is the
definition for the devices memory map. Each line of the definition defines an
area of the memory.

First if the memory is read only PICMEM_RO, write only PICMEM_RO or read/write
PICMEM_RW.

Next the physical type of memory, currently only PICMEM_EEPROM supported.

Next the memory region type, PICMEM_DATA data memory read and writable
by a program. PICMEM_PROG program memory. PICMEM_CONF device configuration
memory.

Next the memory region segment name, e.g. PICMEM_OSC_CAL oscillator calibration
word. If PICMEM_ST is specified, this application will read the value of the
memory before erasing, and where PICMEM_RE is specified the value will be
restored here after erasing.

The final four words of data for a memory region are:

Device memory address. The address of the memory on the physical device.

Device memory size. The number of words in of memory available in this region.

Assembly memory address. For data and program memory the device address
typically starts at 0x0000 for both. So in the assembly program a directive
ORG 0x4000 can be used for example to define data memory content. The
programming specification of the device can define this value, so if it is
defined in the specification, that value must be used.

The last value is the configuration mask, used to prevent verification errors
where configuration bits are unsettable, and always read as a 0 or 1.
This has not been implemented currently.



RELEASE TEST PROCEDURE
======================
Perform the following procedure on each supported device to verify operation
before checking in to source control.

./RPiPIC.py -E 16F877A
./RPiPIC.py -B 16F877A
./RPiPIC.py -W 16F877A TEST_ASM/PIC16F877A/PIC16F877A.hex
./RPiPIC.py -B 16F877A
./RPiPIC.py -V 16F877A TEST_ASM/PIC16F877A/PIC16F877A.hex
./RPiPIC.py -D 16F877A
./RPiPIC.py -P
./RPiPIC.py -O

