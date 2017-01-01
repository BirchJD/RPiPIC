#/****************************************************************************/
#/* RPiPIC                                                                   */
#/* ------------------------------------------------------------------------ */
#/* V1.00 - 2016-12-22 - Jason Birch                                         */
#/* ------------------------------------------------------------------------ */
#/* Python PIC Microcontroller Programmer.                                   */
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
VPP 12.0V 100 mA
VDD = 2.0V < 6.5V += 0.25V 40 mA


Raspberry Pi GPIO Requiements
-----------------------------
VDD Switch
PRG Switch
Data Out
Data In
Clock



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

./RPiPIC.py -D [PIC_DEVICE]
Read memory from device and display.

./RPiPIC.py -B [PIC_DEVICE]
Blank check device.

./RPiPIC.py -E [PIC_DEVICE]
Erase all device memory.

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



Project Files
-------------
A full write up for this project can be found at the web site:
http://www.newsdownload.co.uk/


├── GNU-GeneralPublicLicense.txt
├── RPiPIC.py            - PIC Microchip programmer application.
├── PIC_API.py           - API level PIC Microchip device control.
├── PIC.py               - Low level PIC Microchip device control.
├── HEX_File.py          - Intel HEX file format handler.
├── PIC_DEVICES.py       - Definitions of supported PIC Microchip devices.
├── README.txt           - This file.
└── TEST_ASM             - Example projects for supported PIC Microchip devices.
    ├── INCLUDE           - PIC Microchip device asm include files.
    │   ├── P12F675.INC
    │   └── P12F683.INC
    ├── PIC12F675         - Example application for a PIC Microchip PIC12F675
    │   ├── Build.sh
    │   ├── PIC12F675.asm
    └── PIC12F683         - Example application for a PIC Microchip PIC12F683
        ├── Build.sh
        ├── PIC12F683.asm


Configuration
-------------
The only configuration required is to edit the GPIO pin allocation in the
PIC.py project file to the GPIO allocation used.

