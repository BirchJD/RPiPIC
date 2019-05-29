                  LIST     P = P16F684          ; Current version of GPASM doesn't support P16F18326, so dupe gpasm.

                  INCLUDE  "../INCLUDE/P16F18326.INC"

                  ORG      0x10007               ; Current version of GPASM doesn't support P16F18326, so work around.

                  DW       _RSTOSC_HFINT1 & _FEXTOSC_OFF & _CLKOUTEN_OFF & _CSWEN_ON & _FCMEN_ON
                  DW       _WDTE_ON & _PWRTE_ON & _MCLRE_OFF & _BOREN_OFF & _LPBOREN_OFF & _BORV_LOW & _PPS1WAY_ON & _STVREN_ON & _DEBUG_OFF
                  DW       _WRT_OFF & _LVP_ON
                  DW       _CP_OFF & _CPD_OFF


;/**********************************************************************************/
;/* Raspberry Pi PIC Programmer - Example LED Flash Program For Device PIC16F18326 */
;/* V1.00 2018-01-22 (C) Jason Birch                                               */
;/**********************************************************************************/


;/*************/
;/* Constants */
;/*************/
GPIO_LED          EQU      (1 << RC5)           ; GPIO pin allocated for driving an LED.
GPIO_SWITCH       EQU      (1 << RA4)           ; GPIO pin allocated for sensing a switch press.

DO_FLASH_COUNT    EQU      0x06                 ; Number of times to invert LED on button press.



;/******************/
;/* RAM Registers. */
;/******************/
CBLOCK            0x20
                  FLASH_COUNT                   ; Keep track of how many LED inversions remain.
ENDC



                  CODE

;/**********************************/
;/* Reset program location vector. */
;/**********************************/
                  ORG      0x0000

                  MOVLW    0x06                 ; SELECT REGISTER BANK 6
                  MOVWF    BSR
                  GOTO     INIT



;/*************************************/
;/* Interupt program location vector. */
;/*************************************/
                  ORG      0x0004

INT_HANDLE        CLRF     BSR                  ; SELECT REGISTER BANK 0

                  BTFSS    PIR1, TMR1IF         ; Did a TIMER1 interupt trigger?
                  GOTO     INT_GPI
                  MOVF     FLASH_COUNT, F       ; Is a flashing process active?
                  BTFSC    STATUS, Z
                  GOTO     INT_TIMER1_END
                  COMF     PORTC                ; Invert LED.
                  DECF     FLASH_COUNT          ; Reduce flash count.
INT_TIMER1_END    BCF      PIR1, TMR1IF

INT_GPI           MOVLW    0x07                 ; SELECT REGISTER BANK 7
                  MOVWF    BSR
                  MOVF     IOCAF, F             ; Did an input pin interupt trigger?
                  BTFSC    STATUS, Z
                  GOTO     INT_END
                  CLRF     BSR                  ; SELECT REGISTER BANK 0
                  MOVF     FLASH_COUNT, F       ; Is a flashing process active?
                  BTFSS    STATUS, Z
                  GOTO     INT_GPI_END
                  CLRF     TMR1L                ; Configure full TIMER1 period.
                  CLRF     TMR1H
                  MOVLW    DO_FLASH_COUNT       ; Set flash LED count.
                  MOVWF    FLASH_COUNT
INT_GPI_END       MOVLW    0x07                 ; SELECT REGISTER BANK 7
                  MOVWF    BSR
                  CLRF     IOCAF

INT_END           CLRF     BSR                  ; SELECT REGISTER BANK 0
                  RETFIE



;/*******************************/
;/* Initialise microcontroller. */
;/*******************************/
INIT              CLRF     CCP3CON              ; Switch off comparitors.
                  CLRF     CCP4CON

                  MOVLW    0x03                 ; SELECT REGISTER BANK 3
                  MOVWF    BSR

                  CLRF     ANSELA               ; Switch off A/D pins, all pins digital.
;                  CLRF     ANSELB
                  CLRF     ANSELC

                  MOVLW    0x01                 ; SELECT REGISTER BANK 1
                  MOVWF    BSR

                  MOVLW    0x0F                 ; Prescale watchdog timer.
                  MOVWF    WDTCON
                  MOVLW    ~GPIO_LED            ; All GPIO as an input except LED GPIO.
                  MOVWF    TRISC
                  MOVLW    (1 << IOCIE)         ; Intrupt on input change.
                  MOVWF    PIE0
                  MOVLW    (1 << TMR1IE)        ; Intrupt on Timer1 overflow.
                  MOVWF    PIE1

                  MOVLW    0x04                 ; SELECT REGISTER BANK 4
                  MOVWF    BSR

                  MOVLW    GPIO_SWITCH
                  MOVWF    WPUA                 ; Weak pull up on switch.

                  MOVLW    0x07                 ; SELECT REGISTER BANK 7
                  MOVWF    BSR

                  MOVLW    GPIO_SWITCH
                  MOVWF    IOCAP                ; Interupt on change of switch state.
                  MOVWF    IOCAN
                  CLRF     IOCAF

                  CLRF     BSR                  ; SELECT REGISTER BANK 0

                  CLRF     PORTA                ; Clear GPIO port state.
                  CLRF     PORTC
                  MOVLW    (1 << TMR1ON)|(1 << T1SYNC)|(1 << T1CKPS0) ;|(1 << T1CKPS1)
                  MOVWF    T1CON                ; Configure Timer1.
                  MOVLW    (1 << GIE)|(1 << PEIE)
                  MOVWF    INTCON               ; Enable interupts.
                  CLRF     PIR1                 ; Clear interupt triggered flags.

                  CLRF     FLASH_COUNT          ; Clear the flash count RAM register.

LOOP              SLEEP                         ; Low power mode when inactive.
ACTIVE_LOOP       CLRWDT                        ; Tell the CPU the program is still running.
                  MOVF     FLASH_COUNT, F       ; Is a flashing process active?
                  BTFSS    STATUS, Z
                  GOTO     ACTIVE_LOOP          ; Keep processor awake to receive timer interupts.
                  GOTO     LOOP                 ; Infinite main loop.



;/*********************************/
;/* Write data to data area test. */
;/*********************************/
                  ORG      0x10001               ; Area for PIC USER ID - compiler will complain.

                  DE       0x55, 0x55, 0x55, 0x55


                  ORG      0x10100               ; EEPROM Area.

                  DE       0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF


                  ORG      0x10110               ; EEPROM Area.

                  DE       0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07
                  DE       0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F


                  END

