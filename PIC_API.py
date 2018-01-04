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
#/* V1.01 - 2017-12-30 - Added support for PIC18F device programming.        */
#/* ------------------------------------------------------------------------ */
#/* Python PIC Microcontroller API.                                          */
#/****************************************************************************/


import sys
import time
import datetime
import RPi.GPIO
import PIC


PIC_BLANK_CONFIG_WORD = PIC.PIC_BLANK_CONFIG_WORD
PIC_BLANK_PROG_WORD = PIC.PIC_BLANK_PROG_WORD
PIC_BLANK_PROG_WORD_18F = PIC.PIC_BLANK_PROG_WORD_18F
PIC_BLANK_DATA_WORD = PIC.PIC_BLANK_DATA_WORD
PIC_BLANK_DATA_WORD_18F = PIC.PIC_BLANK_DATA_WORD_18F
PIC_PROG_PULSE_COUNT = PIC.PIC_PROG_PULSE_COUNT
PIC_DELAY_FLASH_PROGRAM = PIC.PIC_DELAY_FLASH_PROGRAM
PIC_DELAY_EEPROM_ERASE = PIC.PIC_DELAY_EEPROM_ERASE
PIC_DELAY_EEPROM_PROGRAM = PIC.PIC_DELAY_EEPROM_PROGRAM



#/***************************/
#/* PIC API LEVEL FUNCTIONS */
#/***************************/

#  /*******************************************/
# /* Configure Raspberry Pi GPIO interfaces. */
#/*******************************************/
def InitGPIO():
   RPi.GPIO.setwarnings(False)
   RPi.GPIO.setmode(RPi.GPIO.BCM)
   RPi.GPIO.setup(PIC.GPIO_PGM_PIN, RPi.GPIO.OUT, initial=PIC.PIC_PGM_OFF)
   RPi.GPIO.setup(PIC.GPIO_VDD_PIN, RPi.GPIO.OUT, initial=PIC.PIC_VDD_OFF)
   RPi.GPIO.setup(PIC.GPIO_CLK_PIN, RPi.GPIO.OUT, initial=PIC.PIC_CLK_OFF)
   RPi.GPIO.setup(PIC.GPIO_DATA_OUT_PIN, RPi.GPIO.OUT, initial=PIC.PIC_OUT_DATA_0)
   RPi.GPIO.setup(PIC.GPIO_DATA_IN_PIN, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)



def ProgrammerPresent():
   RPi.GPIO.output(PIC.GPIO_DATA_OUT_PIN, PIC.PIC_OUT_DATA_1)
   if RPi.GPIO.input(PIC.GPIO_DATA_IN_PIN) == PIC.PIC_IN_DATA_1:
      return True
   else:
      return False



def PowerOnDevice():
   RPi.GPIO.setwarnings(False)
   RPi.GPIO.setmode(RPi.GPIO.BCM)
   RPi.GPIO.setup(PIC.GPIO_VDD_PIN, RPi.GPIO.OUT, initial=PIC.PIC_VDD_ON)



def PowerOffDevice():
   RPi.GPIO.setwarnings(False)
   RPi.GPIO.setmode(RPi.GPIO.BCM)
   RPi.GPIO.setup(PIC.GPIO_VDD_PIN, RPi.GPIO.OUT, initial=PIC.PIC_VDD_OFF)



def ProgramModeStart(PicDevice):
   ProgramModeEnd()
   if PicDevice in ["16F88", "16F627", "16F876A", "16F877A"]:
      RPi.GPIO.output(PIC.GPIO_VDD_PIN, PIC.PIC_VDD_ON)
      time.sleep(PIC.PIC_DELAY_POWER_PROGRAM)
      RPi.GPIO.output(PIC.GPIO_PGM_PIN, PIC.PIC_PGM_ON)
      time.sleep(PIC.PIC_DELAY_POWER_PROGRAM)
   else:
      RPi.GPIO.output(PIC.GPIO_PGM_PIN, PIC.PIC_PGM_ON)
      time.sleep(PIC.PIC_DELAY_POWER_PROGRAM)
      RPi.GPIO.output(PIC.GPIO_VDD_PIN, PIC.PIC_VDD_ON)
      time.sleep(PIC.PIC_DELAY_POWER_PROGRAM)

   RPi.GPIO.output(PIC.GPIO_DATA_OUT_PIN, PIC.PIC_OUT_DATA_1)


