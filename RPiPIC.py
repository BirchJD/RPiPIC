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
#/* V1.01 - 2017-12-30 - Added support for PIC18F device programming.        */
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
ARG_NO_STORE = 3
ARG_DATA = 4


#/***********************/
#/* Blank test results. */
#/***********************/
BLANK_FAIL      = 1000.0
BLANK_PASS      = 2000.0
BLANK_PROTECTED = 3000.0


#/************************/
#/* Verify test results. */
#/************************/
PROGRAM_WRITE_MAX_FAILS = 5



#/*******************************/
#/* APPLICATION LEVEL FUNCTIONS */
#/*******************************/
def ProgrammerPresent(PicDevice):
   PIC_API.ProgramModeStart(PicDevice)
   Result = PIC_API.ProgrammerPresent()
   PIC_API.ProgramModeEnd()

   return Result



def ProgramRead(PicDevice, Address, WordCount, ConfigData):
   PIC_API.ProgramModeStart(PicDevice)

   if ConfigData:
      PIC_API.ConfigMode(PicDevice, PIC_API.PIC_BLANK_CONFIG_WORD)

   PIC_API.Seek(PicDevice, Address, PIC_API.SEEK_SET)

   Data = []
   for Count in range(WordCount):
      PicDataWord = PIC_API.ReadProgLocation(PicDevice, Address + Count, 1)
      Data.append(PicDataWord)

      if Count % 100 == 0:
         sys.stdout.write("{:08X}".format(Address + Count) + " = " + "{:4X}".format(PicDataWord) + "\r")
         sys.stdout.flush()

   sys.stdout.write("{:20}".format(""))
   sys.stdout.write("\r")
   sys.stdout.flush()

   PIC_API.ProgramModeEnd()
   return Data



def DataRead(PicDevice, Address, WordCount):
   PIC_API.ProgramModeStart(PicDevice)

   PIC_API.Seek(PicDevice, Address, PIC_API.SEEK_SET)

   Data = []
   for Count in range(WordCount):
      PicDataWord = PIC_API.ReadDataLocation(PicDevice, Address + Count)
      Data.append(PicDataWord)

      if Count % 100 == 0:
         sys.stdout.write("{:08X}".format(Address + Count) + " = " + "{:4X}".format(PicDataWord) + "\r")
         sys.stdout.flush()

   sys.stdout.write("{:20}".format(""))
   sys.stdout.write("\r")
   sys.stdout.flush()

   PIC_API.ProgramModeEnd()
   return Data



