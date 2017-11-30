#!/usr/bin/python2

# RPiPIC - Python PIC Microcontroller Programmer
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
#/* RPiPIC                                                                   */
#/* ------------------------------------------------------------------------ */
#/* V1.00 - 2016-12-22 - Jason Birch                                         */
#/* ------------------------------------------------------------------------ */
#/* Python PIC Microcontroller Programmer.                                   */
#/****************************************************************************/


import sys
import time
import string
import RPi.GPIO
import PIC_API
import PIC_DEVICES
import HEX_File



#/****************************/
#/* Python script arguments. */
#/****************************/
ARG_COUNT = 3
ARG_EXE = 0
ARG_SWITCH = 1
ARG_DEVICE = 2
ARG_FILE_NAME = 3
ARG_MEM_AREA = 3
ARG_DATA = 4


#/***********************/
#/* Blank test results. */
#/***********************/
BLANK_FAIL = 0
BLANK_PASS = 1
BLANK_PROTECTED = 2


#/************************/
#/* Verify test results. */
#/************************/
LOCATION_PASS = 0xF0000001
LOCATION_FAIL = 0xF0000002



#/*******************************/
#/* APPLICATION LEVEL FUNCTIONS */
#/*******************************/
def ProgrammerPresent():
   PIC_API.ProgramModeStart()
   Result = PIC_API.ProgrammerPresent()
   PIC_API.ProgramModeEnd()

   return Result



def ProgramRead(Address, WordCount, ConfigData):
   PIC_API.ProgramModeStart()

   if ConfigData:
      PIC_API.ConfigMode()

   Count = 0
   for Count in range(Address):
      if Count % 0x0100 == 0:
         sys.stdout.write("Seek {:X}\r".format(Count))
         sys.stdout.flush()
      PIC_API.IncLocation()
   sys.stdout.write("Seek {:X}\n".format(Count))

   Data = []
   for Count in range(WordCount):
      PicDataWord = PIC_API.ReadProgLocation()
      Data.append(PicDataWord)
      PIC_API.IncLocation()

      sys.stdout.write("{:8X}".format(Address + Count) + " = " + "{:4X}".format(PicDataWord) + "\r")
      sys.stdout.flush()

   sys.stdout.write("{:20}".format(""))
   sys.stdout.write("\r")
   sys.stdout.flush()

   PIC_API.ProgramModeEnd()
   return Data



def DataRead(Address, WordCount):
   PIC_API.ProgramModeStart()

   for Count in range(Address):
      PIC_API.IncLocation()

   Data = []
   for Count in range(WordCount):
      PicDataWord = PIC_API.ReadDataLocation()
      Data.append(PicDataWord)
      PIC_API.IncLocation()

      sys.stdout.write("{:8X}".format(Address + Count) + " = " + "{:4X}".format(PicDataWord) + "\r")
      sys.stdout.flush()

   sys.stdout.write("{:20}".format(""))
   sys.stdout.write("\r")
   sys.stdout.flush()

   PIC_API.ProgramModeEnd()
   return Data



def ProgramWrite(WriteMemoryMap, PulseCount):
   MaxPeriod = 0
   AveragePeriod = 0
   
   print(">>>>> WRITING TO DEVICE\n")
   for FindCount in range(len(WriteMemoryMap)):
      time.sleep(0.1) # Allow device to settle before setting programming mode.

      if WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_WO) and len(WriteMemoryMap[FindCount]) > PIC_DEVICES.PICDEV_MEM_DATA and len(WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA]) != 0:
         PIC_API.ProgramModeStart()

         print(PIC_DEVICES.Lookup(WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_TYPE]))

         if     WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_CONF \
            and WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_WO):
            print(">>> CONFIG MODE <<<")
            PIC_API.ConfigMode()

         DataCount = 0
         for DataCount in range(WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_ADDR]):
            if DataCount % 0x0100 == 0:
               sys.stdout.write("SEEK {:8X}\r".format(DataCount))
               sys.stdout.flush()
            PIC_API.IncLocation()
         sys.stdout.write("SEEK {:8X}\n".format(DataCount))

         if WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_DATA:
            sys.stdout.write("DATA {:8X} : ".format(WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_ADDR]))
         else:
            sys.stdout.write("PROG {:8X} : ".format(WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_ADDR]))
         for DataCount in range(WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_SIZE]):
            if     WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_DATA \
               and WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA][DataCount] != PIC_API.PIC_BLANK_DATA_WORD:
               sys.stdout.write("{:4X} ".format(WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA][DataCount]))
               PicDataWord = WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA][DataCount]
               Period = PIC_API.ProgramDataLocation(PicDataWord, PulseCount)
               Verify = PIC_API.ReadDataLocation()
               if PicDataWord != Verify:
                  sys.stdout.write(" *{:4X} != {:4X}* ".format(PicDataWord, Verify))
            elif   WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_CONF | PIC_DEVICES.PICMEM_PROG) \
               and WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA][DataCount] != PIC_API.PIC_BLANK_PROG_WORD:
               sys.stdout.write("{:4X} ".format(WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA][DataCount]))
               PicDataWord = WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA][DataCount]
               Period = PIC_API.ProgramMemoryLocation(PicDataWord, PulseCount)
               Verify = PIC_API.ReadProgLocation()
               if PicDataWord != Verify:
                  sys.stdout.write(" *{:X} != {:X}* ".format(PicDataWord, Verify))
            sys.stdout.flush()   
            PIC_API.IncLocation()
         print("\n")

         PIC_API.ProgramModeEnd()

