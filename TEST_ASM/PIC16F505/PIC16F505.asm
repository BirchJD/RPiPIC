                  LIST     P = P16F505

                  INCLUDE  "../INCLUDE/P16F505.INC"

                  __CONFIG _OSC_IntRC_RB4EN & _WDT_ON & _MCLRE_OFF & _CP_OFF


;/********************************************************************************/
;/* Raspberry Pi PIC Programmer - Example LED Flash Program For Device PIC16F505 */
;/* V1.00 2019-05-11 (C) Jason Birch                                             */
;/********************************************************************************/


;/*************/
;/* Constants */
;/*************/
GPIO_LED          EQU      (1 << RC5)           ; GPIO pin allocated for driving an LED.
GPIO_SWITCH       EQU      (1 << RB4)           ; GPIO pin allocated for sensing a switch press.
GPIO_SWITCH_BIT   EQU      RB4

SCALE_COUNT_VALUE EQU      0x10                 ; TIMER0 Scaling value.
DO_FLASH_COUNT    EQU      0x06                 ; Number of times to invert LED on button press.



;/******************/
;/* RAM Registers. */
;/******************/
CBLOCK            0x08
                  FLASH_COUNT                   ; Keep track of howmany LED inversions remain.
                  SCALE_COUNT                   ; Scale timer.
ENDC



                  CODE

;/**********************************/
;/* Reset program location vector. */
;/**********************************/
                  ORG      0x03FF

                  GOTO     0x0000



                  ORG      0x0000

;/*************************************/
;/* Interupt program location vector. */
;/*************************************/
;                 NO INTERUPTS PRESENT IN THIS MICRO-CONTROLLER.

;/*******************************/
;/* Initialise microcontroller. */
;/*******************************/
INIT              MOVLW    (1 << PS0)|(1 << PS1)|(1 << PS2)|(1 << NOT_GPPU)|(1 << NOT_GPWU) ; Prescale timer.
                  OPTION
                  MOVLW    ~GPIO_LED            ; All GPIO as an input except LED GPIO.
                  TRIS     PORTC
                  CLRF     PORTB                ; Clear GPIO port state.
                  CLRF     PORTC
                  CLRF     FLASH_COUNT          ; Clear the flash count RAM register.
                  CLRF     SCALE_COUNT          ; Clear the timer scaling count.

LOOP              CLRWDT                        ; Tell the CPU the program is still running.

                  BTFSC    PORTB, GPIO_SWITCH_BIT ; Wait for key press.
                  GOTO     LOOP

                  CLRF     TMR0                 ; Configure full TIMER0 period.
                  MOVLW    SCALE_COUNT_VALUE    ; Reset TIMER0 scaling value.
                  MOVWF    SCALE_COUNT
                  MOVLW    DO_FLASH_COUNT       ; Set flash LED count.
                  MOVWF    FLASH_COUNT

TIMER_WAIT        CLRWDT
                  BTFSS    TMR0, 7              ; Did a TIMER0 count below half?
                  GOTO     TIMER_WAIT
                  CLRF     TMR0
                  DECFSZ   SCALE_COUNT
                  GOTO     TIMER_WAIT
                  MOVLW    SCALE_COUNT_VALUE    ; Reset TIMER0 scaling value.
                  MOVWF    SCALE_COUNT

                  COMF     PORTC                ; Invert LED.
                  DECFSZ   FLASH_COUNT          ; Is a flashing process active?
                  GOTO     TIMER_WAIT
                  GOTO     LOOP                 ; Infinite main loop.



;/*********************************/
;/* Write data to data area test. */
;/*********************************/
                  ORG      0x2000               ; Area for PIC USER ID - compiler will complain.

                  DE       0x55, 0x55, 0x55, 0x55



;                  ORG      0x2005               ; Area for OSCAL - compiler will complain.

;                  DE       0xFF



;                  ORG      0x2100               ; EEPROM Area.

;                  NO EEPROM MEMORY PRESENT IN THIS MICRO-CONTROLLER.


                  END