def ProgramWrite(PicDevice, WriteMemoryMap, PulseCount):
   FailCount = 0
   Result = True

   print(">>>>> WRITING TO DEVICE\n")
   for FindCount in range(len(WriteMemoryMap)):
      if FailCount > PROGRAM_WRITE_MAX_FAILS:
         break

      time.sleep(0.1) # Allow device to settle before setting programming mode.

      if WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_WO) and len(WriteMemoryMap[FindCount]) > PIC_DEVICES.PICDEV_MEM_DATA and len(WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA]) != 0:
         PIC_API.ProgramModeStart(PicDevice)

         print(PIC_DEVICES.Lookup(WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_TYPE]))

         ConfigMode = False
         if     WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_CONF \
            and WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_WO) \
            and PicDevice not in ["16F18313", "16F18323", "16F18324", "16F18344", "16F18325", "16F18345", "16F18326", "16F18346"]:
            print(">>> CONFIG MODE <<<")
            ConfigMode = True
            PIC_API.ConfigMode(PicDevice, PIC_API.PIC_BLANK_CONFIG_WORD)

         Address = WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_ADDR]
         PIC_API.Seek(PicDevice, Address, PIC_API.SEEK_SET)
         StepCount = 1
         if WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_DATA:
            sys.stdout.write("DATA {:08X} : ".format(Address))
         else:
            sys.stdout.write("PROG {:08X} : ".format(Address))
            if PicDevice[:3] in ["18F"]:
               StepCount = 2

         SeekOffset = 0
         for DataCount in range(0, WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_SIZE], StepCount):
            if FailCount > PROGRAM_WRITE_MAX_FAILS:
               break
            if     WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_DATA \
               and WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA][DataCount] != DeviceBlankDataWord \
               and DataCount < len(WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA]):
               if SeekOffset > 0:
                  PIC_API.Seek(PicDevice, SeekOffset, PIC_API.SEEK_OFFSET)
                  SeekOffset = 0
               sys.stdout.write("{:4X} ".format(WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA][DataCount]))
               PicDataWord = WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA][DataCount]
               PIC_API.ProgramDataLocation(PicDevice, Address + DataCount, PicDataWord, PulseCount)
               Verify = PIC_API.ReadDataLocation(PicDevice, Address + DataCount)
               if PicDataWord != Verify:
                  FailCount += 1
                  sys.stdout.write(" *{:4X} != {:4X}* ".format(PicDataWord, Verify))
            elif   WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_CONF | PIC_DEVICES.PICMEM_PROG) \
               and   ((WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA][DataCount] != DeviceBlankProgWord) \
                   or (DataCount + 1 < len(WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA]) \
                       and WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA][DataCount + 1] != DeviceBlankProgWord)) \
               and DataCount < len(WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA]):
               if SeekOffset > 0:
                  PIC_API.Seek(PicDevice, SeekOffset, PIC_API.SEEK_OFFSET)
                  SeekOffset = 0
               PicDataWord = WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA][DataCount]
               if StepCount == 2:
                  PicDataWord = PicDataWord | (WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA][DataCount + 1] << 8)
               sys.stdout.write("{:4X} ".format(PicDataWord))
               if     WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_CONF \
                  and (PicDevice[:3] in ["18F"]
                       or PicDevice in ["16F18313", "16F18323", "16F18324", "16F18344", "16F18325", "16F18345", "16F18326", "16F18346"]):
                  PIC_API.ProgramConfigLocation(PicDevice, Address + DataCount, PicDataWord, PulseCount)
                  Verify = PIC_API.ReadConfigLocation(PicDevice, Address + DataCount, StepCount)
               else:
                  PIC_API.ProgramMemoryLocation(PicDevice, Address + DataCount, PicDataWord, PulseCount, ConfigMode and WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_CONFIG)
                  Verify = PIC_API.ReadProgLocation(PicDevice, Address + DataCount, StepCount)
               if PicDataWord != Verify:
                  FailCount += 1
                  sys.stdout.write("\n****** {:08X} : {:4X} != {:4X} [{:}] ******\n".format(Address + DataCount, PicDataWord, Verify, FailCount))
            else:
               SeekOffset = SeekOffset + 1
            sys.stdout.flush()
         print("\n")

         PIC_API.ProgramModeEnd()
         
   if FailCount > 0:
      print("***** PROGRAM FAILED [{:}] *****\n".format(FailCount))
      Result = False

   return Result



def ProgramVerify(PicDevice, DataOffset, Data, HexFileData):
   if PicDevice[:3] in ["12F", "16F"]:
      StepCount = 2
   elif PicDevice[:3] in ["18F"]:
      StepCount = 1

   for Count in range(len(HexFileData)):
      if     HexFileData[Count][HEX_File.ADDRESS] >= DataOffset \
         and HexFileData[Count][HEX_File.ADDRESS] <= DataOffset + len(Data) * StepCount:
         sys.stdout.write("HEX FILE: {:08X} [{:4X}] -> DEVICE: {:08X} [{:4X}] ".format(DataOffset, len(Data), HexFileData[Count][HEX_File.ADDRESS], len(HexFileData[Count][HEX_File.DATA])))
         Offset = HexFileData[Count][HEX_File.ADDRESS] - DataOffset
         Offset = Offset / StepCount

         FailCount = 0
         DataCount = 0
         for SourceDataCount in range(0, len(HexFileData[Count][HEX_File.DATA]), StepCount):
            PicDataWord = HexFileData[Count][HEX_File.DATA][SourceDataCount]
            if StepCount == 2:
               PicDataWord = HexFileData[Count][HEX_File.DATA][SourceDataCount + 1] + PicDataWord
            if Offset + DataCount == len(Data) - 1:
               sys.stdout.write(".")
            if Offset + DataCount >= len(Data):
               Data.append(0x00)
            if Data[Offset + DataCount] != string.atoi(PicDataWord, 16):
               sys.stdout.write("\n***** {:08X} : {:4X} != {:4X} *****".format(Offset + DataCount, Data[Offset + DataCount], string.atoi(PicDataWord, 16)))
               FailCount = FailCount + 1
            DataCount = DataCount + 1
         if FailCount > 0:
            print("\n***** FAIL ***** [{:}]".format(FailCount))
         else:
            print("===== PASS =====")



