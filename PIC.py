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
#/* V1.01 - 2017-12-30 - Added support for PIC18F device programming.        */
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
EEWRITE_TIMEOUT = 1024

SLEEP_CLOCK_WRITE = 1 / 10000000.0
SLEEP_CLOCK_READ = 1 / 1000000.0
SLEEP_DATA = 1 / 1000000.0

PIC_DELAY_POWER_PROGRAM = 1 / 100000.0
PIC_DELAY_FLASH_PROGRAM = 15 / 100000.0
PIC_DELAY_EEPROM_ERASE = 1 / 100.0
PIC_DELAY_EEPROM_PROGRAM = 1 / 100.0


SLEEP_CLOCK_WRITE_18F = 1 / 10000000.0
SLEEP_CLOCK_READ_18F = 1 / 1000000.0

PIC_DELAY_EEPROM_PROGRAM_18F = 1 / 10000.0


#/************************************/
#/* PIC Memory location definitions. */
#/************************************/
PIC_BLANK_CONFIG_WORD = 0xFFFF
PIC_BLANK_PROG_WORD = 0x3FFF
PIC_BLANK_PROG_WORD_18F = 0x00FF
PIC_BLANK_DATA_WORD = 0x00FF
PIC_BLANK_DATA_WORD_18F = 0x00FF
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


#/*******************************************/
#/* PIC12F/PIC16F ICSP command definitions. */
#/*******************************************/
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
PIC_CMD_END_PROGRAMMING_1= 0x0A
PIC_CMD_ERASE_DATA_MEM   = 0x0B
PIC_CMD_END_PROGRAM      = 0x0E
PIC_CMD_ROW_ERASE_PROG   = 0x11
PIC_CMD_END_PROGRAMMING  = 0x17
PIC_CMD_BEGIN_PROG_ONLY  = 0x18
PIC_CMD_CHIP_ERASE       = 0x1F


#/************************************/
#/* PIC18F ICSP command definitions. */
#/************************************/
PIC18_CMD_BIT_COUNT = 4
PIC18_DATA_BIT_COUNT = 16

PIC18_CMD_CORE_CMD         = 0x00
PIC18_CMD_READ_TABLAT      = 0x02
PIC18_CMD_READ             = 0x08
PIC18_CMD_READ_INC         = 0x09
PIC18_CMD_READ_DEC         = 0x0A
PIC18_CMD_INC_READ         = 0x0B
PIC18_CMD_WRITE            = 0x0C
PIC18_CMD_WRITE_INC2       = 0x0D
PIC18_CMD_WRITE_INC2_PROG  = 0x0E
PIC18_CMD_WRITE_PROG       = 0x0F



#/*************************************/
#/* PIC12F/PIC16F LOW LEVEL FUNCTIONS */
#/*************************************/
def DataRead(BitCount):
   RPi.GPIO.output(GPIO_DATA_OUT_PIN, PIC_OUT_DATA_1)
   time.sleep(SLEEP_DATA)

   PicDataWord = 0
   for Count in range(BitCount):
      RPi.GPIO.output(GPIO_CLK_PIN, PIC_CLK_ON)
      time.sleep(SLEEP_CLOCK_READ)

      if RPi.GPIO.input(GPIO_DATA_IN_PIN) == PIC_IN_DATA_1:
         PicDataWord = PicDataWord | int(math.pow(2, Count))

      RPi.GPIO.output(GPIO_CLK_PIN, PIC_CLK_OFF)
      time.sleep(SLEEP_CLOCK_READ)

   PicDataWord = (PicDataWord & 0x7FFE) / 2

   return PicDataWord



def DataWrite(PicDataWord, BitCount):
   if BitCount == PIC_DATA_BIT_COUNT:
      PicDataWord = PicDataWord * 2

   time.sleep(SLEEP_DATA)

   for Count in range(BitCount):
      RPi.GPIO.output(GPIO_CLK_PIN, PIC_CLK_ON)

      Bit = (PicDataWord % 2)
      if Bit == 0:
         RPi.GPIO.output(GPIO_DATA_OUT_PIN, PIC_OUT_DATA_0)
      else:
         RPi.GPIO.output(GPIO_DATA_OUT_PIN, PIC_OUT_DATA_1)

      time.sleep(SLEEP_CLOCK_WRITE)
      RPi.GPIO.output(GPIO_CLK_PIN, PIC_CLK_OFF)
      time.sleep(SLEEP_CLOCK_WRITE)

      PicDataWord = PicDataWord / 2

   RPi.GPIO.output(GPIO_DATA_OUT_PIN, PIC_OUT_DATA_0)



def CmdLoadConfig(PicDataWord):
   DataWrite(PIC_CMD_LOAD_CONFIG, PIC_CMD_BIT_COUNT)
   DataWrite(PicDataWord, PIC_DATA_BIT_COUNT)



