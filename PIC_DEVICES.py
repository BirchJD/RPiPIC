#!/usr/bin/python2

# PIC_DEVICES - Python PIC Microcontroller Device Definitions
# Copyright (C) 2016 Jason Birch
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#/****************************************************************************/
#/* PIC_DEVICES                                                              */
#/* ------------------------------------------------------------------------ */
#/* V1.00 - 2016-12-22 - Jason Birch                                         */
#/* V1.01 - 2017-12-30 - Added support for 18F device programming.           */
#/* V1.02 - 2019-05-10 - Calibrate clock pulse, device specific clock period.*/
#/*                      Device ID lookup and verify.                        */
#/*                      Read specified data range. Only read and verify upto*/
#/*                      highest programmed or specified address.            */
#/*                      Added devices: 12F508,12F1822,16F505,16F688,16F716  */
#/* ------------------------------------------------------------------------ */
#/* Python PIC Microcontroller Device Definitions.                           */
#/****************************************************************************/


#/*********************/
#/* PIC Memory Types. */
#/*********************/
PICMEM_NONAME   = 0x0000000000

PICMEM_RO       = 0x0000000001
PICMEM_WO       = 0x0000000002
PICMEM_RW       = 0x0000000004
PICMEM_ST       = 0x0000000008
PICMEM_RE       = 0x0000000010

PICMEM_EEPROM   = 0x0000000020
PICMEM_FLASH    = 0x0000000040

PICMEM_CONF     = 0x0000010000
PICMEM_DATA     = 0x0000020000
PICMEM_PROG     = 0x0000040000

PICMEM_ID       = 0x0000080000
PICMEM_DEV_ID   = 0x0000100000
PICMEM_CONFIG   = 0x0000200000
PICMEM_CAL      = 0x0000400000
PICMEM_BOR_CAL  = 0x0000800000
PICMEM_OSC_CAL  = 0x0001000000
PICMEM_CALIB    = 0x0002000000
PICMEM_ICD_HALT = 0x0004000000

DEVICE_MEM_NAME_MASK = 0xFFFFFF0000

PICMEM_TYPE_LOOKUP = [
   PICMEM_NONAME,          # Un-named.

   PICMEM_RO,              # Read only memory.
   PICMEM_WO,              # Write only memory.
   PICMEM_RW,              # Read/Write memory.
   PICMEM_ST,              # Store data before erase.
   PICMEM_RE,              # Restore data after erase.

   PICMEM_EEPROM,          # EEPROM memory type.
   PICMEM_FLASH,           # Flash memory type.

   PICMEM_CONF,            # Configuration memory area.
   PICMEM_DATA,            # Data memory area.
   PICMEM_PROG,            # Program memory area.

   PICMEM_ID,              # User ID memory area.
   PICMEM_DEV_ID,          # Device ID memory area.
   PICMEM_CONFIG,          # Device config memory area extended.
   PICMEM_CAL,             # Device calibration memory area.
   PICMEM_BOR_CAL,         # Device brownout calibration memory area.
   PICMEM_OSC_CAL,         # Device oscilator calibration memory area.
   PICMEM_CALIB,           # Device brown out and power on calibration.
   PICMEM_ICD_HALT,        # In circuit debugging, halt entry instruction.
]

PICMEM_TYPE = [
   "",

   "READ",
   "WRITE",
   "READ/WRITE",
   "STORE",
   "RESTORE",

   "EEPROM",
   "FLASH",

   "CONFIG",
   "DATA",
   "PROGRAM",

   "ID",
   "DEV_ID",
   "CONFIG",
   "CAL",
   "BOR_CAL",
   "OSC_CAL",
   "CALIB",
   "ICD_HALT",
]