def EraseAll(PicDevice):
   print("***** ERASING DEVICE DATA *****\n")
   PIC_API.ProgramModeStart(PicDevice)
   PIC_API.EraseAllMemory(PicDevice)
   PIC_API.ProgramModeEnd()



def BlankCheck(PicDevice, BlankWordValue, Data):
   PIC_API.ProgramModeStart(PicDevice)

   ZeroCheck = True
   FailCount = 0.0
   Result = BLANK_PASS
   for Count in range(len(Data)):
      if Data[Count] != 0:
         ZeroCheck = False
      if Data[Count] != BlankWordValue:
         FailCount = FailCount + 1

   if ZeroCheck == True:
      Result = BLANK_PROTECTED
   elif FailCount > 0:
      Result = BLANK_FAIL + (100 * FailCount / len(Data))

   PIC_API.ProgramModeEnd()
   return Result



def DisplayData(Offset, Data):
   sys.stdout.write("Data Size: " + str(len(Data)) + " Words")
   for Count in range(len(Data)):
      if Count % 13 == 0:
         sys.stdout.write("\n{:08X} :".format(Offset + Count))
         sys.stdout.flush()
      sys.stdout.write(" {:4X}".format(Data[Count]))

   sys.stdout.write("\n")
   sys.stdout.flush()



def GetDeviceData(PicDevice, MemoryMap, Count):
   ConfigDataFlag = False
   Data = []

   if     MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_EEPROM \
      and MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_CONF \
      and MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
      ConfigDataFlag = True

   if     MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_EEPROM \
      and MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_CONF | PIC_DEVICES.PICMEM_PROG) \
      and MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
      Data = ProgramRead(PicDevice, MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR], MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE], ConfigDataFlag)
   elif   MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_EEPROM \
      and MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_DATA \
      and MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
      Data = DataRead(PicDevice, MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR], MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE])

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
                                  [DeviceBlankDataWord for Value in range(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE] * 2)]])
         else:
            BlankMemoryMap.append([MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE],
                                  MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR],
                                  MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE],
                                  MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_OBJ_ADDR],
                                  MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_STRE_MASK],
                                  [DeviceBlankProgWord for Value in range(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE])]])

   return BlankMemoryMap



def MemoryAreaSetData(PicDevice, MemoryMap, MemoryArea, Data):
   for Count in range(len(MemoryMap)):
      if     MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_WO) \
         and PIC_DEVICES.LookupName(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]) == MemoryArea:

         print("WRITING: " + Data + " TO " + PIC_DEVICES.LookupName(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))
         WriteMemoryMap = [MemoryMap[Count]]
         WriteMemoryMap[0].append([])
         for Count in range(0, len(Data), 4):
            WriteMemoryMap[0][PIC_DEVICES.PICDEV_MEM_DATA].append(string.atoi(Data[Count:Count + 4], 16))

         ProgramWrite(PicDevice, WriteMemoryMap, PIC_API.PIC_PROG_PULSE_COUNT)



def StoreMemoryValues(PicDevice, MemoryMap):
   print(">>>>> STORE MEMORY LOCATIONS\n")
   for Count in range(len(MemoryMap)):
      if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_ST:
         print(PIC_DEVICES.Lookup(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))
         Data = GetDeviceData(PicDevice, MemoryMap, Count)
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



