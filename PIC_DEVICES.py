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
#/* ------------------------------------------------------------------------ */
#/* Python PIC Microcontroller Device Definitions.                           */
#/****************************************************************************/


#/*********************/
#/* PIC Memory Types. */
#/*********************/
PICMEM_NONAME  = 0x0000000000

PICMEM_RO      = 0x0000000001
PICMEM_WO      = 0x0000000002
PICMEM_RW      = 0x0000000004
PICMEM_ST      = 0x0000000008
PICMEM_RE      = 0x0000000010

PICMEM_EEPROM  = 0x0000000100
PICMEM_FLASH   = 0x0000000200

PICMEM_CONF    = 0x0000010000
PICMEM_DATA    = 0x0000020000
PICMEM_PROG    = 0x0000040000

PICMEM_ID      = 0x0001000000
PICMEM_DEV_ID  = 0x0002000000
PICMEM_CONFIG  = 0x0004000000
PICMEM_CONFIG2 = 0x0008000000
PICMEM_CAL     = 0x0010000000
PICMEM_BOR_CAL = 0x0020000000
PICMEM_OSC_CAL = 0x0040000000
PICMEM_CALIB   = 0x0080000000

DEVICE_TYPE_NAME_MASK = 0xFFFFFF0000

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
   PICMEM_CONFIG,          # Device config memory area.
   PICMEM_CONFIG2,         # Device config memory area extended.
   PICMEM_CAL,             # Device calibration memory area.
   PICMEM_BOR_CAL,         # Device brownout calibration memory area.
   PICMEM_OSC_CAL,         # Device oscilator calibration memory area.
   PICMEM_CALIB,           # Device brown out and power on calibration.
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
   "CONF",
   "CONF2",
   "CAL",
   "BOR_CAL",
   "OSC_CAL",
   "CALIB",
]



#/***************************************************************************/
#/* Define a PIC Microcontroller type:                                      */
#/* [                                                                       */
#/*    PIC Device Name,                                                     */
#/*    [                                                                    */
#/*       Memory Type, PIC Memory Area, Start Address, Length, Obj Address, */
#/*       Store/Restore Mask, Word Size                                     */
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
"READ_DEV_ID",
   [
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, 0x0000],
   ]
])


PIC_DEVICE.append([
"12F629",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0080, 0x4200, 0x0000],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x03FF, 0x0000, 0x0000],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ST|PICMEM_RE|PICMEM_OSC_CAL, 0x03FF, 0x0001, 0x03FF, 0x3FFF],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x0006, 0x0001, 0x4006, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CONFIG,  0x0007, 0x0001, 0x400E, 0x3000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CONFIG,  0x2007, 0x0001, 0x400E, 0x3000],
   ]
])


PIC_DEVICE.append([
"12F675",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0080, 0x4200, 0x0000],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x03FF, 0x0000, 0x0000],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ST|PICMEM_RE|PICMEM_OSC_CAL, 0x03FF, 0x0001, 0x03FF, 0x3FFF],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x0006, 0x0001, 0x4006, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CONFIG,  0x0007, 0x0001, 0x400E, 0x3000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CONFIG,  0x2007, 0x0001, 0x400E, 0x3000],
   ]
])


PIC_DEVICE.append([
"12F683",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, 0x0000],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x0800, 0x0000, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x0006, 0x0001, 0x4006, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_BOR_CAL, 0x0008, 0x0001, 0x400F, 0x3FFF],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_BOR_CAL, 0x2008, 0x0001, 0x400F, 0x3FFF],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CAL,     0x0009, 0x0001, 0x4010, 0x3FFF],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CAL,     0x2009, 0x0001, 0x4010, 0x3FFF],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CONFIG,  0x0007, 0x0001, 0x400E, 0x3000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CONFIG,  0x2007, 0x0001, 0x400E, 0x3000],
   ]
])


# **** TO IMPLEMENT AND TEST - Programming Spec 2 ****
#
# PIC_DEVICE.append([
# "16F88",
#    [
#       [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, 0x0000],
#       [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x1000, 0x0000, 0x0000],
#       [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, 0x0000],
#       [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, 0x0000],
#       [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x0006, 0x0001, 0x4006, 0x0000],
#       [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, 0x0000],
#       [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CONFIG,  0x0007, 0x0001, 0x400E, 0x0000],
#       [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CONFIG,  0x2007, 0x0001, 0x400E, 0x0000],
#       [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CONFIG2, 0x0008, 0x0001, 0x4008, 0x3FFF],
#       [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CONFIG2, 0x2008, 0x0001, 0x4008, 0x3FFF],
#    ]
# ])


