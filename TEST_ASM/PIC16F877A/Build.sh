#!/bin/bash

#/************************/
#/* Compile application. */
#/************************/
gpasm -w 1 -c PIC16F877A.asm

if [ $? -eq 0 ]
then
#/*********************/
#/* Link application. */
#/*********************/
   gplink -o PIC16F877A.hex PIC16F877A.o

   if [ $? -eq 0 ]
   then
#/******************************/
#/* Simulate test application. */
#/******************************/
      gpsim -s PIC16F877A.cod
   fi
fi