def RestoreMemoryValues(PicDevice, MemoryMap):
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
                  Data = GetDeviceData(PicDevice, MemoryMap, FindWriteCount)
         else:
            Data = GetDeviceData(PicDevice, MemoryMap, Count)

         for WordCount in range(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE]):
            MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_DATA][WordCount] = (Data[WordCount] & ~(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_STRE_MASK])) | (MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_DATA][WordCount] & MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_STRE_MASK])
            print("{:4X}".format(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_DATA][WordCount]))
         print("")

   if Found:
      ProgramWrite(PicDevice, MemoryMap, PIC_API.PIC_PROG_PULSE_COUNT)



def MergeMemoryMap(PicDevice, WriteMemoryMap, HexFileData):
   print("MERGING MEMORY MAP")
   if PicDevice[:3] in ["12F", "16F"]:
      StepCount = 2
   elif PicDevice[:3] in ["18F"]:
      StepCount = 1
   for Count in range(len(HexFileData)):
      sys.stdout.write("{:08X} -> ".format(HexFileData[Count][HEX_File.ADDRESS]))
      for FindCount in range(len(WriteMemoryMap)):
         if     HexFileData[Count][HEX_File.ADDRESS] >= WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_OBJ_ADDR] \
            and HexFileData[Count][HEX_File.ADDRESS] + len(HexFileData[Count][HEX_File.DATA]) <= WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_OBJ_ADDR] + WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_SIZE] * StepCount:
            sys.stdout.write("{:08X}".format(WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_ADDR]))
            Offset = HexFileData[Count][HEX_File.ADDRESS] - WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_OBJ_ADDR]
            Offset = Offset / StepCount
            sys.stdout.write(" + {:08X} : ".format(Offset))

            DataCount = 0
            for SourceDataCount in range(0, len(HexFileData[Count][HEX_File.DATA]), StepCount):
               PicDataWord = HexFileData[Count][HEX_File.DATA][SourceDataCount]
               if StepCount == 2:
                  PicDataWord = HexFileData[Count][HEX_File.DATA][SourceDataCount + 1] + PicDataWord 
               sys.stdout.write(PicDataWord)
               if Offset + DataCount == WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_SIZE] - 1:
                  sys.stdout.write(".")
               if Offset + DataCount >= WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_SIZE]:
                  WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA].append(0x00)
               WriteMemoryMap[FindCount][PIC_DEVICES.PICDEV_MEM_DATA][Offset + DataCount] = string.atoi(PicDataWord, 16)

               DataCount = DataCount + 1
            sys.stdout.write("{:12}".format(""))
      print("")
   print("")