# **** TO IMPLEMENT AND TEST - Programming Spec 2 ****
#
# PIC_DEVICE.append([
# "16F627",
#    [
#       [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0080, 0x4200, 0x0000],
#       [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x0400, 0x0000, 0x0000],
#       [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, 0x0000],
#       [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, 0x0000],
#       [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x0006, 0x0001, 0x4006, 0x0000],
#       [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, 0x0000],
#       [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CONFIG,  0x0007, 0x0001, 0x400E, 0x3000],
#       [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CONFIG,  0x2007, 0x0001, 0x400E, 0x3000],
#    ]
# ])


PIC_DEVICE.append([
"16F628A",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0080, 0x4200, 0x0000],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x0800, 0x0000, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x0006, 0x0001, 0x4006, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CONFIG,  0x0007, 0x0001, 0x400E, 0x3000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CONFIG,  0x2007, 0x0001, 0x400E, 0x3000],
   ]
])


PIC_DEVICE.append([
"16F630",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0080, 0x4200, 0x0000],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x03FF, 0x0000, 0x0000],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG|PICMEM_ST|PICMEM_RE|PICMEM_OSC_CAL, 0x03FF, 0x0001, 0x03FF, 0x3FFF],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x0006, 0x0001, 0x4006, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CONFIG,  0x0007, 0x0001, 0x400E, 0x3000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CONFIG,  0x2007, 0x0001, 0x400E, 0x3000],
   ]
])


PIC_DEVICE.append([
"16F684",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, 0x0000],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x0800, 0x0000, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x0006, 0x0001, 0x4006, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CONFIG,  0x0007, 0x0001, 0x400E, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CONFIG,  0x2007, 0x0001, 0x400E, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CALIB,   0x0008, 0x0001, 0x4008, 0x3FFF],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CALIB,   0x2008, 0x0001, 0x4008, 0x3FFF],
   ]
])


PIC_DEVICE.append([
"16F690",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, 0x0000],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x1000, 0x0000, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x0006, 0x0001, 0x4006, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CONFIG,  0x0007, 0x0001, 0x400E, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CONFIG,  0x2007, 0x0001, 0x400E, 0x0000],
   ]
])


# **** TO IMPLEMENT AND TEST - Programming Spec 2 ****
#
# PIC_DEVICE.append([
# "16F876A",
#    [
#       [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, 0x0000],
#       [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x2000, 0x0000, 0x0000],
#       [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, 0x0000],
#       [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, 0x0000],
#       [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x0006, 0x0001, 0x4006, 0x0000],
#       [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, 0x0000],
#       [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CONFIG,  0x0007, 0x0001, 0x400E, 0x0000],
#       [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CONFIG,  0x2007, 0x0001, 0x400E, 0x0000],
#    ]
# ])


PIC_DEVICE.append([
"16F886",
   [
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, 0x0000],
      [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x2000, 0x0000, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x0006, 0x0001, 0x4006, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CONFIG,  0x0007, 0x0001, 0x400E, 0x0000],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CONFIG,  0x2007, 0x0001, 0x400E, 0x0000],
      [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CONFIG2, 0x0008, 0x0001, 0x4008, 0x3FFF],
      [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CONFIG2, 0x2008, 0x0001, 0x4008, 0x3FFF],
   ]
])


# **** TO IMPLEMENT AND TEST ****
#
# PIC_DEVICE.append([
# "16F877A",
#    [
#       [PICMEM_RW|PICMEM_EEPROM|PICMEM_DATA,                          0x0000, 0x0100, 0x4200, 0x0000],
#       [PICMEM_RW|PICMEM_EEPROM|PICMEM_PROG,                          0x0000, 0x2000, 0x0000, 0x0000],
#       [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x0000, 0x0004, 0x4000, 0x0000],
#       [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ID,                0x2000, 0x0004, 0x4000, 0x0000],
#       [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x0006, 0x0001, 0x4006, 0x0000],
#       [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_DEV_ID,            0x2006, 0x0001, 0x4006, 0x0000],
#       [PICMEM_WO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_RE|PICMEM_CONFIG,  0x0007, 0x0001, 0x400E, 0x0000],
#       [PICMEM_RO|PICMEM_EEPROM|PICMEM_CONF|PICMEM_ST|PICMEM_CONFIG,  0x2007, 0x0001, 0x400E, 0x0000],
#    ]
# ])


# **** TO IMPLEMENT AND TEST - 16bit Programming ****
#
# 18F2520



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
   return Lookup(DeviceType & DEVICE_TYPE_NAME_MASK)