def CmdLoadProg(PicDataWord):
   DataWrite(PIC_CMD_LOAD_PROG, PIC_CMD_BIT_COUNT)
   DataWrite(PicDataWord, PIC_DATA_BIT_COUNT)



def CmdReadProg():
   DataWrite(PIC_CMD_READ_PROG, PIC_CMD_BIT_COUNT)
   PicDataWord = DataRead(PIC_DATA_BIT_COUNT)

   return PicDataWord



def CmdLoadData(PicDataWord):
   DataWrite(PIC_CMD_LOAD_DATA, PIC_CMD_BIT_COUNT)
   DataWrite(PicDataWord, PIC_DATA_BIT_COUNT)



def CmdReadData():
   DataWrite(PIC_CMD_READ_DATA, PIC_CMD_BIT_COUNT)
   PicDataWord = DataRead(PIC_DATA_BIT_COUNT)

   return PicDataWord



def CmdIncAddress():
   DataWrite(PIC_CMD_INC_ADDRESS, PIC_CMD_BIT_COUNT)



def CmdEndProgram():
   DataWrite(PIC_CMD_END_PROGRAM, PIC_CMD_BIT_COUNT)



def CmdEndProgramming():
   DataWrite(PIC_CMD_END_PROGRAMMING, PIC_CMD_BIT_COUNT)



def CmdBeginEraseProgram():
   DataWrite(PIC_CMD_BEGIN_ERASE_PROG, PIC_CMD_BIT_COUNT)


def CmdBeginProgramOnly():
   DataWrite(PIC_CMD_BEGIN_PROG_ONLY, PIC_CMD_BIT_COUNT)


def CmdEraseChip():
   DataWrite(PIC_CMD_CHIP_ERASE, PIC_CMD_BIT_COUNT)


def CmdEraseProgMemory():
   DataWrite(PIC_CMD_ERASE_PROG_MEM, PIC_CMD_BIT_COUNT)



def CmdEraseDataMemory():
   DataWrite(PIC_CMD_ERASE_DATA_MEM, PIC_CMD_BIT_COUNT)



def CmdEraseSetup1():
   DataWrite(PIC_CMD_ERASE_SETUP1, PIC_CMD_BIT_COUNT)



def CmdEraseSetup2():
   DataWrite(PIC_CMD_ERASE_SETUP2, PIC_CMD_BIT_COUNT)



#/******************************/
#/* PIC18F LOW LEVEL FUNCTIONS */
#/******************************/
def DataRead_18F(BitCount):
   RPi.GPIO.output(GPIO_DATA_OUT_PIN, PIC_OUT_DATA_1)

   for Count in range(BitCount / 2):
      RPi.GPIO.output(GPIO_CLK_PIN, PIC_CLK_ON)
      time.sleep(SLEEP_CLOCK_READ_18F)
      RPi.GPIO.output(GPIO_CLK_PIN, PIC_CLK_OFF)
      time.sleep(SLEEP_CLOCK_READ_18F)

   PicDataWord = 0
   for Count in range(BitCount / 2):
      RPi.GPIO.output(GPIO_CLK_PIN, PIC_CLK_ON)
      time.sleep(SLEEP_CLOCK_READ_18F)

      if RPi.GPIO.input(GPIO_DATA_IN_PIN) == PIC_IN_DATA_1:
         PicDataWord = PicDataWord | int(math.pow(2, Count))

      RPi.GPIO.output(GPIO_CLK_PIN, PIC_CLK_OFF)
      time.sleep(SLEEP_CLOCK_READ_18F)

   return PicDataWord



def DataWrite_18F(PicDataWord, BitCount, ProgramFlag = False):
   for Count in range(BitCount):
      time.sleep(SLEEP_CLOCK_WRITE_18F)
      RPi.GPIO.output(GPIO_CLK_PIN, PIC_CLK_ON)

      Bit = (PicDataWord % 2)
      if Bit == 0:
         RPi.GPIO.output(GPIO_DATA_OUT_PIN, PIC_OUT_DATA_0)
      else:
         RPi.GPIO.output(GPIO_DATA_OUT_PIN, PIC_OUT_DATA_1)

      if ProgramFlag == True and Count == 3:
         time.sleep(PIC_DELAY_EEPROM_PROGRAM_18F)

      time.sleep(SLEEP_CLOCK_WRITE_18F)
      RPi.GPIO.output(GPIO_CLK_PIN, PIC_CLK_OFF)

      if ProgramFlag == True and Count == 3:
         time.sleep(PIC_DELAY_EEPROM_PROGRAM_18F)

      PicDataWord = PicDataWord / 2

   RPi.GPIO.output(GPIO_DATA_OUT_PIN, PIC_OUT_DATA_0)



