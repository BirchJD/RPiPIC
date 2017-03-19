#!/usr/bin/python2

# HEX_File - Python Intel HEX File Reader
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
#/* HEX_File                                                                 */
#/* ------------------------------------------------------------------------ */
#/* V1.00 - 2016-12-22 - Jason Birch                                         */
#/* ------------------------------------------------------------------------ */
#/* Python Intel HEX File Reader.                                            */
#/****************************************************************************/


import sys
import math
import string


ADDRESS = 0
DATA = 1


#/*******************************/
#/* Return data:                */
#/* [                           */
#/*    Address,                 */
#/*    [                        */
#/*       Data, Data, Data, ... */
#/*    ]                        */
#/* ]                           */
#/*******************************/
def ReadHexFile(FileName):
   BaseAddress = 0
   HexFileData = []

   try:
#  /*************************/
# /* Read Intel .hex file. */
#/*************************/
      print("LOAD HEX DATA FILE: " + FileName)

      File = open(FileName, 'r', 0)
      ThisLine = "."
      while len(ThisLine) > 0:
#  /***********************************/
# /* Read the next line of the file. */
#/***********************************/
         ThisLine = File.readline()

#  /*************************************************/
# /* Seperate the line read into field data items. */
#/*************************************************/
         StartCode = ThisLine[0:1]
         ByteCount = string.atoi(ThisLine[1:3], 16)
         Address = string.atoi(ThisLine[3:7], 16)
         RecordType = string.atoi(ThisLine[7:9], 16)
         Data = ThisLine[9:-3]
         CheckSum = string.atoi(ThisLine[-3:-1], 16)

#  /**********************************/
# /* Identify a valid line of data. */
#/**********************************/
         if StartCode == ":":
#  /***************************************************/
# /* Verify the checksum value for the line of data. */
#/***************************************************/
            ThisCheckSum = 0
            for CheckSumCount in range(1, len(ThisLine) - 4, 2):
               ThisCheckSum = ThisCheckSum + string.atoi(ThisLine[CheckSumCount:CheckSumCount + 2], 16)
            ThisCheckSum = ((~ThisCheckSum) & 0xFF) + 1
            if ThisCheckSum > 255:
               ThisCheckSum = ThisCheckSum - 256
            if CheckSum != ThisCheckSum:
               print("CHECKSUM MISMATCH: {:2.2X} != {:2.2X}".format(CheckSum, ThisCheckSum))

#  /**************************/
# /* Process the data type. */
#/**************************/
            if RecordType == 0:
#  /**************/
# /* Data type. */
#/**************/
               sys.stdout.write("ADDRESS: {:8X} ".format(BaseAddress + Address))
               sys.stdout.write("{:^25s}".format("DATA [" + "{:4d}".format(ByteCount) + "]"))
               HexFileData.append([BaseAddress + Address, []])
               for DataCount in range(0, ByteCount * 2, 2):
                  HexFileData[len(HexFileData) - 1][DATA].append(Data[DataCount:DataCount + 2])
                  Address = Address + 1
               sys.stdout.write("ADDRESS: {:8X}\n".format(BaseAddress + Address))
            elif RecordType == 1:
#  /*********************/
# /* End of file type. */
#/*********************/
               print("EOF")
            elif RecordType == 2:
#  /**********************************/
# /* Extended segment address type. */
#/**********************************/
               BaseAddress = string.atol(Data, 16) * 16
               print("EXTENDED SEGMENT ADDRESS: {:8X}".format(BaseAddress))
            elif RecordType == 3:
#  /*******************************/
# /* Start segment address type. */
#/*******************************/
               BaseAddress = string.atol(Data, 16) * 16
               print("START SEGMENT ADDRESS: {:8X}".format(BaseAddress))
            elif RecordType == 4:
#  /*********************************/
# /* Extended linear address type. */
#/*********************************/
               BaseAddress = string.atol(Data, 16) * int(math.pow(2, 16))
               print("EXTENDED LINEAR ADDRESS: {:8X}".format(BaseAddress))
            elif RecordType == 5:
#  /******************************/
# /* Start linear address type. */
#/******************************/
               BaseAddress = string.atol(Data, 16) * int(math.pow(2, 16))
               print("START LINEAR ADDRESS: {:8X}".format(BaseAddress))

      File.close()
   except:
      print("")

   return HexFileData



def SaveHexFile(FileName, HexData):
#  /*************************/
# /* Read Intel .hex file. */
#/*************************/
   File = open(FileName, 'w', 0)

#  /******************************************/
# /* Standard file extended address header. */
#/******************************************/
   HexLine = ":020000040000FA"
   File.write(HexLine + "\n")
   print(HexLine)

#  /****************************/
# /* Each device memory area. */
#/****************************/
   for Count in range(len(HexData)):
#  /***********************************/
# /* Each memory area block of data. */
#/***********************************/
      for RangeCount in range(len(HexData[Count])):
#  /********************************************/
# /* Write data in lines of 16 bytes maximum. */
#/********************************************/
         DataBatch = 16
         Data = ""
         Address = HexData[Count][RangeCount][0]
         for DataCount in range(len(HexData[Count][RangeCount][1])):
            Data = Data + HexData[Count][RangeCount][1][DataCount]
            DataBatch = DataBatch - 1
            if DataBatch == 0:
               DataBatch = 16
               HexLine = ":{:02X}{:04X}00".format(len(Data) / 2, Address) + Data
               HexLine = HexLine + HexChecksum(HexLine)
               File.write(HexLine + "\n")
               print(HexLine)
               Data = ""
               Address = Address + 16
         if Data != "":
            HexLine = ":{:02X}{:04X}00".format(len(Data) / 2, Address) + Data
            HexLine = HexLine + HexChecksum(HexLine)
            File.write(HexLine + "\n")
            print(HexLine)

#  /*****************************/
# /* Standard file EOF record. */
#/*****************************/
   HexLine = ":00000001FF"
   File.write(HexLine + "\n")
   print(HexLine)
   File.close()
   print("")



def HexChecksum(ThisLine):
#  /********************************************/
# /* Calculate a checksum for a line of data. */
#/********************************************/
   ThisCheckSum = 0
   for CheckSumCount in range(1, len(ThisLine) - 1, 2):
      ThisCheckSum = ThisCheckSum + string.atoi(ThisLine[CheckSumCount:CheckSumCount + 2], 16)
   ThisCheckSum = ((~ThisCheckSum) & 0xFF) + 1

   return "{:02X}".format(ThisCheckSum)