#/***************************************************************************/
#/* Define a PIC Microcontroller type:                                      */
#/* [                                                                       */
#/*    PIC Device Name,                                                     */
#/*    [                                                                    */
#/*       Memory Type|PIC Memory Area, Start Address, Length, Obj Address,  */
#/*       Store-Restore/Verify Mask, Word Size                              */
#/*       ...                                                               */
#/*    ],                                                                   */
#/*    ...                                                                  */
#/* ]                                                                       */
#/***************************************************************************/
PICDEV_NAME = 0
PICDEV_MEM = 1

PICDEV_MEM_TYPE = 0
PICDEV_MEM_ADDR = 1
PICDEV_MEM_SIZE = 2
PICDEV_MEM_OBJ_ADDR = 3
PICDEV_MEM_STRE_MASK = 4
PICDEV_MEM_DATA = 5


PIC_DEVICE = []


PIC_DEVICE.append([
"16F_1W_DEV_ID",
   [
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x002006, 0x000001, 0x004006, [0x0000]],
   ]
])


PIC_DEVICE.append([
"16F_2W_DEV_ID",
   [
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x008005, 0x000002, 0x02000A, [0x0000]],
   ]
])


PIC_DEVICE.append([
"18F_DEV_ID",
   [
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x3FFFFE, 0x00002, 0x3FFFFE, [0x0000]],
   ]
])


PIC_DEVICE.append([
"12F508",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0001, 0x0200, 0x0000, [0x0FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x0201, 0x0004, 0x4000, [0x0FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ST|PICMEM_RE|PICMEM_OSC_CAL, 0x0205, 0x0001, 0x400A, [0x0FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_CONFIG,            0x0000, 0x0001, 0x1FFE, [0x001F]],
   ]
])


PIC_DEVICE.append([
"12F629",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0080, 0x4200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x03FF, 0x0000, [0x3FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ST|PICMEM_RE|PICMEM_OSC_CAL, 0x03FF, 0x0001, 0x03FF, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, [0x0000]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x0007, 0x0001, 0x400E, [0x31FF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x2007, 0x0001, 0x400E, [0x31FF]],
   ]
])


PIC_DEVICE.append([
"12F675",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0080, 0x4200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x03FF, 0x0000, [0x3FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ST|PICMEM_RE|PICMEM_OSC_CAL, 0x03FF, 0x0001, 0x03FF, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, [0x0000]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x0007, 0x0001, 0x400E, [0x31FF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x2007, 0x0001, 0x400E, [0x31FF]],
   ]
])


PIC_DEVICE.append([
"12F683",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x0800, 0x0000, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, [0x0000]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_BOR_CAL, 0x0008, 0x0001, 0x400F, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_BOR_CAL, 0x2008, 0x0001, 0x400F, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CAL,     0x0009, 0x0001, 0x4010, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CAL,     0x2009, 0x0001, 0x4010, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x0007, 0x0001, 0x400E, [0x0FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x2007, 0x0001, 0x400E, [0x0FFF]],
   ]
])


PIC_DEVICE.append([
"12F1822",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x0800, 0x0000, [0x3FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x8000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x8006, 0x0001, 0x400C, [0x0000]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x8007, 0x0002, 0x400E, [0x3FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_RE|PICMEM_CAL, 0x8009, 0x0002, 0x4012, [0x3FFF]],
   ]
])


PIC_DEVICE.append([
"16F88",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x1000, 0x0000, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, [0x0000]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x0007, 0x0002, 0x400E, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x2007, 0x0002, 0x400E, [0x3FFF]],
   ]
])


PIC_DEVICE.append([
"16F505",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0001, 0x0400, 0x0000, [0x0FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x0401, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ST|PICMEM_RE|PICMEM_OSC_CAL, 0x0405, 0x0001, 0x400A, [0x0FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_CONFIG,            0x0000, 0x0001, 0x1FFE, [0x001F]],
   ]
])


PIC_DEVICE.append([
"16F627",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0080, 0x4200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x0400, 0x0000, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, [0x0000]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x0007, 0x0001, 0x400E, [0x21FF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x2007, 0x0001, 0x400E, [0x21FF]],
   ]
])