def DataWriteCmd_18F(Command, PicDataWord, ProgramFlag = False):
   DataWrite_18F(Command, PIC18_CMD_BIT_COUNT, ProgramFlag)
   DataWrite_18F(PicDataWord, PIC18_DATA_BIT_COUNT)



def DataReadCmd_18F(Command):
   DataWrite_18F(Command, PIC18_CMD_BIT_COUNT)
   PicDataWord = DataRead_18F(PIC18_DATA_BIT_COUNT)

   return PicDataWord



def CmdSetAddress_18F(Address, ConfigFlag = False):
# BSF EECON1, EEPGD
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x8EA6)
   if ConfigFlag == True:
# BSF EECON1, CFGS
      DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x8CA6)
   else:
# BCF EECON1, CFGS
      DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x9CA6)
# MOVLW Addr[21:16]
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x0E00 | ((Address & 0x3F0000) >> 16))
# MOVWF TBLPTRU
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x6EF8)
# MOVLW <Addr[15:8]>
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x0E00 | ((Address & 0x00FF00) >> 8))
# MOVWF TBLPTRH
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x6EF7)
# MOVLW <Addr[7:0]>
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x0E00 | (Address & 0x0000FF))
# MOVWF TBLPTRL
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x6EF6)



def CmdSetDataAddress_18F(Address):
# BCF EECON1, EEPGD
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x9EA6)
# BCF EECON1, CFGS
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x9CA6)
# MOVLW <Addr>
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x0E00 | (Address & 0x00FF))
# MOVWF EEADR
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x6EA9)
# MOVLW <AddrH>
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x0E00 | ((Address & 0xFF00) >> 8))
# MOVWF EEADRH
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x6EAA)



def CmdLoadProg_18F(Address, PicDataWord, ConfigFlag = False):
   CmdSetAddress_18F(Address, ConfigFlag)
# Write 2 bytes and start programming.
# 1111 <MSB><LSB>
   DataWriteCmd_18F(PIC18_CMD_WRITE_PROG, PicDataWord)
# NOP - hold PGC high for time P9 and low for time P10.
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x0000, True)
   if ConfigFlag == True:
# MOVLW <Addr[7:0]>
      DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x0E00 | ((Address + 1) & 0x0000FF))
# MOVWF TBLPTRL
      DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x6EF6)
# Write 2 bytes and start programming.
# 1111 <MSB><LSB>
      DataWriteCmd_18F(PIC18_CMD_WRITE_PROG, PicDataWord)
# NOP - hold PGC high for time P9 and low for time P10.
      DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x0000, True)



def CmdReadProg_18F(Address, ConfigFlag = False):
   CmdSetAddress_18F(Address, ConfigFlag)
# TBLRD *+
   PicDataWord = DataReadCmd_18F(PIC18_CMD_READ_INC)

   return PicDataWord



def CmdLoadData_18F(Address, PicDataWord):
   CmdSetDataAddress_18F(Address)
# MOVLW <Data>
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x0E00 | PicDataWord)
# MOVWF EEDATA
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x6EA8)
# BSF EECON1, WREN
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x84A6)
# BSF EECON1, WR
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x82A6)

   TimeOut = 0
   PicDataWord = 0x02
   while (PicDataWord & 0x2 and TimeOut < EEWRITE_TIMEOUT):
      TimeOut = TimeOut + 1

# MOVF EECON1, W, 0
      DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x50A6)
# MOVWF TABLAT
      DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x6EF5)
# NOP
      DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x0000)
# Shift out data <MSB><LSB>
      PicDataWord = DataReadCmd_18F(PIC18_CMD_READ_TABLAT)

# BCF EECON1, WREN
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x94A6)



def CmdReadData_18F(Address):
   CmdSetDataAddress_18F(Address)
# BSF EECON1, RD
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x80A6)
# MOVF EEDATA, W, 0
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x50A8)
# MOVWF TABLAT
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x6EF5)
#  NOP
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x0000)
# Shift Out Data
   PicDataWord = DataReadCmd_18F(PIC18_CMD_READ_TABLAT)

   return PicDataWord



def CmdBulkErase_18F():
# Write 3F3Fh to 3C0005h
   CmdSetAddress_18F(0x3C0005)
   DataWriteCmd_18F(PIC18_CMD_WRITE, 0x3F3F)
# Write 8F8Fh TO 3C0004h to erase entire device.
   CmdSetAddress_18F(0x3C0004)
   DataWriteCmd_18F(PIC18_CMD_WRITE, 0x8F8F)
# NOP
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x0000, True)
# Hold PGD low until erase completes.
   DataWriteCmd_18F(PIC18_CMD_CORE_CMD, 0x0000, True)