def ProgramModeEnd():
   RPi.GPIO.output(PIC.GPIO_DATA_OUT_PIN, PIC.PIC_OUT_DATA_0)
   RPi.GPIO.output(PIC.GPIO_CLK_PIN, PIC.PIC_CLK_OFF)
   RPi.GPIO.output(PIC.GPIO_VDD_PIN, PIC.PIC_VDD_OFF)
   RPi.GPIO.output(PIC.GPIO_PGM_PIN, PIC.PIC_PGM_OFF)



def IncLocation():
   PIC.CmdIncAddress()



def Seek(PicDevice, Address, IsOffset = False):
   sys.stdout.write("\n")
   if IsOffset == True:
      OffsetChar = "+"
   else:
      OffsetChar = ""

   if PicDevice[:3] in ["12F", "16F"]:
      Count = 0
      for Count in range(Address):
         if Count % 100 == 0:
            sys.stdout.write("SEEK {:}{:08X}\r".format(OffsetChar, Count))
            sys.stdout.flush()
         IncLocation()
      sys.stdout.write("SEEK {:}{:08X}\n".format(OffsetChar, Count))
   elif PicDevice[:3] in ["18F"]:
      sys.stdout.write("SEEK {:}{:08X}\n".format(OffsetChar, Address))



def EraseChip(PicDevice):
   ConfigMode(PicDevice, PIC_BLANK_CONFIG_WORD)
   PIC.CmdEraseChip()
   time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)
   time.sleep(PIC.PIC_DELAY_EEPROM_PROGRAM)



def EraseProgramMemory(SetWordFlag = False):
   if SetWordFlag == True:
      PIC.CmdLoadProg(PIC_BLANK_PROG_WORD)
      PIC.CmdBeginEraseProgram()
      time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)
      time.sleep(PIC.PIC_DELAY_EEPROM_PROGRAM)
   PIC.CmdEraseProgMemory()
   time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)
   time.sleep(PIC.PIC_DELAY_EEPROM_PROGRAM)



def EraseDataMemory(SetWordFlag = False):
   if SetWordFlag == True:
      PIC.CmdLoadProg(PIC_BLANK_DATA_WORD)
      PIC.CmdBeginEraseProgram()
      time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)
      time.sleep(PIC.PIC_DELAY_EEPROM_PROGRAM)
   PIC.CmdEraseDataMemory()
   time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)
   time.sleep(PIC.PIC_DELAY_EEPROM_PROGRAM)



def EraseAllProcess_1():
   PIC.CmdLoadConfig(0x0000)
   for Count in range(7):
      PIC.CmdIncAddress()
   PIC.CmdEraseSetup1()
   PIC.CmdEraseSetup2()
   PIC.CmdLoadProg(PIC_BLANK_PROG_WORD)
   PIC.CmdBeginEraseProgram()
   time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)
   time.sleep(PIC.PIC_DELAY_EEPROM_PROGRAM)
   PIC.CmdEraseSetup1()
   PIC.CmdEraseSetup2()



def EraseAllMemory(PicDevice):
   if PicDevice[:3] in ["12F", "16F"]:
      if PicDevice in ["16F88", "16F876A", "16F877A"]:
         EraseChip(PicDevice)
      elif PicDevice in ["16F627"]:
         EraseAllProcess_1()
      else:
         EraseProgramMemory()
         ConfigMode(PicDevice, PIC_BLANK_CONFIG_WORD)
         EraseProgramMemory()
         EraseDataMemory()
   elif PicDevice[:3] in ["18F"]:
      PIC.CmdBulkErase_18F()
      time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)
      time.sleep(PIC.PIC_DELAY_EEPROM_PROGRAM)



def ConfigMode(PicDevice, PicDataWord):
   if PicDevice[:3] in ["12F", "16F"]:
      PIC.CmdLoadConfig(PicDataWord)



def ReadConfigLocation(PicDevice, Address, Bytes = 1):
   if PicDevice[:3] in ["12F", "16F"]:
      Data = PIC.CmdReadProg()
      IncLocation()
   elif PicDevice[:3] in ["18F"]:
      Data = PIC.CmdReadProg_18F(Address, True)
      if Bytes == 2:
         Data = Data | (PIC.CmdReadProg_18F(Address + 1, True) << 8)
   return Data