# Flash memory programming pulses should be no longer than 100uS 
#   if AveragePeriod == 0:
#      AveragePeriod = Period
#   else:
#      AveragePeriod = (AveragePeriod + Period) / 2
#
#   if Period > MaxPeriod:
#      MaxPeriod = Period

   return [ AveragePeriod, MaxPeriod ]



def ProgramVerify(DataOffset, Data, HexFileData):
   for Count in range(len(HexFileData)):
      if     HexFileData[Count][HEX_File.ADDRESS] >= DataOffset \
         and HexFileData[Count][HEX_File.ADDRESS] <= DataOffset + len(Data) * 2:
         sys.stdout.write("{:8X} [{:4X}] -> {:8X} [{:4X}] ".format(DataOffset, len(Data), HexFileData[Count][HEX_File.ADDRESS], len(HexFileData[Count][HEX_File.DATA])))
         Offset = HexFileData[Count][HEX_File.ADDRESS] - DataOffset
         Offset = Offset / 2

         PassFlag = True
         DataCount = 0
         for SourceDataCount in range(0, len(HexFileData[Count][HEX_File.DATA]), 2):
            PicDataWord = HexFileData[Count][HEX_File.DATA][SourceDataCount + 1] + HexFileData[Count][HEX_File.DATA][SourceDataCount]
            if Offset + DataCount == DataOffset - 1:
               sys.stdout.write(".")
            if Offset + DataCount >= DataOffset:
               Data.append(0x00)
            if Data[Offset + DataCount] != string.atoi(PicDataWord, 16):
               sys.stdout.write("\n***** ERROR: {:8X} : {:4X} != {:4X} ***** ".format(Offset + DataCount, Data[Offset + DataCount], string.atoi(PicDataWord, 16)))
               PassFlag = False
            DataCount = DataCount + 1
         if PassFlag:
            print("PASS")
         else:
            print("***** FAIL *****")



def EraseAll():
   print("***** ERASING DEVICE DATA *****\n")

   PIC_API.ProgramModeStart()

   PIC_API.EraseProgramMemory()
   PIC_API.ConfigMode()
   PIC_API.EraseProgramMemory()
   PIC_API.EraseDataMemory()

   PIC_API.ProgramModeEnd()



def BlankCheck(BlankWordValue, Data):
   PIC_API.ProgramModeStart()

   ZeroCheck = True
   Result = BLANK_PASS
   for Count in range(len(Data)):
      if Data[Count] != 0:
         ZeroCheck = False
      if ZeroCheck == False and Data[Count] != BlankWordValue:
         Result = BLANK_FAIL
         break

   if ZeroCheck == True:
      Result = BLANK_PROTECTED

   PIC_API.ProgramModeEnd()
   return Result



def DisplayData(Offset, Data):
   sys.stdout.write("Data Size: " + str(len(Data)) + " Words")
   for Count in range(len(Data)):
      if Count % 13 == 0:
         sys.stdout.write("\n{:8X} :".format(Offset + Count))
         sys.stdout.flush()
      sys.stdout.write(" {:4X}".format(Data[Count]))

   sys.stdout.write("\n")
   sys.stdout.flush()