PIC_DEVICE.append([
"16F628A",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0080, 0x4200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x0800, 0x0000, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, [0x0000]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x0007, 0x0001, 0x400E, [0x21FF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x2007, 0x0001, 0x400E, [0x21FF]],
   ]
])


PIC_DEVICE.append([
"16F630",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0080, 0x4200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x03FF, 0x0000, [0x3FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ST|PICMEM_RE|PICMEM_OSC_CAL, 0x03FF, 0x0001, 0x03FF, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, [0x0000]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x0007, 0x0001, 0x400E, [0x31FF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x2007, 0x0001, 0x400E, [0x31FF]],
   ]
])


PIC_DEVICE.append([
"16F684",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x0800, 0x0000, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, [0x0000]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x0007, 0x0001, 0x400E, [0x0FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x2007, 0x0001, 0x400E, [0x0FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_BOR_CAL, 0x0008, 0x0001, 0x4008, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_BOR_CAL, 0x2008, 0x0001, 0x4008, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CAL,     0x0009, 0x0001, 0x4009, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CAL,     0x2009, 0x0001, 0x4009, [0x3FFF]],
   ]
])


PIC_DEVICE.append([
"16F688",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x0800, 0x0000, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, [0x0000]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x0007, 0x0001, 0x400E, [0x0FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x2007, 0x0001, 0x400E, [0x0FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CAL,     0x0008, 0x0001, 0x4008, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CAL,     0x2008, 0x0001, 0x4008, [0x3FFF]],
   ]
])


PIC_DEVICE.append([
"16F690",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x1000, 0x0000, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, [0x0000]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x0007, 0x0001, 0x400E, [0x0FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x2007, 0x0001, 0x400E, [0x0FFF]],
   ]
])


PIC_DEVICE.append([
"16F716",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x0800, 0x0000, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, [0x0000]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x0007, 0x0001, 0x400E, [0x02FC]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x2007, 0x0001, 0x400E, [0x02FC]],
   ]
])


PIC_DEVICE.append([
"16F876A",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x2000, 0x0000, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, [0x0000]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x0007, 0x0001, 0x400E, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x2007, 0x0001, 0x400E, [0x3FFF]],
   ]
])


PIC_DEVICE.append([
"16F877A",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x2000, 0x0000, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, [0x0000]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x0007, 0x0001, 0x400E, [0x2FCF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x2007, 0x0001, 0x400E, [0x2FCF]],
   ]
])


PIC_DEVICE.append([
"16F886",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x2000, 0x0000, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, [0x0000]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x0007, 0x0002, 0x400E, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x2007, 0x0002, 0x400E, [0x3FFF]],
   ]
])


PIC_DEVICE.append([
"16F887",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x2000, 0x0000, [0x3FFF]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, [0x0000]],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x0007, 0x0002, 0x400E, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x2007, 0x0002, 0x400E, [0x3FFF]],
   ]
])


PIC_DEVICE.append([
"16F18313",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x00F000, 0x000100, 0x020200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x000000, 0x000800, 0x000000, [0x3FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x008000, 0x000004, 0x020002, [0x3FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ICD_HALT,          0x008004, 0x000001, 0x020004, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_PROG|PICMEM_DEV_ID,            0x008005, 0x000002, 0x02000A, [0x0000]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_CONFIG,            0x008007, 0x000004, 0x02000E, [0x3FFF]],
   ]
])


PIC_DEVICE.append([
"16F18323",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x00F000, 0x000100, 0x020200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x000000, 0x000800, 0x000000, [0x3FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x008000, 0x000004, 0x020002, [0x3FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ICD_HALT,          0x008004, 0x000001, 0x020004, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_PROG|PICMEM_DEV_ID,            0x008005, 0x000002, 0x02000A, [0x0000]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_CONFIG,            0x008007, 0x000004, 0x02000E, [0x3FFF]],
   ]
])


