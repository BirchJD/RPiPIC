#!/bin/bash

#/************************/
#/* Compile application. */
#/************************/
gpasm -w 1 -c PIC16F887.asm

if [ $? -eq 0 ]
then
#/*********************/
#/* Link application. */
#/*********************/
   gplink -o PIC16F887.hex PIC16F887.o

   if [ $? -eq 0 ]
   then
#/******************************/
#/* Simulate test application. */
#/******************************/
      gpsim -s PIC16F887.cod
   fi
fi