def GetDeviceData(MemoryMap, Count):
   ConfigDataFlag = False
   Data = []

   if     MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_EEPROM \
      and MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_CONF \
      and MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
      ConfigDataFlag = True

   if     MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_EEPROM \
      and MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_CONF | PIC_DEVICES.PICMEM_PROG) \
      and MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
      Data = ProgramRead(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR], MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE], ConfigDataFlag)
   elif   MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_EEPROM \
      and MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_DATA \
      and MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
      Data = DataRead(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR], MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE])

   return Data



def CreateMemoryMap(MemoryMap):
   BlankMemoryMap = []
   for Count in range(len(MemoryMap)):
      if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_WO):
         if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_DATA:
            BlankMemoryMap.append([MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE],
                                  MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR],
                                  MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE] * 2,
                                  MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_OBJ_ADDR],
                                  MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_STRE_MASK],
                                  [PIC_API.PIC_BLANK_DATA_WORD for Value in range(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE] * 2)]])
         else:
            BlankMemoryMap.append([MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE],
                                  MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR],
                                  MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE],
                                  MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_OBJ_ADDR],
                                  MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_STRE_MASK],
                                  [PIC_API.PIC_BLANK_PROG_WORD for Value in range(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE])]])

   return BlankMemoryMap



def MemoryAreaSetData(MemoryMap, MemoryArea, Data):
   for Count in range(len(MemoryMap)):
      if     MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_WO) \
         and PIC_DEVICES.LookupName(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]) == MemoryArea:

         print("WRITING: " + Data + " TO " + PIC_DEVICES.LookupName(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))
         WriteMemoryMap = [MemoryMap[Count]]
         WriteMemoryMap[0].append([])
         for Count in range(0, len(Data), 4):
            WriteMemoryMap[0][PIC_DEVICES.PICDEV_MEM_DATA].append(string.atoi(Data[Count:Count + 4], 16))

         Period = ProgramWrite(WriteMemoryMap, PIC_API.PIC_PROG_PULSE_COUNT)

# Flash memory programming pulses should be no longer than 100uS 
#                 print("AVERAGE PROGRAM PERIOD: " + str(Period[0]) + " - MAX PROGRAM PERIOD: " + str(Period[1]))



def StoreMemoryValues(MemoryMap):
   print(">>>>> STORE MEMORY LOCATIONS\n")
   for Count in range(len(MemoryMap)):
      if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_ST:
         print(PIC_DEVICES.Lookup(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))
         Data = GetDeviceData(MemoryMap, Count)
         MemoryMap[Count].append(Data)
         for WordCount in range(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE]):
            MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_DATA][WordCount] = MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_DATA][WordCount] & MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_STRE_MASK]
            print("{:4X}".format(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_DATA][WordCount]))

#  /********************************************************************/
# /* For read only data, find the equivelent write only restore data. */
#/********************************************************************/
         if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_RO:
            FindType = (MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & ~(PIC_DEVICES.PICMEM_RO | PIC_DEVICES.PICMEM_ST)) | (PIC_DEVICES.PICMEM_WO | PIC_DEVICES.PICMEM_RE)
            for FindWriteCount in range(len(MemoryMap)):
               if MemoryMap[FindWriteCount][PIC_DEVICES.PICDEV_MEM_TYPE] == FindType:
                  print(PIC_DEVICES.Lookup(MemoryMap[FindWriteCount][PIC_DEVICES.PICDEV_MEM_TYPE]))
                  MemoryMap[FindWriteCount].append(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_DATA])
                  break
         print("")
   
   return MemoryMap



def RestoreMemoryValues(MemoryMap):
   print("<<<<< RESTORE MEMORY LOCATIONS\n")
   Found = False
   for Count in range(len(MemoryMap)):
      if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_RE:
         Found = True
         print(PIC_DEVICES.Lookup(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))

#  /******************************************************************/
# /* For write only data, find the equivelent read only store data. */
#/******************************************************************/
         if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_WO:
            FindType = (MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & ~(PIC_DEVICES.PICMEM_WO | PIC_DEVICES.PICMEM_RE)) | (PIC_DEVICES.PICMEM_RO | PIC_DEVICES.PICMEM_ST)
            for FindWriteCount in range(len(MemoryMap)):
               if MemoryMap[FindWriteCount][PIC_DEVICES.PICDEV_MEM_TYPE] == FindType:
                  print(PIC_DEVICES.Lookup(MemoryMap[FindWriteCount][PIC_DEVICES.PICDEV_MEM_TYPE]))
                  Data = GetDeviceData(MemoryMap, FindWriteCount)
         else:
            Data = GetDeviceData(MemoryMap, Count)

         for WordCount in range(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE]):
            MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_DATA][WordCount] = (Data[WordCount] & ~(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_STRE_MASK])) | (MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_DATA][WordCount] & MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_STRE_MASK])
            print("{:4X}".format(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_DATA][WordCount]))
         print("")

   if Found:
      Period = ProgramWrite(MemoryMap, PIC_API.PIC_PROG_PULSE_COUNT)