def HexDataFromMemoryMap(MemoryMap, Data):
   if MemoryMap[PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_DATA:
      BlankWord = DeviceBlankDataWord
   else:
      BlankWord = DeviceBlankProgWord
   
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
      if Count % 5 == 0:
         sys.stdout.write("\n")
         sys.stdout.flush()
      sys.stdout.write("{:16}".format(PIC_DEVICES.PIC_DEVICE[Count][PIC_DEVICES.PICDEV_NAME]))
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
   print("V1.01 - 2017-12-30 - (C) Jason Birch")
   print("")
   print("TODO: Implement configuration mask.")
   print("TODO: Implement HEX dump for extended addresses.")
   print("TODO: Complete device ID look-up.")
   print("TODO: Add additional devices and example test code.")
   print("")
   print(sys.argv[ARG_EXE] + " -P")
   print("Power on current device.\n")
   print(sys.argv[ARG_EXE] + " -O")
   print("Power off current device.\n")
   print(sys.argv[ARG_EXE] + " -L")
   print("List currently supported PIC devices.\n")
   print(sys.argv[ARG_EXE] + " -C [PIC_DEVICE]")
   print("Display device memory checksum.\n")
   print(sys.argv[ARG_EXE] + " -D [PIC_DEVICE] <MEMORY_AREA>")
   print("Read memory from device and display.\n")
   print(sys.argv[ARG_EXE] + " -B [PIC_DEVICE]")
   print("Blank check device.\n")
   print(sys.argv[ARG_EXE] + " -E [PIC_DEVICE] <NO_STORE>")
   print("Erase all device memory.")
   print("If 'NO_STORE' is specified non data and program memory is not retained.\n")
   print(sys.argv[ARG_EXE] + " -EC [PIC_DEVICE]")
   print("Erase all device config.\n")
   print(sys.argv[ARG_EXE] + " -R [PIC_DEVICE] [FILE_NAME]")
   print("Read memory from device and save to .hex file.\n")
   print(sys.argv[ARG_EXE] + " -W [PIC_DEVICE] [FILE_NAME]")
   print("Read .hex file and write to device memory.\n")
   print(sys.argv[ARG_EXE] + " -V [PIC_DEVICE] [FILE_NAME]")
   print("Read memory from device and read .hex file, then verify data.\n")
   print(sys.argv[ARG_EXE] + " -LM [PIC_DEVICE]")
   print("List device memory areas.\n")
   print(sys.argv[ARG_EXE] + " -LD [PIC_DEVICE] [MEMORY_AREA] [DATA]")
   print("Load data into a device memory area.")
   print("EXAMPLES:")
   print("./RPiPIC.py -LD 16F684 CONFIG:BOR_CAL 23F8")
   print("./RPiPIC.py -LD 16F684 CONFIG:CAL 3FFF")
   print("./RPiPIC.py -LD 16F684 CONFIG:ID 0005000100020001")
   print("\n")
else:
#  /***********************************************/
# /* Initialise required Raspberry Pi GPIO pins. */
#/***********************************************/
   PIC_API.InitGPIO()

#  /*********************************************/
# /* Check if RPiPIC programmer is plugged in. */
#/*********************************************/
   ThisPicDevice = sys.argv[ARG_DEVICE]
   if ProgrammerPresent(ThisPicDevice) == False:
      print("RPiPIC Programmer Not Present.\n")
   else:
#  /********************************************************/
# /* Find memory map definition for the specified device. */
#/********************************************************/
      MemoryMap = []
      for Count in range(len(PIC_DEVICES.PIC_DEVICE)):
         if ThisPicDevice == PIC_DEVICES.PIC_DEVICE[Count][PIC_DEVICES.PICDEV_NAME]:
            MemoryMap = PIC_DEVICES.PIC_DEVICE[Count][PIC_DEVICES.PICDEV_MEM]

#  /****************************************************/
# /* Check if a memory map definition has been found. */
#/****************************************************/
      if len(MemoryMap) == 0:
         print("SPECIFIED DEVICE: " + ThisPicDevice + " NOT CURRENTLY SUPPORTED.\n")
      else:
         print("SPECIFIED DEVICE: " + ThisPicDevice + "\n")
         if ThisPicDevice[:3] in ["12F", "16F"]:
            DeviceBlankProgWord = PIC_API.PIC_BLANK_PROG_WORD
            DeviceBlankDataWord = PIC_API.PIC_BLANK_DATA_WORD
         elif ThisPicDevice[:3] in ["18F"]:
            DeviceBlankProgWord = PIC_API.PIC_BLANK_PROG_WORD_18F
            DeviceBlankDataWord = PIC_API.PIC_BLANK_DATA_WORD_18F

#  /***********************************/
# /* Display device memory checksum. */
#/***********************************/
         if "-C" in sys.argv:
            Checksum = 0
            for Count in range(len(MemoryMap)):
               if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
                  print(PIC_DEVICES.Lookup(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))
                  Data = GetDeviceData(ThisPicDevice, MemoryMap, Count)
                  if len(Data) == 0 or Data[0] == PIC_API.PIC_UNKNOWN_WORD:
                     print("UNKNOWN MEMORY TYPE\n")
                  else:
                     Checksum = Checksum + ChecksumData(Data)
            print("\nCHECKSUM: {:04X}\n".format((Checksum & 0xFFFF)))
#  /**********************************/
# /* Display device memory content. */
#/**********************************/
         elif "-D" in sys.argv:
            for Count in range(len(MemoryMap)):
               if    len(sys.argv) == ARG_COUNT and MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO) \
                  or len(sys.argv) > ARG_COUNT and PIC_DEVICES.LookupName(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]) == sys.argv[ARG_MEM_AREA] and MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
                  print(PIC_DEVICES.Lookup(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))
                  Data = GetDeviceData(ThisPicDevice, MemoryMap, Count)
                  if len(Data) == 0 or Data[0] == PIC_API.PIC_UNKNOWN_WORD:
                     print("UNKNOWN MEMORY TYPE\n")
                  else:
                     DisplayData(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR], Data)
                     print("")
