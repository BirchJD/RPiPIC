                  LIST     P = P12F675

                  INCLUDE  "../INCLUDE/P12F675.INC"

                  __CONFIG _INTRC_OSC_NOCLKOUT & _WDT_ON & _PWRTE_ON & _MCLRE_OFF & _BOREN_OFF & _CP_OFF & _CPD_OFF



;/*************/
;/* Constants */
;/*************/
GPIO_LED          EQU      0x04                 ; GPIO pin allocated for driving an LED.
GPIO_SWITCH       EQU      0x08                 ; GPIO pin allocated for driving an LED.

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

                  CLRF     STATUS               ; Clear the status register and select register bank 0
                  BCF      STATUS, RP0          ; Select Register bank 0
                  GOTO     INIT



;/*************************************/
;/* Interupt program location vector. */
;/*************************************/
                  ORG      0x0004

                  GOTO     INT_HANDLE



INT_HANDLE        BCF      STATUS, RP0          ; Select Register bank 0
                  BTFSS    PIR1, TMR1IF         ; Did a TIMER1 interupt trigger?
                  GOTO     INT_TIMER1_END
                  MOVFW    FLASH_COUNT          ; Is a flashing process active?
                  ANDLW    0xFF
                  BTFSC    STATUS, Z
                  GOTO     INT_TIMER1_END
                  MOVLW    ~GPIO2               ; Invert LED.
                  XORWF    GPIO
                  DECF     FLASH_COUNT          ; Reduce flash count.

INT_TIMER1_END:   BCF      PIR1, TMR1IF

                  BTFSS    INTCON, GPIF         ; Did an input pin interupt trigger?
                  GOTO     INT_GPI_END
                  MOVFW    FLASH_COUNT          ; Is a flashing process active?
                  ANDLW    0xFF
                  BTFSS    STATUS, Z
                  GOTO     INT_GPI_END
                  MOVLW    0x00                 ; Configure full TIMER1 period.
                  MOVWF    TMR1L
                  MOVLW    0x00
                  MOVWF    TMR1H
                  MOVLW    DO_FLASH_COUNT       ; Set flash LED count.
                  MOVWF    FLASH_COUNT

INT_GPI_END:      BCF      INTCON, GPIF
                  RETFIE



;/*******************************/
;/* Initialise microcontroller. */
;/*******************************/
                  ORG      0x0100

INIT:             CLRF     GPIO
                  CLRF     PIR1
                  MOVLW    0x07                 ; All GPIO as digital IO.
                  MOVWF    CMCON
                  MOVLW    0x3D                 ; Configure Timer1.
                  MOVWF    T1CON
                  BSF      STATUS, RP0          ; Select Register bank 1
                  CLRF     WPU
                  CLRF     ANSEL
                  MOVLW    0x0F                 ; Prescale watchdog timer.
                  MOVWF    OPTION_REG
                  MOVLW    ~GPIO_LED            ; All GPIO as an input except LED GPIO.
                  MOVWF    TRISIO
                  MOVLW    0xC8                 ; Configure GPIO input.
                  MOVWF    INTCON
                  MOVLW    GPIO_SWITCH          ; Configure GPIO input.
                  MOVWF    IOC
                  MOVLW    0x01                 ; Configure Timer1.
                  MOVWF    PIE1

                  BCF      STATUS, RP0          ; Select Register bank 0
                  CLRF     FLASH_COUNT          ; Clear the flash count RAM register.

LOOP              SLEEP                         ; Low power mode when inactive.
ACTIVE_LOOP       CLRWDT                        ; Tell the CPU the program is still running.
                  MOVFW    FLASH_COUNT          ; Is a flashing process active?
                  ANDLW    0xFF
                  BTFSS    STATUS, Z
                  GOTO     ACTIVE_LOOP
                  GOTO     LOOP                 ; Infinite main loop, waiting for interupts.



;/*********************************/
;/* Write data to data area test. */
;/*********************************/
                  ORG      0x2000 ; Area for PIC ID  - compiler will complain.

                  DE       0x55, 0x55, 0x55, 0x55


                  ORG      0x2100

                  DE       0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF


                  ORG      0x2110

                  DE       0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07
                  DE       0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F


                  END