# Flash memory programming pulses should be no longer than 100uS 
#                 print("AVERAGE PROGRAM PERIOD: " + str(Period[0]) + " - MAX PROGRAM PERIOD: " + str(Period[1]))



def MergeMemoryMap(WriteMemoryMap, HexFileData):
   print("MERGING MEMORY MAP")
   for Count in range(len(HexFileData)):
      sys.stdout.write("{:8X} -> ".format(HexFileData[Count][HEX_File.ADDRESS]))
      for FindCount in range(len(WriteMemoryMap)):
         if     HexFileData[Count][HEX_File.ADDRESS] >= WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_OBJ_ADDR] \
            and HexFileData[Count][HEX_File.ADDRESS] <= WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_OBJ_ADDR] + WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_SIZE] * 2:
            sys.stdout.write("{:8X} ".format(WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_ADDR]))
            Offset = HexFileData[Count][HEX_File.ADDRESS] - WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_OBJ_ADDR]
            Offset = Offset / 2
            sys.stdout.write(" + {:8X} : ".format(Offset))

            DataCount = 0
            for SourceDataCount in range(0, len(HexFileData[Count][HEX_File.DATA]), 2):
               PicDataWord = HexFileData[Count][HEX_File.DATA][SourceDataCount + 1] + HexFileData[Count][HEX_File.DATA][SourceDataCount]
               sys.stdout.write(PicDataWord)
               if Offset + DataCount == WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_SIZE] - 1:
                  sys.stdout.write(".")
               if Offset + DataCount >= WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_SIZE]:
                  WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA].append(0x00)
               WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA][Offset + DataCount] = string.atoi(PicDataWord, 16)

               DataCount = DataCount + 1
      print("")
   print("")



