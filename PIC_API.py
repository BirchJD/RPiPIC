#!/usr/bin/python2

# PIC_API - Python PIC Microcontroller API
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
#/* PIC_API                                                                  */
#/* ------------------------------------------------------------------------ */
#/* V1.00 - 2016-12-22 - Jason Birch                                         */
#/* ------------------------------------------------------------------------ */
#/* Python PIC Microcontroller API.                                          */
#/****************************************************************************/


import time
import datetime
import RPi.GPIO
import PIC


PIC_BLANK_PROG_WORD = PIC.PIC_BLANK_PROG_WORD
PIC_BLANK_PROG_WORD_FORMAT = PIC.PIC_BLANK_PROG_WORD_FORMAT
PIC_BLANK_DATA_WORD = PIC.PIC_BLANK_DATA_WORD
PIC_BLANK_DATA_WORD_FORMAT = PIC.PIC_BLANK_DATA_WORD_FORMAT
PIC_PROG_PULSE_COUNT = PIC.PIC_PROG_PULSE_COUNT
PIC_DELAY_FLASH_PROGRAM = PIC.PIC_DELAY_FLASH_PROGRAM
PIC_DELAY_EEPROM_ERASE = PIC.PIC_DELAY_EEPROM_ERASE
PIC_DELAY_EEPROM_PROGRAM = PIC.PIC_DELAY_EEPROM_PROGRAM



#/***********************/
#/* API LEVEL FUNCTIONS */
#/***********************/

#  /*******************************************/
# /* Configure Raspberry Pi GPIO interfaces. */
#/*******************************************/
def InitGPIO():
   RPi.GPIO.setwarnings(False)
   RPi.GPIO.setmode(RPi.GPIO.BCM)
   RPi.GPIO.setup(PIC.GPIO_VDD_PIN, RPi.GPIO.OUT, initial=0)
   RPi.GPIO.setup(PIC.GPIO_PGM_PIN, RPi.GPIO.OUT, initial=0)
   RPi.GPIO.setup(PIC.GPIO_CLK_PIN, RPi.GPIO.OUT, initial=0)
   RPi.GPIO.setup(PIC.GPIO_DATA_OUT_PIN, RPi.GPIO.OUT, initial=0)
   RPi.GPIO.setup(PIC.GPIO_DATA_IN_PIN, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)

   RPi.GPIO.output(PIC.GPIO_VDD_PIN, PIC.PIC_VDD_OFF)
   RPi.GPIO.output(PIC.GPIO_PGM_PIN, PIC.PIC_PGM_OFF)
   RPi.GPIO.output(PIC.GPIO_CLK_PIN, PIC.PIC_CLK_OFF)
   RPi.GPIO.output(PIC.GPIO_DATA_OUT_PIN, PIC.PIC_OUT_DATA_0)



def ProgrammerPresent():
   RPi.GPIO.output(PIC.GPIO_DATA_OUT_PIN, PIC.PIC_OUT_DATA_1)
   if RPi.GPIO.input(PIC.GPIO_DATA_IN_PIN) == PIC.PIC_IN_DATA_1:
      return True
   else:
      return False



def PowerOnDevice():
   RPi.GPIO.setwarnings(False)
   RPi.GPIO.setmode(RPi.GPIO.BCM)
   RPi.GPIO.setup(PIC.GPIO_VDD_PIN, RPi.GPIO.OUT, initial=0)
   RPi.GPIO.output(PIC.GPIO_VDD_PIN, PIC.PIC_VDD_ON)



def PowerOffDevice():
   RPi.GPIO.setwarnings(False)
   RPi.GPIO.setmode(RPi.GPIO.BCM)
   RPi.GPIO.setup(PIC.GPIO_VDD_PIN, RPi.GPIO.OUT, initial=0)
   RPi.GPIO.output(PIC.GPIO_VDD_PIN, PIC.PIC_VDD_OFF)



def ProgramModeStart():
   RPi.GPIO.output(PIC.GPIO_VDD_PIN, PIC.PIC_VDD_ON)
   RPi.GPIO.output(PIC.GPIO_PGM_PIN, PIC.PIC_PGM_ON)
   RPi.GPIO.output(PIC.GPIO_CLK_PIN, PIC.PIC_CLK_OFF)
   RPi.GPIO.output(PIC.GPIO_DATA_OUT_PIN, PIC.PIC_OUT_DATA_0)



