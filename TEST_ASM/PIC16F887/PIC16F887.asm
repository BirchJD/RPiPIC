                  LIST     P = P16F887

                  INCLUDE  "../INCLUDE/P16F887.INC"

                  __CONFIG _INTRC_OSC_NOCLKOUT & _WDT_ON & _PWRTE_ON & _MCLRE_OFF & _IESO_OFF & _FCMEN_OFF & _BOREN_OFF & _DEBUG_OFF & _CP_OFF & _CPD_OFF


;/********************************************************************************/
;/* Raspberry Pi PIC Programmer - Example LED Flash Program For Device PIC16F887 */
;/* V1.00 2017-12-31 (C) Jason Birch                                             */
;/********************************************************************************/


;/*************/
;/* Constants */
;/*************/
GPIO_LED          EQU      (1 << RB5)           ; GPIO pin allocated for driving an LED.
GPIO_SWITCH       EQU      (1 << RB4)           ; GPIO pin allocated for sensing a switch press.

DO_FLASH_COUNT    EQU      0x06                 ; Number of times to invert LED on button press.



;/******************/
;/* RAM Registers. */
;/******************/
CBLOCK            0x20
                  FLASH_COUNT                   ; Keep track of howmany LED inversions remain.
ENDC



                  CODE

;/**********************************/
;/* Reset program location vector. */
;/**********************************/
                  ORG      0x0000

                  BCF      STATUS, RP0          ; Select Register bank 2
                  BSF      STATUS, RP1
                  CLRF     PORTB                ; Clear GPIO port state.
                  GOTO     INIT



;/*************************************/
;/* Interupt program location vector. */
;/*************************************/
                  ORG      0x0004

INT_HANDLE        BCF      STATUS, RP0          ; Select Register bank 0
                  BCF      STATUS, RP1

                  BTFSS    PIR1, TMR1IF         ; Did a TIMER1 interupt trigger?
                  GOTO     INT_GPI
                  MOVF     FLASH_COUNT, F       ; Is a flashing process active?
                  BTFSC    STATUS, Z
                  GOTO     INT_TIMER1_END
                  MOVLW    GPIO_LED
                  XORWF    PORTB, F             ; Invert LED.
                  DECF     FLASH_COUNT          ; Reduce flash count.
INT_TIMER1_END    BCF      PIR1, TMR1IF

INT_GPI           BTFSS    INTCON, RBIF         ; Did an input pin interupt trigger?
                  GOTO     INT_END
                  MOVF     FLASH_COUNT, F       ; Is a flashing process active?
                  BTFSS    STATUS, Z
                  GOTO     INT_GPI_END
                  CLRF     TMR1L                ; Configure full TIMER1 period.
                  CLRF     TMR1H
                  MOVLW    DO_FLASH_COUNT       ; Set flash LED count.
                  MOVWF    FLASH_COUNT
INT_GPI_END       MOVFW    PORTB                ; Read PORTB so interupt flag can be cleared.
                  BCF      INTCON, RBIF

INT_END           RETFIE



;/*******************************/
;/* Initialise microcontroller. */
;/*******************************/
INIT              CLRF     CM1CON0              ; Switch comparitor off.
                  CLRF     CM2CON0
                  CLRF     CM2CON1

                  BSF      STATUS, RP0          ; Select Register bank 3

                  CLRF     ANSEL                ; Switch off A/D pins, all pins digital.
                  CLRF     ANSELH

                  BSF      STATUS, RP0          ; Select Register bank 1
                  BCF      STATUS, RP1

                  MOVLW    (1 << NOT_RBPU)|(1 << PS0)|(1 << PS1)|(1 << PS2) ; Prescale timer.
                  MOVWF    OPTION_REG
                  MOVLW    ~GPIO_LED            ; All GPIO as an input except LED GPIO.
                  MOVWF    TRISB
                  MOVLW    GPIO_SWITCH
                  MOVWF    WPUB                 ; Weak pull up on switch.
                  MOVWF    IOCB                 ; Interupt on change of switch state.
                  MOVLW    (1 << TMR1IE)        ; Intrupt on Timer1 overflow.
                  MOVWF    PIE1

                  BCF      STATUS, RP0          ; Select Register bank 0

                  CLRF     ADCON0               ; Turn off the A/D.
                  CLRF     TMR1L                ; Configure full TIMER1 period.
                  CLRF     TMR1H
                  MOVLW    (1 << TMR1ON)|(1 << NOT_T1SYNC)|(1 << T1CKPS0)|(1 << T1CKPS1)
                  MOVWF    T1CON                ; Configure Timer1.
                  MOVLW    (1 << GIE)|(1 << PEIE)|(1 << RBIE)
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
                  ORG      0x2000               ; Area for PIC USER ID - compiler will complain.

                  DE       0x55, 0x55, 0x55, 0x55


                  ORG      0x2100               ; EEPROM Area.

                  DE       0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF


                  ORG      0x2110               ; EEPROM Area.

                  DE       0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07
                  DE       0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F


                  END