PIC_DEVICE.append([
"16F18324",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x00F000, 0x000100, 0x020200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x000000, 0x001000, 0x000000, [0x3FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x008000, 0x000004, 0x020002, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_PROG|PICMEM_DEV_ID,            0x008005, 0x000002, 0x02000A, [0x0000]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_CONFIG,            0x008007, 0x000004, 0x02000E, [0x3FFF]],
   ]
])


PIC_DEVICE.append([
"16F18325",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x00F000, 0x000100, 0x020200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x000000, 0x002000, 0x000000, [0x3FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x008000, 0x000004, 0x020002, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_PROG|PICMEM_DEV_ID,            0x008005, 0x000002, 0x02000A, [0x0000]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_CONFIG,            0x008007, 0x000004, 0x02000E, [0x3FFF]],
   ]
])


PIC_DEVICE.append([
"16F18326",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x00F000, 0x000100, 0x020200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x000000, 0x004000, 0x000000, [0x3FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x008000, 0x000004, 0x020002, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_PROG|PICMEM_DEV_ID,            0x008005, 0x000002, 0x02000A, [0x0000]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_CONFIG,            0x008007, 0x000004, 0x02000E, [0x3FFF]],
   ]
])


PIC_DEVICE.append([
"16F18344",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x00F000, 0x000100, 0x020200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x000000, 0x001000, 0x000000, [0x3FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x008000, 0x000004, 0x020002, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_PROG|PICMEM_DEV_ID,            0x008005, 0x000002, 0x02000A, [0x0000]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_CONFIG,            0x008007, 0x000004, 0x02000E, [0x3FFF]],
   ]
])


PIC_DEVICE.append([
"16F18345",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x00F000, 0x000100, 0x020200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x000000, 0x002000, 0x000000, [0x3FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x008000, 0x000004, 0x020002, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_PROG|PICMEM_DEV_ID,            0x008005, 0x000002, 0x02000A, [0x0000]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_CONFIG,            0x008007, 0x000004, 0x02000E, [0x3FFF]],
   ]
])