#  /***************************************/
# /* Read device memory content to file. */
#/***************************************/
         elif "-R" in sys.argv and len(sys.argv) > ARG_COUNT:
            print("READ DEVICE DATA\n")
            HexData = []
            for Count in range(len(MemoryMap)):
               if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_WO):
                  print(PIC_DEVICES.Lookup(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))
                  Data = GetDeviceData(ThisPicDevice, MemoryMap, Count)
                  if len(Data) == 0 or Data[0] == PIC_API.PIC_UNKNOWN_WORD:
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
            WriteMemoryMap = CreateMemoryMap(MemoryMap)
            HexFileData = HEX_File.ReadHexFile(sys.argv[ARG_FILE_NAME])
            MergeMemoryMap(ThisPicDevice, WriteMemoryMap, HexFileData)
            ProgramWrite(ThisPicDevice, WriteMemoryMap, PIC_API.PIC_PROG_PULSE_COUNT)
#  /*******************************************/
# /* Verify device memory content from file. */
#/*******************************************/
         elif "-V" in sys.argv and len(sys.argv) > ARG_COUNT:
            HexFileData = HEX_File.ReadHexFile(sys.argv[ARG_FILE_NAME])
            for Count in range(len(MemoryMap)):
               if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
                  print(PIC_DEVICES.Lookup(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))
                  Data = GetDeviceData(ThisPicDevice, MemoryMap, Count)
                  if len(Data) == 0 or Data[0] == PIC_API.PIC_UNKNOWN_WORD:
                     print("UNKNOWN MEMORY TYPE\n")
                  else:
                     ProgramVerify(ThisPicDevice, MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_OBJ_ADDR], Data, HexFileData)
                     print("")
#  /********************************/
# /* Erase device memory content. */
#/********************************/
         elif "-E" in sys.argv:
            if ThisPicDevice[:3] in ["12F", "16F"]:
               if len(sys.argv) == ARG_COUNT or (len(sys.argv) > ARG_COUNT and sys.argv[ARG_NO_STORE] != "NO_STORE"):
                  MemoryMapStore = StoreMemoryValues(ThisPicDevice, MemoryMap)
                  MemoryAreaSetData(ThisPicDevice, MemoryMap, "CONFIG:CONF", "0000")
            EraseAll(ThisPicDevice)
            if ThisPicDevice[:3] in ["12F", "16F"]:
#               print("Allow device to complete erase process...")
#               PIC_API.PowerOnDevice()
#               for Count in range(5):
#                  sys.stdout.write("{:1}  \r".format(5 - Count))
#                  sys.stdout.flush()
#                  time.sleep(1)
#               PIC_API.PowerOffDevice()
               if len(sys.argv) == ARG_COUNT or (len(sys.argv) > ARG_COUNT and sys.argv[ARG_NO_STORE] != "NO_STORE"):
                  RestoreMemoryValues(ThisPicDevice, MemoryMapStore)
            print("ALL DEVICE DATA ERASED\n")
#  /********************************/
# /* Erase device config content. */
#/********************************/
         elif "-EC" in sys.argv:
            for Count in range(len(MemoryMap)):
               if  MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_CONF \
               and MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_WO):
                  Data = ""
                  for DataCount in range(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE]):
                     Data = Data + "{:4X}".format(DeviceBlankProgWord)
                  print("{:25} {}".format(PIC_DEVICES.LookupName(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]), Data))
                  MemoryAreaSetData(ThisPicDevice, MemoryMap, PIC_DEVICES.LookupName(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]), Data)
            print("\nALL DEVICE CONFIG ERASED\n")
