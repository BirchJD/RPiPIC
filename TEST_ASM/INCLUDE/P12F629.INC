        LIST

;==========================================================================
;  MPASM PIC12F629 processor include
; 
;  (c) Copyright 1999-2011 Microchip Technology, All rights reserved
;==========================================================================

        NOLIST

;==========================================================================
;  This header file defines configurations, registers, and other useful
;  bits of information for the PIC12F629 microcontroller.  These names
;  are taken to match the data sheets as closely as possible.
;
;  Note that the processor must be selected before this file is included.
;  The processor may be selected the following ways:
;
;       1. Command line switch:
;               C:\MPASM MYFILE.ASM /PIC12F629
;       2. LIST directive in the source file
;               LIST   P=PIC12F629
;       3. Processor Type entry in the MPASM full-screen interface
;       4. Setting the processor in the MPLAB Project Dialog
;==========================================================================

;==========================================================================
;
;       Verify Processor
;
;==========================================================================
        IFNDEF __12F629
           MESSG "Processor-header file mismatch.  Verify selected processor."
        ENDIF



;==========================================================================
;
;       Register Definitions
;
;==========================================================================

W                EQU  H'0000'
F                EQU  H'0001'

;----- Register Files -----------------------------------------------------

;-----Bank0------------------
INDF             EQU  H'0000'
TMR0             EQU  H'0001'
PCL              EQU  H'0002'
STATUS           EQU  H'0003'
FSR              EQU  H'0004'
GPIO             EQU  H'0005'
PCLATH           EQU  H'000A'
INTCON           EQU  H'000B'
PIR1             EQU  H'000C'
TMR1L            EQU  H'000E'
TMR1H            EQU  H'000F'
T1CON            EQU  H'0010'
CMCON            EQU  H'0019'

;-----Bank1------------------
OPTION_REG       EQU  H'0081'
TRISIO           EQU  H'0085'
PIE1             EQU  H'008C'
PCON             EQU  H'008E'
OSCCAL           EQU  H'0090'
WPU              EQU  H'0095'
IOC              EQU  H'0096'
IOCB             EQU  H'0096'
VRCON            EQU  H'0099'
EEDAT            EQU  H'009A'
EEDATA           EQU  H'009A'
EEADR            EQU  H'009B'
EECON1           EQU  H'009C'
EECON2           EQU  H'009D'

;----- STATUS Bits -----------------------------------------------------
C                EQU  H'0000'
DC               EQU  H'0001'
Z                EQU  H'0002'
NOT_PD           EQU  H'0003'
NOT_TO           EQU  H'0004'
IRP              EQU  H'0007'

RP0              EQU  H'0005'
RP1              EQU  H'0006'


;----- GPIO Bits -----------------------------------------------------
GP0              EQU  H'0000'
GP1              EQU  H'0001'
GP2              EQU  H'0002'
GP3              EQU  H'0003'
GP4              EQU  H'0004'
GP5              EQU  H'0005'

GPIO0            EQU  H'0000'
GPIO1            EQU  H'0001'
GPIO2            EQU  H'0002'
GPIO3            EQU  H'0003'
GPIO4            EQU  H'0004'
GPIO5            EQU  H'0005'


;----- INTCON Bits -----------------------------------------------------
GPIF             EQU  H'0000'
INTF             EQU  H'0001'
T0IF             EQU  H'0002'
GPIE             EQU  H'0003'
INTE             EQU  H'0004'
T0IE             EQU  H'0005'
PEIE             EQU  H'0006'
GIE              EQU  H'0007'

TMR0IF           EQU  H'0002'
TMR0IE           EQU  H'0005'


;----- PIR1 Bits -----------------------------------------------------
TMR1IF           EQU  H'0000'
CMIF             EQU  H'0003'
ADIF             EQU  H'0006'
EEIF             EQU  H'0007'

T1IF             EQU  H'0000'


;----- T1CON Bits -----------------------------------------------------
TMR1ON           EQU  H'0000'
TMR1CS           EQU  H'0001'
NOT_T1SYNC       EQU  H'0002'
T1OSCEN          EQU  H'0003'
TMR1GE           EQU  H'0006'

T1CKPS0          EQU  H'0004'
T1CKPS1          EQU  H'0005'


;----- CMCON Bits -----------------------------------------------------
CIS              EQU  H'0003'
CINV             EQU  H'0004'
COUT             EQU  H'0006'

