                  LIST     P = P18F4550

                  INCLUDE  "../INCLUDE/P18F4550.INC"

                  ; Micro-controller oscilator
                  CONFIG   FOSC = INTOSCIO_EC, IESO = OFF, LPT1OSC = OFF

                  ; Micro-controller configuration
                  CONFIG   PWRT = ON, MCLRE = OFF, PBADEN = OFF, CCP2MX = OFF, STVREN = OFF
                  CONFIG   CPUDIV = OSC1_PLL2, PLLDIV = 12, USBDIV = 2, VREGEN = OFF

                  ; Micro-contoller monitoring
                  CONFIG   WDT = OFF, WDTPS = 512, FCMEN = OFF, BOR = OFF, BORV = 0

                  ; Programming/Debugging
                  CONFIG   DEBUG = OFF, XINST = OFF, LVP = OFF

                  ; Code Protection
                  CONFIG   CP0 = OFF, CP1 = OFF, CP2 = OFF, CPB = OFF, CPD = OFF

                  ; Write Protection
                  CONFIG   WRT0 = OFF, WRT1 = OFF, WRT2 = OFF, WRTC = OFF, WRTB = OFF, WRTD = OFF

                  ; Table Read Protection
                  CONFIG   EBTR0 = OFF, EBTR1 = OFF, EBTR2 = OFF, EBTRB = OFF


;/*********************************************************************************/
;/* Raspberry Pi PIC Programmer - Example LED Flash Program For Device PIC18F4550 */
;/* V1.00 2017-12-31 (C) Jason Birch                                              */
;/*********************************************************************************/


;/*************/
;/* Constants */
;/*************/
GPIO_LED          EQU      (1 << RB5)           ; GPIO pin allocated for driving an LED.
GPIO_SWITCH       EQU      (1 << RB4)           ; GPIO pin allocated for sensing a switch press.

DO_FLASH_COUNT    EQU      0x0006               ; Number of times to invert LED on button press.



;/******************/
;/* RAM Registers. */
;/******************/
CBLOCK            0x0000
                  INT_W                         ; Store W register during interupt.
                  INT_STATUS                    ; Store STATUS register during interupt.
                  INT_BSR                       ; Store BSR register during interupt.

                  FLASH_COUNT                   ; Keep track of howmany LED inversions remain.
ENDC



                  CODE

;/**********************************/
;/* Reset program location vector. */
;/**********************************/
                  ORG      0x000000

                  MOVLW    0x07                 ; Switch comparitor off.
                  MOVWF    CMCON, A
                  GOTO     INIT



;/****************************************************/
;/* Interupt program location vector, high priority. */
;/****************************************************/
                  ORG      0x000008             ; Using RETFIE S, so don't need to save register status.

HP_INT_HANDLE     RETFIE   S



;/***************************************************/
;/* Interupt program location vector, low priority. */
;/***************************************************/
                  ORG      0x000018             ; Can not use RETFIE S as low priority interupt is using it,
                                                ; store/restore register states and just use RETFIE to return.
LP_INT_HANDLE     MOVWF    INT_W, A             ; Store registers, to restore before returning from interupt.
                  MOVFF    STATUS, INT_STATUS
                  MOVFF    BSR, INT_BSR

                  BTFSS    PIR1, TMR1IF, A      ; Did a TIMER1 interupt trigger?
                  GOTO     INT_RBI

                  MOVF     FLASH_COUNT, F, A    ; Is a flashing process active?
                  BTFSC    STATUS, Z, A
                  GOTO     INT_TIMER1_END
                  MOVLW    GPIO_LED
                  XORWF    PORTB, F, A          ; Invert LED.
                  DECF     FLASH_COUNT, F, A       ; Reduce flash count.
INT_TIMER1_END    BCF      PIR1, TMR1IF, A

INT_RBI           BTFSS    INTCON, RBIF, A      ; Did an input pin interupt trigger?
                  GOTO     INT_END

                  MOVF     FLASH_COUNT, F, A    ; Is a flashing process active?
                  BTFSS    STATUS, Z, A
                  GOTO     INT_RBI_END
                  CLRF     TMR1L, A             ; Configure full TIMER1 period.
                  CLRF     TMR1H, A
                  MOVLW    DO_FLASH_COUNT       ; Set flash LED count.
                  MOVWF    FLASH_COUNT, A
INT_RBI_END       MOVF     PORTB, W, A          ; Read PORTB to allow the interupt flag to be cleared.
                  BCF      INTCON, RBIF, A

INT_END           MOVFF    INT_BSR, BSR         ; Restore registers before returning from interupt.
                  MOVF     INT_W, W, A
                  MOVFF    INT_STATUS, STATUS
                  RETFIE



;/*******************************/
;/* Initialise microcontroller. */
;/*******************************/
INIT              BSF      WDTCON, SWDTEN, A    ; Enable watchdog timer.
                  MOVLW    0x0F                 ; Make all pins digital.
                  MOVWF    ADCON1, A
                  CLRF     ADCON0, A            ; Switch off A/D pins, all pins digital.
                  CLRF     PORTB, A             ; Clear GPIO port state.
                  MOVLW    ~GPIO_LED            ; All GPIO as an input except LED GPIO.
                  MOVWF    TRISB, A
                  CLRF     INTCON2, A           ; Weak pull up on switch. Set PORTB as a low pritority interupt.
                  CLRF     IPR1, A              ; Set all interupt priorities to low priority.
                  CLRF     TMR1L, A             ; Configure full TIMER1 period.
                  CLRF     TMR1H, A
                  BSF      RCON, IPEN, A        ; Enable high and low priority interupt states.
                  MOVLW    (1 << GIEH)|(1 << GIEL)|(1 << PEIE)|(1 << RBIE)
                  MOVWF    INTCON, A            ; Enable interupts.
                  MOVLW    (1 << TMR1ON)|(1 << NOT_T1SYNC) ; |(1 << T1CKPS0)|(1 << T1CKPS1)
                  MOVWF    T1CON, A             ; Configure Timer1.
                  MOVLW    (1 << TMR1IE)        ; Intrupt on Timer1 overflow.
                  MOVWF    PIE1, A
                  CLRF     PORTB, A             ; Clear PORTB to allow the interupt flag to be cleared.
                  BCF      INTCON, RBIF, A
                  CLRF     PIR1, A              ; Clear interupt triggered flags.

                  CLRF     FLASH_COUNT, A       ; Clear the flash count RAM register.

LOOP              SLEEP                         ; Low power mode when inactive.
ACTIVE_LOOP       CLRWDT                        ; Tell the CPU the program is still running.
                  MOVF     FLASH_COUNT, F, A    ; Is a flashing process active?
                  BTFSS    STATUS, Z, A
                  GOTO     ACTIVE_LOOP          ; Keep processor awake to receive timer interupts.
                  GOTO     LOOP                 ; Infinite main loop.



;/*********************************/
;/* Write data to data area test. */
;/*********************************/
                  ORG      0x200000             ; Area for PIC USER ID - compiler will complain.

                  DE       0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55



                  ORG      0x400000             ; EEPROM Area.

                  DE       0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF


                  ORG      0x400050             ; EEPROM Area.

                  DE       0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07
                  DE       0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F


                  END

