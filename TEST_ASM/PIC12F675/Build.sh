#!/bin/bash

#/************************/
#/* Compile application. */
#/************************/
gpasm -w 1 -c PIC12F675.asm

if [ $? -eq 0 ]
then
#/*********************/
#/* Link application. */
#/*********************/
   gplink -o PIC12F675.hex PIC12F675.o

   if [ $? -eq 0 ]
   then
#/******************************/
#/* Simulate test application. */
#/******************************/
      gpsim -s PIC12F675.cod
   fi
fi