CM0              EQU  H'0000'
CM1              EQU  H'0001'
CM2              EQU  H'0002'


;----- OPTION_REG Bits -----------------------------------------------------
PSA              EQU  H'0003'
T0SE             EQU  H'0004'
T0CS             EQU  H'0005'
INTEDG           EQU  H'0006'
NOT_GPPU         EQU  H'0007'

PS0              EQU  H'0000'
PS1              EQU  H'0001'
PS2              EQU  H'0002'


;----- TRISIO Bits -----------------------------------------------------
TRISIO0          EQU  H'0000'
TRISIO1          EQU  H'0001'
TRISIO2          EQU  H'0002'
TRISIO3          EQU  H'0003'
TRISIO4          EQU  H'0004'
TRISIO5          EQU  H'0005'


;----- PIE1 Bits -----------------------------------------------------
TMR1IE           EQU  H'0000'
CMIE             EQU  H'0003'
ADIE             EQU  H'0006'
EEIE             EQU  H'0007'

T1IE             EQU  H'0000'


;----- PCON Bits -----------------------------------------------------
NOT_BOR          EQU  H'0000'
NOT_POR          EQU  H'0001'

NOT_BOD          EQU  H'0000'


;----- OSCCAL Bits -----------------------------------------------------
CAL0             EQU  H'0002'
CAL1             EQU  H'0003'
CAL2             EQU  H'0004'
CAL3             EQU  H'0005'
CAL4             EQU  H'0006'
CAL5             EQU  H'0007'


;----- WPU Bits -----------------------------------------------------
WPU0             EQU  H'0000'
WPU1             EQU  H'0001'
WPU2             EQU  H'0002'
WPU4             EQU  H'0004'
WPU5             EQU  H'0005'


;----- IOC Bits -----------------------------------------------------
IOC0             EQU  H'0000'
IOC1             EQU  H'0001'
IOC2             EQU  H'0002'
IOC3             EQU  H'0003'
IOC4             EQU  H'0004'
IOC5             EQU  H'0005'

IOCB0            EQU  H'0000'
IOCB1            EQU  H'0001'
IOCB2            EQU  H'0002'
IOCB3            EQU  H'0003'
IOCB4            EQU  H'0004'
IOCB5            EQU  H'0005'


;----- IOCB Bits -----------------------------------------------------
IOC0             EQU  H'0000'
IOC1             EQU  H'0001'
IOC2             EQU  H'0002'
IOC3             EQU  H'0003'
IOC4             EQU  H'0004'
IOC5             EQU  H'0005'

IOCB0            EQU  H'0000'
IOCB1            EQU  H'0001'
IOCB2            EQU  H'0002'
IOCB3            EQU  H'0003'
IOCB4            EQU  H'0004'
IOCB5            EQU  H'0005'


;----- VRCON Bits -----------------------------------------------------
VRR              EQU  H'0005'
VREN             EQU  H'0007'

VR0              EQU  H'0000'
VR1              EQU  H'0001'
VR2              EQU  H'0002'
VR3              EQU  H'0003'


;----- EECON1 Bits -----------------------------------------------------
RD               EQU  H'0000'
WR               EQU  H'0001'
WREN             EQU  H'0002'
WRERR            EQU  H'0003'



;==========================================================================
;
;       RAM Definitions
;
;==========================================================================
       __MAXRAM  H'00DF'
       __BADRAM  H'0006'-H'0009'
       __BADRAM  H'000D'
       __BADRAM  H'0011'-H'0018'
       __BADRAM  H'001A'-H'001F'
       __BADRAM  H'0060'-H'007F'
       __BADRAM  H'0086'-H'0089'
       __BADRAM  H'008D'
       __BADRAM  H'008F'
       __BADRAM  H'0091'-H'0094'
       __BADRAM  H'0097'-H'0098'
       __BADRAM  H'009E'-H'009F'

;==========================================================================
;
;       Configuration Bits
;
;   NAME            Address
;   CONFIG            2007h
;
;==========================================================================

; The following is an assignment of address values for all of the
; configuration registers for the purpose of table reads
_CONFIG          EQU  H'2007'

