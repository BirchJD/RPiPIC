#!/usr/bin/python2

# PIC - Python PIC Microcontroller Low Level Functions
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
#/* PIC                                                                      */
#/* ------------------------------------------------------------------------ */
#/* V1.00 - 2016-12-22 - Jason Birch                                         */
#/* ------------------------------------------------------------------------ */
#/* Python PIC Microcontroller Low Level Functions.                          */
#/****************************************************************************/


import time
import math
import RPi.GPIO


#/**************************************/
#/* Raspberry Pi GPIO pin allocations. */
#/**************************************/
GPIO_VDD_PIN = 27
GPIO_PGM_PIN = 17
GPIO_CLK_PIN = 9
GPIO_DATA_IN_PIN = 22
GPIO_DATA_OUT_PIN = 10



#/******************************/
#/* Timinig delay definitions. */
#/******************************/
# Target 100nS between each clock transition.
# NOTE: Calling a function in Python will probably exceed the required period.
SLEEP_CLOCK = 100 / 1000000000.0
SLEEP_CLOCK_READ = 1000 / 1000000000.0
# Target 1uS between each command and data.
# NOTE: Calling a function in Python will probably exceed the required period.
SLEEP_DATA = 1 / 1000000.0
# Target 100uS program pulse width.
# NOTE: This is for Flash type memory on older devices, using program pulses.
PIC_DELAY_FLASH_PROGRAM = 150 / 1000000.0
# Target 6mS to erase EEPROM memory location.
PIC_DELAY_EEPROM_ERASE = 10 / 1000.0
# Target 8mS to write EEPROM memory location.
PIC_DELAY_EEPROM_PROGRAM = 10 / 1000.0
# Target 5uS power on program mode.
PIC_DELAY_POWER_PROGRAM = 10 / 1000000.0



#/************************************/
#/* PIC Memory location definitions. */
#/************************************/
PIC_BLANK_PROG_WORD = 0x3FFF
PIC_BLANK_PROG_WORD_FORMAT = "{:04X}"
PIC_BLANK_DATA_WORD = 0xFF
PIC_BLANK_DATA_WORD_FORMAT = "{:02X}"
PIC_PROG_PULSE_COUNT = 1


#/*************************************/
#/* GPIO pin level value definitions. */
#/*************************************/
PIC_VDD_OFF = 0
PIC_VDD_ON = 1
PIC_PGM_OFF = 0
PIC_PGM_ON = 1
PIC_CLK_OFF = 1
PIC_CLK_ON = 0
PIC_IN_DATA_0 = 1
PIC_IN_DATA_1 = 0
PIC_OUT_DATA_0 = 1
PIC_OUT_DATA_1 = 0


#/*********************************/
#/* PIC ICSP command definitions. */
#/*********************************/
PIC_CMD_BIT_COUNT = 6
PIC_DATA_BIT_COUNT = 16

PIC_CMD_LOAD_CONFIG      = 0x00
PIC_CMD_ERASE_SETUP1     = 0x01
PIC_CMD_LOAD_PROG        = 0x02
PIC_CMD_LOAD_DATA        = 0x03
PIC_CMD_READ_PROG        = 0x04
PIC_CMD_READ_DATA        = 0x05
PIC_CMD_INC_ADDRESS      = 0x06
PIC_CMD_ERASE_SETUP2     = 0x07
PIC_CMD_BEGIN_ERASE_PROG = 0x08
PIC_CMD_ERASE_PROG_MEM   = 0x09
PIC_CMD_ERASE_DATA_MEM   = 0x0B
PIC_CMD_END_PROGRAM      = 0x0E
PIC_CMD_BEGIN_PROG_ONLY  = 0x18



#/***********************/
#/* LOW LEVEL FUNCTIONS */
#/***********************/
def DataRead(BitCount):
   RPi.GPIO.output(GPIO_DATA_OUT_PIN, PIC_OUT_DATA_1)
   time.sleep(SLEEP_DATA)

   PicDataWord = 0
   for Count in range(BitCount):
      RPi.GPIO.output(GPIO_CLK_PIN, PIC_CLK_ON)
      time.sleep(SLEEP_CLOCK_READ)
      RPi.GPIO.output(GPIO_CLK_PIN, PIC_CLK_OFF)
      time.sleep(SLEEP_CLOCK_READ)

      if RPi.GPIO.input(GPIO_DATA_IN_PIN) == PIC_IN_DATA_1:
         PicDataWord = PicDataWord | int(math.pow(2, Count))

   PicDataWord = (PicDataWord & 0x7FFE) / 2

   return PicDataWord



def DataWrite(PicDataWord, BitCount):
   if BitCount == PIC_DATA_BIT_COUNT:
      PicDataWord = PicDataWord * 2

   for Count in range(BitCount):
      Bit = (PicDataWord % 2)
      if Bit == 0:
         RPi.GPIO.output(GPIO_DATA_OUT_PIN, PIC_OUT_DATA_0)
      else:
         RPi.GPIO.output(GPIO_DATA_OUT_PIN, PIC_OUT_DATA_1)

      RPi.GPIO.output(GPIO_CLK_PIN, PIC_CLK_ON)
      time.sleep(SLEEP_CLOCK)
      RPi.GPIO.output(GPIO_CLK_PIN, PIC_CLK_OFF)
      time.sleep(SLEEP_CLOCK)

      PicDataWord = PicDataWord / 2



def CmdLoadConfig(PicDataWord):
   DataWrite(PIC_CMD_LOAD_CONFIG, PIC_CMD_BIT_COUNT)
   time.sleep(SLEEP_DATA)
   DataWrite(PicDataWord, PIC_DATA_BIT_COUNT)



def CmdLoadProg(PicDataWord):
   DataWrite(PIC_CMD_LOAD_PROG, PIC_CMD_BIT_COUNT)
   time.sleep(SLEEP_DATA)
   DataWrite(PicDataWord, PIC_DATA_BIT_COUNT)



def CmdReadProg():
   DataWrite(PIC_CMD_READ_PROG, PIC_CMD_BIT_COUNT)
   time.sleep(SLEEP_DATA)
   PicDataWord = DataRead(PIC_DATA_BIT_COUNT)

   return PicDataWord



def CmdLoadData(PicDataWord):
   DataWrite(PIC_CMD_LOAD_DATA, PIC_CMD_BIT_COUNT)
   time.sleep(SLEEP_DATA)
   DataWrite(PicDataWord, PIC_DATA_BIT_COUNT)



def CmdReadData():
   DataWrite(PIC_CMD_READ_DATA, PIC_CMD_BIT_COUNT)
   time.sleep(SLEEP_DATA)
   PicDataWord = DataRead(PIC_DATA_BIT_COUNT)

   return PicDataWord



def CmdIncAddress():
   DataWrite(PIC_CMD_INC_ADDRESS, PIC_CMD_BIT_COUNT)



def CmdBeginProgram():
   DataWrite(PIC_CMD_BEGIN_PROG_ONLY, PIC_CMD_BIT_COUNT)



def CmdEndProgram():
   DataWrite(PIC_CMD_END_PROGRAM, PIC_CMD_BIT_COUNT)



def CmdBeginEraseProgram():
   DataWrite(PIC_CMD_BEGIN_ERASE_PROG, PIC_CMD_BIT_COUNT)



def CmdEraseProgMemory():
   DataWrite(PIC_CMD_ERASE_PROG_MEM, PIC_CMD_BIT_COUNT)



def CmdEraseDataMemory():
   DataWrite(PIC_CMD_ERASE_DATA_MEM, PIC_CMD_BIT_COUNT)