PIC_DEVICE.append([
"16F18346",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x00F000, 0x000100, 0x020200, [0x00FF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x000000, 0x004000, 0x000000, [0x3FFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x008000, 0x000004, 0x020002, [0x3FFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_PROG|PICMEM_DEV_ID,            0x008005, 0x000002, 0x02000A, [0x0000]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_CONFIG,            0x008007, 0x000004, 0x02000E, [0x3FFF]],
   ]
])


PIC_DEVICE.append([
"18F2420",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x000000, 0x00100, 0x400000, [0xFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x000000, 0x04000, 0x000000, [0xFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x200000, 0x00008, 0x200000, [0xFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x3FFFFE, 0x00002, 0x3FFFFE, [0x00]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x300000, 0x0000F, 0x300000, 
                    [0x00, 0xCF, 0x1F, 0x1F, 0x00, 0x87, 0xC5, 0x00, 0x03, 0xC0, 0x03, 0xE0, 0x03, 0x40]],
   ]
])


PIC_DEVICE.append([
"18F2455",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x000000, 0x00100, 0x400000, [0xFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x000000, 0x06000, 0x000000, [0xFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x200000, 0x00008, 0x200000, [0xFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x3FFFFE, 0x00002, 0x3FFFFE, [0x00]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x300000, 0x0000F, 0x300000, 
                    [0x3F, 0xCF, 0x3F, 0x1F, 0x00, 0x87, 0xE5, 0x00, 0x07, 0xC0, 0x07, 0xE0, 0x07, 0x40]],
   ]
])


PIC_DEVICE.append([
"18F2520",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x000000, 0x00100, 0x400000, [0xFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x000000, 0x08000, 0x000000, [0xFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x200000, 0x00008, 0x200000, [0xFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x3FFFFE, 0x00002, 0x3FFFFE, [0x00]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x300000, 0x0000F, 0x300000, 
                    [0x00, 0xCF, 0x1F, 0x1F, 0x00, 0x87, 0xC5, 0x00, 0x0F, 0xC0, 0x0F, 0xE0, 0x0F, 0x40]],
   ]
])


PIC_DEVICE.append([
"18F2550",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x000000, 0x00100, 0x400000, [0xFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x000000, 0x08000, 0x000000, [0xFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x200000, 0x00008, 0x200000, [0xFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x3FFFFE, 0x00002, 0x3FFFFE, [0x00]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x300000, 0x0000F, 0x300000, 
                    [0x3F, 0xCF, 0x3F, 0x1F, 0x00, 0x87, 0xE5, 0x00, 0x0F, 0xC0, 0x0F, 0xE0, 0x0F, 0x40]],
   ]
])


PIC_DEVICE.append([
"18F4420",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x000000, 0x00100, 0x400000, [0xFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x000000, 0x04000, 0x000000, [0xFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x200000, 0x00008, 0x200000, [0xFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x3FFFFE, 0x00002, 0x3FFFFE, [0x00]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x300000, 0x0000F, 0x300000, 
                    [0x00, 0xCF, 0x1F, 0x1F, 0x00, 0x87, 0xC5, 0x00, 0x03, 0xC0, 0x03, 0xE0, 0x03, 0x40]],
   ]
])


PIC_DEVICE.append([
"18F4455",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x000000, 0x00100, 0x400000, [0xFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x000000, 0x06000, 0x000000, [0xFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x200000, 0x00008, 0x200000, [0xFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x3FFFFE, 0x00002, 0x3FFFFE, [0x00]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x300000, 0x0000F, 0x300000, 
                    [0x3F, 0xCF, 0x3F, 0x1F, 0x00, 0x87, 0xE5, 0x00, 0x07, 0xC0, 0x07, 0xE0, 0x07, 0x40]],
   ]
])


PIC_DEVICE.append([
"18F4520",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x000000, 0x00100, 0x400000, [0xFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x000000, 0x08000, 0x000000, [0xFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x200000, 0x00008, 0x200000, [0xFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x3FFFFE, 0x00002, 0x3FFFFE, [0x00]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x300000, 0x0000F, 0x300000, 
                    [0x00, 0xCF, 0x1F, 0x1F, 0x00, 0x87, 0xC5, 0x00, 0x0F, 0xC0, 0x0F, 0xE0, 0x0F, 0x40]],
   ]
])


PIC_DEVICE.append([
"18F4550",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x000000, 0x00100, 0x400000, [0xFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x000000, 0x08000, 0x000000, [0xFF]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ID,                0x200000, 0x00008, 0x200000, [0xFF]],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x3FFFFE, 0x00002, 0x3FFFFE, [0x00]],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_CONF|PICMEM_CONFIG,            0x300000, 0x0000F, 0x300000, 
                    [0x3F, 0xCF, 0x3F, 0x1F, 0x00, 0x87, 0xE5, 0x00, 0x0F, 0xC0, 0x0F, 0xE0, 0x0F, 0x40]],
   ]
])



LookupDeviceID = {
   0x0F80:"12F629",
   0x0FA0:"12F635",
   0x0FC0:"12F675",
   0x0460:"12F683",

   0x0560:"16F84A",
   0x0720:"16F87",
   0x0760:"16F88",

   0x07A0:"16F627",
   0x07B0:"16F628",
   0x1060:"16F628A",

   0x10C0:"16F630",
   0x1420:"16F631",
   0x10A0:"16F636",
   0x10A0:"16F639",
   0x10E0:"16F676",
   0x1440:"16F677",
   0x1080:"16F684",
   0x04A0:"16F685",
   0x1620:"16F687",
   0x1180:"16F688",
   0x1340:"16F689",
   0x1400:"16F690",
   0x1140:"16F716",

   0x2780:"16F1826",
   0x27A0:"16F1827",
   0x2880:"16LF1826",
   0x2720:"16F1823",
   0x2820:"16LF1823",
   0x2700:"12F1822",
   0x2800:"12LF1822",
   0x2740:"16F1824",
   0x2840:"16LF1824",
   0x2760:"16F1825",
   0x2860:"16LF1825",
   0x27C0:"16F1828",
   0x28C0:"16LF1828",
   0x27E0:"16F1829",
   0x28E0:"16LF1829",

   0x0D00:"16F870",
   0x0D20:"16F871",
   0x08E0:"16F872",
   0x0960:"16F873",
   0x0E40:"16F873A",
   0x0920:"16F874",
   0x0E60:"16F874A",
   0x09E0:"16F876",
   0x0E00:"16F876A",
   0x09A0:"16F877",
   0x0E20:"16F877A",
   0x2000:"16F882",
   0x2020:"16F883",
   0x2040:"16F884",
   0x2060:"16F886",
   0x2080:"16F887",

   0x3066:"16F18313",
   0x3068:"16LF18313",
   0x3067:"16F18323",
   0x3069:"16LF18323",
   0x303A:"16F18324",
   0x303C:"16LF18324",
   0x303B:"16F18344",
   0x303D:"16LF18344",
   0x303E:"16F18325",
   0x3040:"16LF18325",
   0x303F:"16F18345",
   0x3041:"16LF18345",
   0x30A4:"16F18326",
   0x30A6:"16LF18326",
   0x30A5:"16F18346",
   0x30A7:"16LF18346",
}

LookupDevice18fID = {
   0x2160:"18F2221",
   0x2120:"18F2321",
   0x1160:"18F2410",
   0x1140:"18F2420/18F2423",
   0x2420:"18F2450",
   0x1260:"18F2455",
   0x2A60:"18F2458",
   0x1AE0:"18F2480",
   0x1120:"18F2510",
   0x0CE0:"18F2515",
   0x1100:"18F2520/18F2523",
   0x0CC0:"18F2525",
   0x1240:"18F2550",
   0x2A40:"18F2553",
   0x1AC0:"18F2580",
   0x0EE0:"18F2585",
   0x0CA0:"18F2610",
   0x0C80:"18F2620",
   0x0EC0:"18F2680",
   0x2700:"18F2682",
   0x2720:"18F2685",
   0x2140:"18F4221",
   0x2100:"18F4321",
   0x10E0:"18F4410",
   0x10C0:"18F4420/18F4423",
   0x2400:"18F4450",
   0x1220:"18F4455",
   0x2A20:"18F4458",
   0x1AA0:"18F4480",
   0x10A0:"18F4510",
   0x0C60:"18F4515",
   0x1080:"18F4520/18F4523",
   0x0C40:"18F4525",
   0x1200:"18F4550",
   0x2A00:"18F4553",
   0x1A80:"18F4580",
   0x0EA0:"18F4585",
   0x0C20:"18F4610",
   0x0C00:"18F4620",
   0x0E80:"18F4680",
   0x2740:"18F4682",
   0x2760:"18F4685",
}



#/********************************************/
#/* Lookup full description of memory range. */
#/********************************************/
def Lookup(DeviceType):
   Result = ""
   ThisID = 1
   LookupIDs = DeviceType
   while LookupIDs != 0:
      ThisLookup = LookupIDs % 2
      if ThisLookup != 0:
         Result = Result + PICMEM_TYPE[PICMEM_TYPE_LOOKUP.index(ThisID)] + ":"

      ThisID = ThisID * 2
      LookupIDs = LookupIDs / 2

   return Result[:len(Result) - 1]



#/*****************************************/
#/* Lookup area and name of memory range. */
#/*****************************************/
def LookupName(DeviceType):
   return Lookup(DeviceType & DEVICE_MEM_NAME_MASK)