;----- CONFIG Options --------------------------------------------------
_FOSC_LP             EQU  H'3FF8'    ; LP oscillator: Low power crystal on GP4/OSC2/CLKOUT and GP5/OSC1/CLKIN
_LP_OSC              EQU  H'3FF8'    ; LP oscillator: Low power crystal on GP4/OSC2/CLKOUT and GP5/OSC1/CLKIN
_FOSC_XT             EQU  H'3FF9'    ; XT oscillator: Crystal/resonator on GP4/OSC2/CLKOUT and GP5/OSC1/CLKIN
_XT_OSC              EQU  H'3FF9'    ; XT oscillator: Crystal/resonator on GP4/OSC2/CLKOUT and GP5/OSC1/CLKIN
_FOSC_HS             EQU  H'3FFA'    ; HS oscillator: High speed crystal/resonator on GP4/OSC2/CLKOUT and GP5/OSC1/CLKIN
_HS_OSC              EQU  H'3FFA'    ; HS oscillator: High speed crystal/resonator on GP4/OSC2/CLKOUT and GP5/OSC1/CLKIN
_FOSC_EC             EQU  H'3FFB'    ; EC: I/O function on GP4/OSC2/CLKOUT pin, CLKIN on GP5/OSC1/CLKIN
_EC_OSC              EQU  H'3FFB'    ; EC: I/O function on GP4/OSC2/CLKOUT pin, CLKIN on GP5/OSC1/CLKIN
_FOSC_INTRCIO        EQU  H'3FFC'    ; INTOSC oscillator: I/O function on GP4/OSC2/CLKOUT pin, I/O function on GP5/OSC1/CLKIN
_INTRC_OSC_NOCLKOUT  EQU  H'3FFC'    ; INTOSC oscillator: I/O function on GP4/OSC2/CLKOUT pin, I/O function on GP5/OSC1/CLKIN
_FOSC_INTRCCLK       EQU  H'3FFD'    ; INTOSC oscillator: CLKOUT function on GP4/OSC2/CLKOUT pin, I/O function on GP5/OSC1/CLKIN
_INTRC_OSC_CLKOUT    EQU  H'3FFD'    ; INTOSC oscillator: CLKOUT function on GP4/OSC2/CLKOUT pin, I/O function on GP5/OSC1/CLKIN
_FOSC_EXTRCIO        EQU  H'3FFE'    ; RC oscillator: I/O function on GP4/OSC2/CLKOUT pin, RC on GP5/OSC1/CLKIN
_EXTRC_OSC_NOCLKOUT  EQU  H'3FFE'    ; RC oscillator: I/O function on GP4/OSC2/CLKOUT pin, RC on GP5/OSC1/CLKIN
_FOSC_EXTRCCLK       EQU  H'3FFF'    ; RC oscillator: CLKOUT function on GP4/OSC2/CLKOUT pin, RC on GP5/OSC1/CLKIN
_EXTRC_OSC_CLKOUT    EQU  H'3FFF'    ; RC oscillator: CLKOUT function on GP4/OSC2/CLKOUT pin, RC on GP5/OSC1/CLKIN

_WDTE_OFF            EQU  H'3FF7'    ; WDT disabled
_WDT_OFF             EQU  H'3FF7'    ; WDT disabled
_WDTE_ON             EQU  H'3FFF'    ; WDT enabled
_WDT_ON              EQU  H'3FFF'    ; WDT enabled

_PWRTE_ON            EQU  H'3FEF'    ; PWRT enabled
_PWRTE_OFF           EQU  H'3FFF'    ; PWRT disabled

_MCLRE_OFF           EQU  H'3FDF'    ; GP3/MCLR pin function is digital I/O, MCLR internally tied to VDD
_MCLRE_ON            EQU  H'3FFF'    ; GP3/MCLR pin function is MCLR

_BOREN_OFF           EQU  H'3FBF'    ; BOD disabled
_BODEN_OFF           EQU  H'3FBF'    ; BOD disabled
_BOREN_ON            EQU  H'3FFF'    ; BOD enabled
_BODEN_ON            EQU  H'3FFF'    ; BOD enabled

_CP_ON               EQU  H'3F7F'    ; Program Memory code protection is enabled
_CP_OFF              EQU  H'3FFF'    ; Program Memory code protection is disabled

_CPD_ON              EQU  H'3EFF'    ; Data memory code protection is enabled
_CPD_OFF             EQU  H'3FFF'    ; Data memory code protection is disabled

;----- DEVID Equates --------------------------------------------------
_DEVID1          EQU  H'2006'

;----- IDLOC Equates --------------------------------------------------
_IDLOC0          EQU  H'2000'
_IDLOC1          EQU  H'2001'
_IDLOC2          EQU  H'2002'
_IDLOC3          EQU  H'2003'

        LIST