def HexDataFromMemoryMap(MemoryMap, Data):
   if MemoryMap[PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_DATA:
      BlankWord = PIC_API.PIC_BLANK_DATA_WORD
   else:
      BlankWord = PIC_API.PIC_BLANK_PROG_WORD
   
   StartFlag = True
   Address = MemoryMap[PIC_DEVICES.PICDEV_MEM_OBJ_ADDR]
   HexData = []
   for Count in range(len(Data)):
      if Data[Count] != BlankWord:
         if StartFlag == True:
            StartFlag = False
            HexData.append([Address, ["{:02X}".format(Data[Count] & 0xFF)]])
            HexData[len(HexData) - 1][1].append("{:02X}".format(Data[Count] / 256))
         else:
            HexData[len(HexData) - 1][1].append("{:02X}".format(Data[Count] & 0xFF))
            HexData[len(HexData) - 1][1].append("{:02X}".format(Data[Count] / 256))
      else:
         StartFlag = True
      Address = Address + 2

   return HexData



def ChecksumData(Data):
   Checksum = 0
   for Count in range(len(Data)):
      Checksum = (Checksum + Data[Count]) & 0xFFFF
   return Checksum



#  /*********************************************/
# /* List the currently supported PIC devices. */
#/*********************************************/
print("")
if "-L" in sys.argv:
   sys.stdout.write("\nCurrently supported PIC devices:\n")
   for Count in range(len(PIC_DEVICES.PIC_DEVICE)):
      if Count % 8 == 0:
         sys.stdout.write("\n")
         sys.stdout.flush()
      sys.stdout.write(PIC_DEVICES.PIC_DEVICE[Count][PIC_DEVICES.PICDEV_NAME] + "   ")
   sys.stdout.write("\n\n")
   sys.stdout.flush()
elif "-P" in sys.argv:
   PIC_API.PowerOnDevice()
elif "-O" in sys.argv:
   PIC_API.PowerOffDevice()
#  /**************************************************************************/
# /* Check the minimum number of command line arguments have been provided. */
#/**************************************************************************/
elif len(sys.argv) < ARG_COUNT:
   print(sys.argv[ARG_EXE] + " -P")
   print("Power on current device.\n")
   print(sys.argv[ARG_EXE] + " -O")
   print("Power off current device.\n")
   print(sys.argv[ARG_EXE] + " -L")
   print("List currently supported PIC devices.\n")
   print(sys.argv[ARG_EXE] + " -C [PIC_DEVICE]")
   print("Display device memory checksum.\n")
   print(sys.argv[ARG_EXE] + " -D [PIC_DEVICE]")
   print("Read memory from device and display.\n")
   print(sys.argv[ARG_EXE] + " -B [PIC_DEVICE]")
   print("Blank check device.\n")
   print(sys.argv[ARG_EXE] + " -E [PIC_DEVICE]")
   print("Erase all device memory.\n")
   print(sys.argv[ARG_EXE] + " -R [PIC_DEVICE] [FILE_NAME]")
   print("Read memory from device and save to .hex file.\n")
   print(sys.argv[ARG_EXE] + " -W [PIC_DEVICE] [FILE_NAME]")
   print("Read .hex file and write to device memory.\n")
   print(sys.argv[ARG_EXE] + " -V [PIC_DEVICE] [FILE_NAME]")
   print("Read memory from device and read .hex file, then verify data.\n")
   print(sys.argv[ARG_EXE] + " -LM [PIC_DEVICE]")
   print("List device memory areas.\n")
   print(sys.argv[ARG_EXE] + " -LD [PIC_DEVICE] [MEMORY_AREA] [DATA]")
   print("Load data into a device memory area.\n")
else:
#  /***********************************************/
# /* Initialise required Raspberry Pi GPIO pins. */
#/***********************************************/
   PIC_API.InitGPIO()

#  /*********************************************/
# /* Check if RPiPIC programmer is plugged in. */
#/*********************************************/
   if ProgrammerPresent() == False:
      print("RPiPIC Programmer Not Present.\n")
   else:
#  /********************************************************/
# /* Find memory map definition for the specified device. */
#/********************************************************/
      MemoryMap = []
      for Count in range(len(PIC_DEVICES.PIC_DEVICE)):
         if sys.argv[ARG_DEVICE] == PIC_DEVICES.PIC_DEVICE[Count][PIC_DEVICES.PICDEV_NAME]:
            MemoryMap = PIC_DEVICES.PIC_DEVICE[Count][PIC_DEVICES.PICDEV_MEM]

#  /****************************************************/
# /* Check if a memory map definition has been found. */
#/****************************************************/
      if len(MemoryMap) == 0:
         print("Device " + sys.argv[ARG_DEVICE] + " Not Found.\n")
      else:
#  /***********************************/
# /* Display device memory checksum. */
#/***********************************/
         if "-C" in sys.argv:
            print("Device " + sys.argv[ARG_DEVICE] + "\n")
            Checksum = 0
            for Count in range(len(MemoryMap)):
               if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
                  print(PIC_DEVICES.Lookup(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))
                  Data = GetDeviceData(MemoryMap, Count)
                  if len(Data) == 0:
                     print("UNKNOWN MEMORY TYPE\n")
                  else:
                     Checksum = Checksum + ChecksumData(Data) & 0xFFFF
            print("\nCHECKSUM: {:04X}\n".format(Checksum))
#  /**********************************/
# /* Display device memory content. */
#/**********************************/
         elif "-D" in sys.argv:
            print("Device " + sys.argv[ARG_DEVICE] + "\n")
            for Count in range(len(MemoryMap)):
               if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
                  print(PIC_DEVICES.Lookup(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))
                  Data = GetDeviceData(MemoryMap, Count)
                  if len(Data) == 0:
                     print("UNKNOWN MEMORY TYPE\n")
                  else:
                     DisplayData(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR], Data)
                     print("")
#  /***************************************/
# /* Read device memory content to file. */
#/***************************************/
         elif "-R" in sys.argv and len(sys.argv) > ARG_COUNT:
            print("Device " + sys.argv[ARG_DEVICE] + "\n")
            print("READ DEVICE DATA\n")
            HexData = []
            for Count in range(len(MemoryMap)):
               if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
                  print(PIC_DEVICES.Lookup(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))
                  Data = GetDeviceData(MemoryMap, Count)
                  if len(Data) == 0:
                     print("UNKNOWN MEMORY TYPE\n")
                  else:
                     HexData.append(HexDataFromMemoryMap(MemoryMap[Count], Data))
                  print("")

            print("SAVE HEX FILE: " + sys.argv[ARG_FILE_NAME] + "\n")
            HEX_File.SaveHexFile(sys.argv[ARG_FILE_NAME], HexData)
