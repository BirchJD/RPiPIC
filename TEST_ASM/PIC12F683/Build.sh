#!/bin/bash

#/************************/
#/* Compile application. */
#/************************/
gpasm -w 1 -c PIC12F683.asm

if [ $? -eq 0 ]
then
#/*********************/
#/* Link application. */
#/*********************/
   gplink -o PIC12F683.hex PIC12F683.o

   if [ $? -eq 0 ]
   then
#/******************************/
#/* Simulate test application. */
#/******************************/
      gpsim -s PIC12F683.cod
   fi
fi