#  /***********************/
# /* Blank check device. */
#/***********************/
         elif "-B" in sys.argv:
            for Count in range(len(MemoryMap)):
               if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
                  print(PIC_DEVICES.Lookup(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))
                  Data = GetDeviceData(ThisPicDevice, MemoryMap, Count)
                  
                  Result = False
                  if len(Data) == 0 or Data[0] == PIC_API.PIC_UNKNOWN_WORD:
                     print("UNKNOWN MEMORY TYPE\n")
                     continue
                  elif MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_DATA:
                     Result = BlankCheck(ThisPicDevice, DeviceBlankDataWord, Data)
                  else:
                     Result = BlankCheck(ThisPicDevice, DeviceBlankProgWord, Data)

                  if int(Result / 1000) == int(BLANK_PASS / 1000):
                     print("{:08X} -> {:08X} : BLANK".format(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR], (MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR] + MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE])))
                  elif int(Result / 1000) == int(BLANK_FAIL / 1000):
                     print("{:08X} -> {:08X} : {:.4}% USED !NOT BLANK!".format(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR], (MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR] + MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE]), Result - BLANK_FAIL))
                  elif int(Result / 1000) == int(BLANK_PROTECTED / 1000):
                     print("{:08X} -> {:08X} : !PROTECTED!".format(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR], (MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR] + MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE])))

                  print("")
#  /*****************************/
# /* List device memory areas. */
#/*****************************/
         elif "-LM" in sys.argv:
            for Count in range(len(MemoryMap)):
               if MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_RW:
                  print("R/W [{:08X}] [{:6X}] {}".format(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR], MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE], PIC_DEVICES.LookupName(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE])))
               elif MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_RO:
                  print("R   [{:08X}] [{:6X}] {}".format(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR], MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE], PIC_DEVICES.LookupName(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE])))
               elif MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & PIC_DEVICES.PICMEM_WO:
                  print("  W [{:08X}] [{:6X}] {}".format(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_ADDR], MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_SIZE], PIC_DEVICES.LookupName(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE])))
            print("")
#  /**************************************/
# /* Load data into device memory area. */
#/**************************************/
         elif "-LD" in sys.argv and len(sys.argv) > ARG_COUNT + 1:
            MemoryAreaSetData(ThisPicDevice, MemoryMap, sys.argv[ARG_MEM_AREA], sys.argv[ARG_DATA])
#  /******************************/
# /* Valid arguments not found. */
#/******************************/
         else:
            print("INVALID ARGUMENTS PROVIDED\n")

#  /*************************************/
# /* Identify device currently in use. */
#/*************************************/
         if ThisPicDevice != "":
            for Count in range(len(MemoryMap)):
               if len(sys.argv) >= ARG_COUNT and PIC_DEVICES.LookupName(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]) == "CONFIG:DEV_ID" and MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE] & (PIC_DEVICES.PICMEM_RW | PIC_DEVICES.PICMEM_RO):
                  print(PIC_DEVICES.Lookup(MemoryMap[Count][PIC_DEVICES.PICDEV_MEM_TYPE]))
                  Data = GetDeviceData(ThisPicDevice, MemoryMap, Count)
                  if len(Data) == 0 or (Data[0] & 0x3FE0) not in PIC_DEVICES.LookupDeviceID or Data[0] == DeviceBlankProgWord:
                     print("CURRENT DEVICE UNKNOWN TYPE: {:X}\n".format(Data[0]))
                  else:
                     LookupPicDevice = PIC_DEVICES.LookupDeviceID[Data[0] & 0x3FE0]
                     if ThisPicDevice != LookupPicDevice:
                        print("***** WARNING ***** {:} != {:}".format(ThisPicDevice, LookupPicDevice))
                     print("CURRENT DEVICE TYPE: [{:X}] {:} REV:{:}\n".format(Data[0] & 0x3FE0, LookupPicDevice, Data[0] & 0x001F))

#  /*************************************************/
# /* Close Raspberry Pi GPIO use before finishing. */
#/*************************************************/
   RPi.GPIO.cleanup()