def ReadProgLocation(PicDevice, Address, Bytes = 1):
   if PicDevice[:3] in ["12F", "16F"]:
      Data = (PIC.CmdReadProg() & PIC.PIC_BLANK_PROG_WORD)
      IncLocation()
   elif PicDevice[:3] in ["18F"]:
      Data = (PIC.CmdReadProg_18F(Address) & PIC.PIC_BLANK_PROG_WORD_18F)
      if Bytes == 2:
         Data = Data | ((PIC.CmdReadProg_18F(Address + 1) & PIC.PIC_BLANK_PROG_WORD_18F) << 8)
   return Data



def ReadDataLocation(PicDevice, Address):
   if PicDevice[:3] in ["12F", "16F"]:
      Data = (PIC.CmdReadData() & PIC.PIC_BLANK_DATA_WORD)
      IncLocation()
   elif PicDevice[:3] in ["18F"]:
      Data = (PIC.CmdReadData_18F(Address) & PIC.PIC_BLANK_DATA_WORD_18F)
   return Data



def ProgramConfigLocation(PicDevice, Address, PicDataWord, PulseCount):
   if PicDevice[:3] in ["12F", "16F"]:
      PIC.CmdLoadConfig(PicDataWord)
# Pulse loop for Flash memory programming.
# For EEPROM memory, PulseCount = 1.
      for Count in range(PulseCount):
         PIC.CmdBeginEraseProgram()
         time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)
         time.sleep(PIC.PIC_DELAY_EEPROM_PROGRAM)
         if PicDevice in ["16F88", "16F876A", "16F877A"]:
            PIC.CmdEndProgramming()
   elif PicDevice[:3] in ["18F"]:
      PIC.CmdLoadProg_18F(Address, PicDataWord, True)



def ProgramMemoryLocation(PicDevice, Address, PicDataWord, PulseCount, ConfigMode = False):
   if PicDevice[:3] in ["12F", "16F"]:
      PIC.CmdLoadProg(PicDataWord)
# Pulse loop for Flash memory programming.
# For EEPROM memory, PulseCount = 1.
      for Count in range(PulseCount):
         if PicDevice in ["16F88"]:
            PIC.CmdBeginProgramOnly()
         elif ConfigMode == False and PicDevice in ["16F876A", "16F877A"]:
            PIC.CmdBeginProgramOnly()
         else:
            PIC.CmdBeginEraseProgram()
         time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)
         time.sleep(PIC.PIC_DELAY_EEPROM_PROGRAM)
         if PicDevice in ["16F88"]:
            time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)
            time.sleep(PIC.PIC_DELAY_EEPROM_PROGRAM)
         if PicDevice in ["16F88", "16F876A", "16F877A"]:
            PIC.CmdEndProgramming()
   elif PicDevice[:3] in ["18F"]:
      PIC.CmdLoadProg_18F(Address, PicDataWord)



def ProgramDataLocation(PicDevice, Address, PicDataWord, PulseCount):
   if PicDevice[:3] in ["12F", "16F"]:
      PIC.CmdLoadData(PicDataWord)
# Pulse loop for Flash memory programming.
# For EEPROM memory, PulseCount = 1.
      for Count in range(PulseCount):
         if PicDevice in ["16F88"]:
            PIC.CmdBeginProgramOnly()
         elif ConfigMode == False and PicDevice in ["16F876A", "16F877A"]:
            PIC.CmdBeginProgramOnly()
         else:
            PIC.CmdBeginEraseProgram()
         time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)
         time.sleep(PIC.PIC_DELAY_EEPROM_PROGRAM)
         if PicDevice in ["16F88"]:
            time.sleep(PIC.PIC_DELAY_EEPROM_ERASE)
            time.sleep(PIC.PIC_DELAY_EEPROM_PROGRAM)
         if PicDevice in ["16F88", "16F876A", "16F877A"]:
            PIC.CmdEndProgramming()
   elif PicDevice[:3] in ["18F"]:
      PIC.CmdLoadData_18F(Address, PicDataWord)



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

