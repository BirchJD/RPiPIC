#!/bin/bash

#/************************/
#/* Compile application. */
#/************************/
gpasm -w 1 -c PIC18F4550.asm

if [ $? -eq 0 ]
then
#/*********************/
#/* Link application. */
#/*********************/
   gplink -o PIC18F4550.hex PIC18F4550.o

   if [ $? -eq 0 ]
   then
#/******************************/
#/* Simulate test application. */
#/******************************/
      gpsim -s PIC18F4550.cod
   fi
fi