def ProgramModeEnd():
   RPi.GPIO.output(PIC.GPIO_VDD_PIN, PIC.PIC_VDD_OFF)
   RPi.GPIO.output(PIC.GPIO_PGM_PIN, PIC.PIC_PGM_OFF)
   RPi.GPIO.output(PIC.GPIO_CLK_PIN, PIC.PIC_CLK_OFF)
   RPi.GPIO.output(PIC.GPIO_DATA_OUT_PIN, PIC.PIC_OUT_DATA_0)



def EraseProgramMemory():
   PIC.CmdLoadProg(PIC_BLANK_PROG_WORD)
   PIC.CmdBeginEraseProgram()
   PIC.CmdEraseProgMemory()
   time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)



def EraseDataMemory():
   PIC.CmdLoadProg(PIC_BLANK_PROG_WORD)
   PIC.CmdBeginEraseProgram()
   PIC.CmdEraseDataMemory()
   time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)



def IncLocation():
   PIC.CmdIncAddress()



def ReadProgLocation():
   return PIC.CmdReadProg()



def ReadDataLocation():
   return PIC.CmdReadData()



def ConfigMode():
   PIC.CmdLoadConfig(0x00)



def ProgramConfigLocation(PicDataWord, PulseCount):
   PIC.CmdLoadConfig(PicDataWord)

# Pulse loop for Flash memory programming.
# PulseCount = 1 for EEPROM memory.
   AvgPeriod = 0
   for Count in range(PulseCount):
      PIC.CmdBeginEraseProgram()
      time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)
      time.sleep(PIC.PIC_DELAY_EEPROM_PROGRAM)

# Flash memory programming sample.
#      StartTime = datetime.datetime.now().microsecond
#      EndTime = StartTime
#      while EndTime - StartTime < PIC.PIC_DELAY_EEPROM_PROGRAM:
#         EndTime = datetime.datetime.now().microsecond
#      PIC.CmdEndProgram()
#      EndTime = datetime.datetime.now().microsecond
#      if AvgPeriod == 0:
#         AvgPeriod = EndTime - StartTime
#      else:
#         AvgPeriod = (AvgPeriod + (EndTime - StartTime)) / 2

   return AvgPeriod



def ProgramMemoryLocation(PicDataWord, PulseCount):
   PIC.CmdLoadProg(PicDataWord)

# Pulse loop for Flash memory programming.
# PulseCount = 1 for EEPROM memory.
   AvgPeriod = 0
   for Count in range(PulseCount):
      PIC.CmdBeginEraseProgram()
      time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)
      time.sleep(PIC.PIC_DELAY_EEPROM_PROGRAM)

# Flash memory programming sample.
#      StartTime = datetime.datetime.now().microsecond
#      EndTime = StartTime
#      while EndTime - StartTime < PIC.PIC_DELAY_EEPROM_PROGRAM:
#         EndTime = datetime.datetime.now().microsecond
#      PIC.CmdEndProgram()
#      EndTime = datetime.datetime.now().microsecond
#      if AvgPeriod == 0:
#         AvgPeriod = EndTime - StartTime
#      else:
#         AvgPeriod = (AvgPeriod + (EndTime - StartTime)) / 2

   return AvgPeriod



def ProgramDataLocation(PicDataWord, PulseCount):
   PIC.CmdLoadData(PicDataWord)

# Pulse loop for Flash memory programming.
# PulseCount = 1 for EEPROM memory.
   AvgPeriod = 0
   for Count in range(PulseCount):
      PIC.CmdBeginEraseProgram()
      time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)
      time.sleep(PIC.PIC_DELAY_EEPROM_PROGRAM)

# Flash memory programming sample.
#      StartTime = datetime.datetime.now().microsecond
#      EndTime = StartTime
#      while EndTime - StartTime < PIC.PIC_DELAY_EEPROM_PROGRAM:
#         EndTime = datetime.datetime.now().microsecond
#      PIC.CmdEndProgram()
#      EndTime = datetime.datetime.now().microsecond
#      if AvgPeriod == 0:
#         AvgPeriod = EndTime - StartTime
#      else:
#         AvgPeriod = (AvgPeriod + (EndTime - StartTime)) / 2

   return AvgPeriod