#  /******************************************/
# /* Write device memory content from file. */
#/******************************************/
         elif "-W" in sys.argv and len(sys.argv) > ARG_COUNT:
            print("Device " + sys.argv[ARG_DEVICE] + "\n")
            WriteMemoryMap = CreateMemoryMap(MemoryMap)
            HexFileData = HEX_File.ReadHexFile(sys.argv[ARG_FILE_NAME])
            MergeMemoryMap(WriteMemoryMap, HexFileData)
            Period = ProgramWrite(WriteMemoryMap, PIC_API.PIC_PROG_PULSE_COUNT)

# Flash memory programming pulses should be no longer than 100uS 
#            print("AVERAGE PROGRAM PERIOD: " + str(Period[0]) + " - MAX PROGRAM PERIOD: " + str(Period[1]))
#  /*******************************************/
# /* Verify device memory content from file. */
#/*******************************************/
         elif "-V" in sys.argv and len(sys.argv) > ARG_COUNT:
            print("Device " + sys.argv[ARG_DEVICE] + "\n")
            HexFileData = HEX_File.ReadHexFile(sys.argv[ARG_FILE_NAME])
            for Count in range(len(MemoryMap)):
               if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
                  print(PIC_DEVICES.Lookup(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))
                  Data = GetDeviceData(MemoryMap, Count)
                  if len(Data) == 0:
                     print("UNKNOWN MEMORY TYPE\n")
                  else:
                     ProgramVerify(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_OBJ_ADDR], Data, HexFileData)
                     print("")
#  /********************************/
# /* Erase device memory content. */
#/********************************/
         elif "-E" in sys.argv:
            print("Device " + sys.argv[ARG_DEVICE] + "\n")
            MemoryMapStore = StoreMemoryValues(MemoryMap)
            MemoryAreaSetData(MemoryMap, "CONFIG:CONF", "0000")
            EraseAll()
            RestoreMemoryValues(MemoryMapStore)
            print("ALL DEVICE DATA ERASED\n")
#  /***********************/
# /* Blank check device. */
#/***********************/
         elif "-B" in sys.argv:
            print("Device " + sys.argv[ARG_DEVICE] + "\n")
            for Count in range(len(MemoryMap)):
               if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
                  print(PIC_DEVICES.Lookup(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))
                  Data = GetDeviceData(MemoryMap, Count)
                  
                  Result = False
                  if len(Data) == 0:
                     print("UNKNOWN MEMORY TYPE\n")
                     continue
                  elif MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_DATA:
                     Result = BlankCheck(PIC_API.PIC_BLANK_DATA_WORD, Data)
                  else:
                     Result = BlankCheck(PIC_API.PIC_BLANK_PROG_WORD, Data)

                  if Result == BLANK_PASS:
                     print("{:8X} -> {:8X} : BLANK".format(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR], (MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR] + MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE])))
                  elif Result == BLANK_FAIL:
                     print("{:8X} -> {:8X} : !NOT BLANK!".format(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR], (MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR] + MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE])))
                  elif Result == BLANK_PROTECTED:
                     print("{:8X} -> {:8X} : !PROTECTED!".format(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR], (MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR] + MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE])))

                  print("")
#  /*****************************/
# /* List device memory areas. */
#/*****************************/
         elif "-LM" in sys.argv:
            print("Device " + sys.argv[ARG_DEVICE] + "\n")
            for Count in range(len(MemoryMap)):
               if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
                  print(PIC_DEVICES.LookupName(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))
            print("")
#  /*****************************/
# /* List device memory areas. */
#/*****************************/
         elif "-LD" in sys.argv and len(sys.argv) > ARG_COUNT + 1:
            print("Device " + sys.argv[ARG_DEVICE] + "\n")
            MemoryAreaSetData(MemoryMap, sys.argv[ARG_MEM_AREA], sys.argv[ARG_DATA])
#  /******************************/
# /* Valid arguments not found. */
#/******************************/
         else:
            print("INVALID ARGUMENTS PROVIDED\n")

#  /*************************************************/
# /* Close Raspberry Pi GPIO use before finishing. */
#/*************************************************/
   RPi.GPIO.cleanup()

