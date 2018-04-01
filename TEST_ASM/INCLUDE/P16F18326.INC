        LIST

;==========================================================================
; Build date : Sep 19 2017
;  MPASM PIC16F18326 processor include
; 
;  (c) Copyright 1999-2017 Microchip Technology, All rights reserved
;==========================================================================

        NOLIST

;==========================================================================
;  This header file defines configurations, registers, and other useful
;  bits of information for the PIC16F18326 microcontroller.  These names
;  are taken to match the data sheets as closely as possible.
;
;  Note that the processor must be selected before this file is included.
;  The processor may be selected the following ways:
;
;       1. Command line switch:
;               C:\MPASM MYFILE.ASM /PIC16F18326
;       2. LIST directive in the source file
;               LIST   P=PIC16F18326
;       3. Processor Type entry in the MPASM full-screen interface
;       4. Setting the processor in the MPLAB Project Dialog
;==========================================================================

;==========================================================================
;
;       Verify Processor
;
;==========================================================================
        IFNDEF __16F18326
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
INDF0            EQU  H'0000'
INDF1            EQU  H'0001'
PCL              EQU  H'0002'
STATUS           EQU  H'0003'
FSR0             EQU  H'0004'
FSR0L            EQU  H'0004'
FSR0H            EQU  H'0005'
FSR1             EQU  H'0006'
FSR1L            EQU  H'0006'
FSR1H            EQU  H'0007'
BSR              EQU  H'0008'
WREG             EQU  H'0009'
PCLATH           EQU  H'000A'
INTCON           EQU  H'000B'
PORTA            EQU  H'000C'
PORTC            EQU  H'000E'
PIR0             EQU  H'0010'
PIR1             EQU  H'0011'
PIR2             EQU  H'0012'
PIR3             EQU  H'0013'
PIR4             EQU  H'0014'
TMR0             EQU  H'0015'
TMR0L            EQU  H'0015'
PR0              EQU  H'0016'
TMR0H            EQU  H'0016'
T0CON0           EQU  H'0017'
T0CON1           EQU  H'0018'
TMR1             EQU  H'0019'
TMR1L            EQU  H'0019'
TMR1H            EQU  H'001A'
T1CON            EQU  H'001B'
T1GCON           EQU  H'001C'
TMR2             EQU  H'001D'
PR2              EQU  H'001E'
T2CON            EQU  H'001F'

;-----Bank1------------------
TRISA            EQU  H'008C'
TRISC            EQU  H'008E'
PIE0             EQU  H'0090'
PIE1             EQU  H'0091'
PIE2             EQU  H'0092'
PIE3             EQU  H'0093'
PIE4             EQU  H'0094'
WDTCON           EQU  H'0097'
ADRES            EQU  H'009B'
ADRESL           EQU  H'009B'
ADRESH           EQU  H'009C'
ADCON0           EQU  H'009D'
ADCON1           EQU  H'009E'
ADACT            EQU  H'009F'

;-----Bank2------------------
LATA             EQU  H'010C'
LATC             EQU  H'010E'
CM1CON0          EQU  H'0111'
CM1CON1          EQU  H'0112'
CM2CON0          EQU  H'0113'
CM2CON1          EQU  H'0114'
CMOUT            EQU  H'0115'
BORCON           EQU  H'0116'
FVRCON           EQU  H'0117'
DACCON0          EQU  H'0118'
DACCON1          EQU  H'0119'

;-----Bank3------------------
ANSELA           EQU  H'018C'
ANSELC           EQU  H'018E'
VREGCON          EQU  H'0197'
RC1REG           EQU  H'0199'
RCREG            EQU  H'0199'
RCREG1           EQU  H'0199'
TX1REG           EQU  H'019A'
TXREG            EQU  H'019A'
TXREG1           EQU  H'019A'
SP1BRG           EQU  H'019B'
SP1BRGL          EQU  H'019B'
SPBRG            EQU  H'019B'
SPBRG1           EQU  H'019B'
SPBRGL           EQU  H'019B'
SP1BRGH          EQU  H'019C'
SPBRGH           EQU  H'019C'
SPBRGH1          EQU  H'019C'
RC1STA           EQU  H'019D'
RCSTA            EQU  H'019D'
RCSTA1           EQU  H'019D'
TX1STA           EQU  H'019E'
TXSTA            EQU  H'019E'
TXSTA1           EQU  H'019E'
BAUD1CON         EQU  H'019F'
BAUDCON          EQU  H'019F'
BAUDCON1         EQU  H'019F'
BAUDCTL          EQU  H'019F'
BAUDCTL1         EQU  H'019F'

;-----Bank4------------------
WPUA             EQU  H'020C'
WPUC             EQU  H'020E'
SSP1BUF          EQU  H'0211'
SSPBUF           EQU  H'0211'
SSP1ADD          EQU  H'0212'
SSPADD           EQU  H'0212'
SSP1MSK          EQU  H'0213'
SSPMSK           EQU  H'0213'
SSP1STAT         EQU  H'0214'
SSPSTAT          EQU  H'0214'
SSP1CON          EQU  H'0215'
SSP1CON1         EQU  H'0215'
SSPCON           EQU  H'0215'
SSPCON1          EQU  H'0215'
SSP1CON2         EQU  H'0216'
SSPCON2          EQU  H'0216'
SSP1CON3         EQU  H'0217'
SSPCON3          EQU  H'0217'
SSP2BUF          EQU  H'0219'
SSP2ADD          EQU  H'021A'
SSP2MSK          EQU  H'021B'
SSP2STAT         EQU  H'021C'
SSP2CON          EQU  H'021D'
SSP2CON1         EQU  H'021D'
SSP2CON2         EQU  H'021E'
SSP2CON3         EQU  H'021F'

;-----Bank5------------------
ODCONA           EQU  H'028C'
ODCONC           EQU  H'028E'
CCPR1            EQU  H'0291'
CCPR1L           EQU  H'0291'
CCPR1H           EQU  H'0292'
CCP1CON          EQU  H'0293'
CCP1CAP          EQU  H'0294'
CCPR2            EQU  H'0295'
CCPR2L           EQU  H'0295'
CCPR2H           EQU  H'0296'
CCP2CON          EQU  H'0297'
CCP2CAP          EQU  H'0298'
CCPTMRS          EQU  H'029F'

;-----Bank6------------------
SLRCONA          EQU  H'030C'
SLRCONC          EQU  H'030E'
CCPR3            EQU  H'0311'
CCPR3L           EQU  H'0311'
CCPR3H           EQU  H'0312'
CCP3CON          EQU  H'0313'
CCP3CAP          EQU  H'0314'
CCPR4            EQU  H'0315'
CCPR4L           EQU  H'0315'
CCPR4H           EQU  H'0316'
CCP4CON          EQU  H'0317'
CCP4CAP          EQU  H'0318'

;-----Bank7------------------
INLVLA           EQU  H'038C'
INLVLC           EQU  H'038E'
IOCAP            EQU  H'0391'
IOCAN            EQU  H'0392'
IOCAF            EQU  H'0393'
IOCCP            EQU  H'0397'
IOCCN            EQU  H'0398'
IOCCF            EQU  H'0399'
CLKRCON          EQU  H'039A'
MDCON            EQU  H'039C'
MDSRC            EQU  H'039D'
MDCARH           EQU  H'039E'
MDCARL           EQU  H'039F'

;-----Bank8------------------
TMR3             EQU  H'0411'
TMR3L            EQU  H'0411'
TMR3H            EQU  H'0412'
T3CON            EQU  H'0413'
T3GCON           EQU  H'0414'
TMR4             EQU  H'0415'
PR4              EQU  H'0416'
T4CON            EQU  H'0417'
TMR5             EQU  H'0418'
TMR5L            EQU  H'0418'
TMR5H            EQU  H'0419'
T5CON            EQU  H'041A'
T5GCON           EQU  H'041B'
TMR6             EQU  H'041C'
PR6              EQU  H'041D'
T6CON            EQU  H'041E'
CCDCON           EQU  H'041F'

;-----Bank9------------------
NCO1ACC          EQU  H'0498'
NCO1ACCL         EQU  H'0498'
NCO1ACCH         EQU  H'0499'
NCO1ACCU         EQU  H'049A'
NCO1INC          EQU  H'049B'
NCO1INCL         EQU  H'049B'
NCO1INCH         EQU  H'049C'
NCO1INCU         EQU  H'049D'
NCO1CON          EQU  H'049E'
NCO1CLK          EQU  H'049F'

;-----Bank12------------------
PWM5DCL          EQU  H'0617'
PWM5DCH          EQU  H'0618'
PWM5CON          EQU  H'0619'
PWM5CON0         EQU  H'0619'
PWM6DCL          EQU  H'061A'
PWM6DCH          EQU  H'061B'
PWM6CON          EQU  H'061C'
PWM6CON0         EQU  H'061C'
PWMTMRS          EQU  H'061F'

;-----Bank13------------------
CWG1CLKCON       EQU  H'0691'
CWG1DAT          EQU  H'0692'
CWG1DBR          EQU  H'0693'
CWG1DBF          EQU  H'0694'
CWG1CON0         EQU  H'0695'
CWG1CON1         EQU  H'0696'
CWG1AS0          EQU  H'0697'
CWG1AS1          EQU  H'0698'
CWG1STR          EQU  H'0699'

;-----Bank14------------------
CWG2CLKCON       EQU  H'0711'
CWG2DAT          EQU  H'0712'
CWG2DBR          EQU  H'0713'
CWG2DBF          EQU  H'0714'
CWG2CON0         EQU  H'0715'
CWG2CON1         EQU  H'0716'
CWG2AS0          EQU  H'0717'
CWG2AS1          EQU  H'0718'
CWG2STR          EQU  H'0719'

;-----Bank17------------------
EEADR            EQU  H'0891'
EEADRL           EQU  H'0891'
NVMADR           EQU  H'0891'
NVMADRL          EQU  H'0891'
PMADR            EQU  H'0891'
PMADRL           EQU  H'0891'
EEADRH           EQU  H'0892'
NVMADRH          EQU  H'0892'
PMADRH           EQU  H'0892'
EEDAT            EQU  H'0893'
EEDATL           EQU  H'0893'
NVMDAT           EQU  H'0893'
NVMDATL          EQU  H'0893'
PMDAT            EQU  H'0893'
PMDATL           EQU  H'0893'
EEDATH           EQU  H'0894'
NVMDATH          EQU  H'0894'
PMDATH           EQU  H'0894'
EECON1           EQU  H'0895'
NVMCON1          EQU  H'0895'
PMCON1           EQU  H'0895'
EECON2           EQU  H'0896'
NVMCON2          EQU  H'0896'
PMCON2           EQU  H'0896'
PCON0            EQU  H'089B'

;-----Bank18------------------
PMD0             EQU  H'0911'
PMD1             EQU  H'0912'
PMD2             EQU  H'0913'
PMD3             EQU  H'0914'
PMD4             EQU  H'0915'
PMD5             EQU  H'0916'
CPUDOZE          EQU  H'0918'
OSCCON1          EQU  H'0919'
OSCCON2          EQU  H'091A'
OSCCON3          EQU  H'091B'
OSCSTAT1         EQU  H'091C'
OSCEN            EQU  H'091D'
OSCTUNE          EQU  H'091E'
OSCFRQ           EQU  H'091F'

;-----Bank28------------------
PPSLOCK          EQU  H'0E0F'
INTPPS           EQU  H'0E10'
T0CKIPPS         EQU  H'0E11'
T1CKIPPS         EQU  H'0E12'
T1GPPS           EQU  H'0E13'
CCP1PPS          EQU  H'0E14'
CCP2PPS          EQU  H'0E15'
CCP3PPS          EQU  H'0E16'
CCP4PPS          EQU  H'0E17'
CWG1PPS          EQU  H'0E18'
CWG2PPS          EQU  H'0E19'
MDCIN1PPS        EQU  H'0E1A'
MDCIN2PPS        EQU  H'0E1B'
MDMINPPS         EQU  H'0E1C'
SSP2CLKPPS       EQU  H'0E1D'
SSP2DATPPS       EQU  H'0E1E'
SSP2SSPPS        EQU  H'0E1F'
SSP1CLKPPS       EQU  H'0E20'
SSP1DATPPS       EQU  H'0E21'
SSP1SSPPS        EQU  H'0E22'
RXPPS            EQU  H'0E24'
TXPPS            EQU  H'0E25'
CLCIN0PPS        EQU  H'0E28'
CLCIN1PPS        EQU  H'0E29'
CLCIN2PPS        EQU  H'0E2A'
CLCIN3PPS        EQU  H'0E2B'
T3CKIPPS         EQU  H'0E2C'
T3GPPS           EQU  H'0E2D'
T5CKIPPS         EQU  H'0E2E'
T5GPPS           EQU  H'0E2F'

;-----Bank29------------------
RA0PPS           EQU  H'0E90'
RA1PPS           EQU  H'0E91'
RA2PPS           EQU  H'0E92'
RA4PPS           EQU  H'0E94'
RA5PPS           EQU  H'0E95'
RC0PPS           EQU  H'0EA0'
RC1PPS           EQU  H'0EA1'
RC2PPS           EQU  H'0EA2'
RC3PPS           EQU  H'0EA3'
RC4PPS           EQU  H'0EA4'
RC5PPS           EQU  H'0EA5'

;-----Bank30------------------
CLCDATA          EQU  H'0F0F'
CLC1CON          EQU  H'0F10'
CLC1POL          EQU  H'0F11'
CLC1SEL0         EQU  H'0F12'
CLC1SEL1         EQU  H'0F13'
CLC1SEL2         EQU  H'0F14'
CLC1SEL3         EQU  H'0F15'
CLC1GLS0         EQU  H'0F16'
CLC1GLS1         EQU  H'0F17'
CLC1GLS2         EQU  H'0F18'
CLC1GLS3         EQU  H'0F19'
CLC2CON          EQU  H'0F1A'
CLC2POL          EQU  H'0F1B'
CLC2SEL0         EQU  H'0F1C'
CLC2SEL1         EQU  H'0F1D'
CLC2SEL2         EQU  H'0F1E'
CLC2SEL3         EQU  H'0F1F'
CLC2GLS0         EQU  H'0F20'
CLC2GLS1         EQU  H'0F21'
CLC2GLS2         EQU  H'0F22'
CLC2GLS3         EQU  H'0F23'
CLC3CON          EQU  H'0F24'
CLC3POL          EQU  H'0F25'
CLC3SEL0         EQU  H'0F26'
CLC3SEL1         EQU  H'0F27'
CLC3SEL2         EQU  H'0F28'
CLC3SEL3         EQU  H'0F29'
CLC3GLS0         EQU  H'0F2A'
CLC3GLS1         EQU  H'0F2B'
CLC3GLS2         EQU  H'0F2C'
CLC3GLS3         EQU  H'0F2D'
CLC4CON          EQU  H'0F2E'
CLC4POL          EQU  H'0F2F'
CLC4SEL0         EQU  H'0F30'
CLC4SEL1         EQU  H'0F31'
CLC4SEL2         EQU  H'0F32'
CLC4SEL3         EQU  H'0F33'
CLC4GLS0         EQU  H'0F34'
CLC4GLS1         EQU  H'0F35'
CLC4GLS2         EQU  H'0F36'
CLC4GLS3         EQU  H'0F37'

;-----Bank31------------------
STATUS_SHAD      EQU  H'0FE4'
WREG_SHAD        EQU  H'0FE5'
BSR_SHAD         EQU  H'0FE6'
PCLATH_SHAD      EQU  H'0FE7'
FSR0L_SHAD       EQU  H'0FE8'
FSR0H_SHAD       EQU  H'0FE9'
FSR1L_SHAD       EQU  H'0FEA'
FSR1H_SHAD       EQU  H'0FEB'
STKPTR           EQU  H'0FED'
TOSL             EQU  H'0FEE'
TOSH             EQU  H'0FEF'

;----- STATUS Bits -----------------------------------------------------
C                EQU  H'0000'
DC               EQU  H'0001'
Z                EQU  H'0002'
NOT_PD           EQU  H'0003'
NOT_TO           EQU  H'0004'


;----- BSR Bits -----------------------------------------------------
BSR0             EQU  H'0000'
BSR1             EQU  H'0001'
BSR2             EQU  H'0002'
BSR3             EQU  H'0003'
BSR4             EQU  H'0004'


;----- INTCON Bits -----------------------------------------------------
INTEDG           EQU  H'0000'
PEIE             EQU  H'0006'
GIE              EQU  H'0007'


;----- PORTA Bits -----------------------------------------------------
RA0              EQU  H'0000'
RA1              EQU  H'0001'
RA2              EQU  H'0002'
RA3              EQU  H'0003'
RA4              EQU  H'0004'
RA5              EQU  H'0005'


;----- PORTC Bits -----------------------------------------------------
RC0              EQU  H'0000'
RC1              EQU  H'0001'
RC2              EQU  H'0002'
RC3              EQU  H'0003'
RC4              EQU  H'0004'
RC5              EQU  H'0005'


;----- PIR0 Bits -----------------------------------------------------
INTF             EQU  H'0000'
IOCIF            EQU  H'0004'
TMR0IF           EQU  H'0005'


;----- PIR1 Bits -----------------------------------------------------
TMR1IF           EQU  H'0000'
TMR2IF           EQU  H'0001'
BCL1IF           EQU  H'0002'
SSP1IF           EQU  H'0003'
TXIF             EQU  H'0004'
RCIF             EQU  H'0005'
ADIF             EQU  H'0006'
TMR1GIF          EQU  H'0007'


;----- PIR2 Bits -----------------------------------------------------
NCO1IF           EQU  H'0000'
TMR4IF           EQU  H'0001'
BCL2IF           EQU  H'0002'
SSP2IF           EQU  H'0003'
NVMIF            EQU  H'0004'
C1IF             EQU  H'0005'
C2IF             EQU  H'0006'
TMR6IF           EQU  H'0007'


;----- PIR3 Bits -----------------------------------------------------
CLC1IF           EQU  H'0000'
CLC2IF           EQU  H'0001'
CLC3IF           EQU  H'0002'
CLC4IF           EQU  H'0003'
TMR3IF           EQU  H'0004'
TMR3GIF          EQU  H'0005'
CSWIF            EQU  H'0006'
OSFIF            EQU  H'0007'


;----- PIR4 Bits -----------------------------------------------------
CCP1IF           EQU  H'0000'
CCP2IF           EQU  H'0001'
CCP3IF           EQU  H'0002'
CCP4IF           EQU  H'0003'
TMR5IF           EQU  H'0004'
TMR5GIF          EQU  H'0005'
CWG1IF           EQU  H'0006'
CWG2IF           EQU  H'0007'


;----- TMR0 Bits -----------------------------------------------------
TMR00            EQU  H'0000'
TMR01            EQU  H'0001'
TMR02            EQU  H'0002'
TMR03            EQU  H'0003'
TMR04            EQU  H'0004'
TMR05            EQU  H'0005'
TMR06            EQU  H'0006'
TMR07            EQU  H'0007'


;----- TMR0L Bits -----------------------------------------------------
TMR00            EQU  H'0000'
TMR01            EQU  H'0001'
TMR02            EQU  H'0002'
TMR03            EQU  H'0003'
TMR04            EQU  H'0004'
TMR05            EQU  H'0005'
TMR06            EQU  H'0006'
TMR07            EQU  H'0007'


;----- PR0 Bits -----------------------------------------------------
TMR08            EQU  H'0000'
TMR09            EQU  H'0001'
TMR010           EQU  H'0002'
TMR011           EQU  H'0003'
TMR012           EQU  H'0004'
TMR013           EQU  H'0005'
TMR014           EQU  H'0006'
TMR015           EQU  H'0007'



;----- TMR0H Bits -----------------------------------------------------
TMR08            EQU  H'0000'
TMR09            EQU  H'0001'
TMR010           EQU  H'0002'
TMR011           EQU  H'0003'
TMR012           EQU  H'0004'
TMR013           EQU  H'0005'
TMR014           EQU  H'0006'
TMR015           EQU  H'0007'



;----- T0CON0 Bits -----------------------------------------------------
T016BIT          EQU  H'0004'
T0OUT            EQU  H'0005'
T0EN             EQU  H'0007'

T0OUTPS0         EQU  H'0000'
T0OUTPS1         EQU  H'0001'
T0OUTPS2         EQU  H'0002'
T0OUTPS3         EQU  H'0003'


;----- T0CON1 Bits -----------------------------------------------------
T0ASYNC          EQU  H'0004'

T0CKPS0          EQU  H'0000'
T0CKPS1          EQU  H'0001'
T0CKPS2          EQU  H'0002'
T0CKPS3          EQU  H'0003'
T0CS0            EQU  H'0005'
T0CS1            EQU  H'0006'
T0CS2            EQU  H'0007'


;----- T1CON Bits -----------------------------------------------------
TMR1ON           EQU  H'0000'
T1SYNC           EQU  H'0002'
T1SOSC           EQU  H'0003'

T1CKPS0          EQU  H'0004'
T1CKPS1          EQU  H'0005'
TMR1CS0          EQU  H'0006'
TMR1CS1          EQU  H'0007'


;----- T1GCON Bits -----------------------------------------------------
T1GVAL           EQU  H'0002'
T1GGO_NOT_DONE   EQU  H'0003'
T1GSPM           EQU  H'0004'
T1GTM            EQU  H'0005'
T1GPOL           EQU  H'0006'
TMR1GE           EQU  H'0007'

T1GSS0           EQU  H'0000'
T1GSS1           EQU  H'0001'


;----- T2CON Bits -----------------------------------------------------
TMR2ON           EQU  H'0002'

T2CKPS0          EQU  H'0000'
T2CKPS1          EQU  H'0001'
T2OUTPS0         EQU  H'0003'
T2OUTPS1         EQU  H'0004'
T2OUTPS2         EQU  H'0005'
T2OUTPS3         EQU  H'0006'


;----- TRISA Bits -----------------------------------------------------
TRISA0           EQU  H'0000'
TRISA1           EQU  H'0001'
TRISA2           EQU  H'0002'
TRISA4           EQU  H'0004'
TRISA5           EQU  H'0005'


;----- TRISC Bits -----------------------------------------------------
TRISC0           EQU  H'0000'
TRISC1           EQU  H'0001'
TRISC2           EQU  H'0002'
TRISC3           EQU  H'0003'
TRISC4           EQU  H'0004'
TRISC5           EQU  H'0005'


;----- PIE0 Bits -----------------------------------------------------
INTE             EQU  H'0000'
IOCIE            EQU  H'0004'
TMR0IE           EQU  H'0005'


;----- PIE1 Bits -----------------------------------------------------
TMR1IE           EQU  H'0000'
TMR2IE           EQU  H'0001'
BCL1IE           EQU  H'0002'
SSP1IE           EQU  H'0003'
TXIE             EQU  H'0004'
RCIE             EQU  H'0005'
ADIE             EQU  H'0006'
TMR1GIE          EQU  H'0007'


;----- PIE2 Bits -----------------------------------------------------
NCO1IE           EQU  H'0000'
TMR4IE           EQU  H'0001'
BCL2IE           EQU  H'0002'
SSP2IE           EQU  H'0003'
NVMIE            EQU  H'0004'
C1IE             EQU  H'0005'
C2IE             EQU  H'0006'
TMR6IE           EQU  H'0007'


;----- PIE3 Bits -----------------------------------------------------
CLC1IE           EQU  H'0000'
CLC2IE           EQU  H'0001'
CLC3IE           EQU  H'0002'
CLC4IE           EQU  H'0003'
TMR3IE           EQU  H'0004'
TMR3GIE          EQU  H'0005'
CSWIE            EQU  H'0006'
OSFIE            EQU  H'0007'


;----- PIE4 Bits -----------------------------------------------------
CCP1IE           EQU  H'0000'
CCP2IE           EQU  H'0001'
CCP3IE           EQU  H'0002'
CCP4IE           EQU  H'0003'
TMR5IE           EQU  H'0004'
TMR5GIE          EQU  H'0005'
CWG1IE           EQU  H'0006'
CWG2IE           EQU  H'0007'


;----- WDTCON Bits -----------------------------------------------------
SWDTEN           EQU  H'0000'

WDTPS0           EQU  H'0001'
WDTPS1           EQU  H'0002'
WDTPS2           EQU  H'0003'
WDTPS3           EQU  H'0004'
WDTPS4           EQU  H'0005'


;----- ADCON0 Bits -----------------------------------------------------
ADON             EQU  H'0000'
GO_NOT_DONE      EQU  H'0001'

ADGO             EQU  H'0001'
CHS0             EQU  H'0002'
CHS1             EQU  H'0003'
CHS2             EQU  H'0004'
CHS3             EQU  H'0005'
CHS4             EQU  H'0006'
CHS5             EQU  H'0007'

GO               EQU  H'0001'


;----- ADCON1 Bits -----------------------------------------------------
ADNREF           EQU  H'0002'
ADFM             EQU  H'0007'

ADPREF0          EQU  H'0000'
ADPREF1          EQU  H'0001'
ADCS0            EQU  H'0004'
ADCS1            EQU  H'0005'
ADCS2            EQU  H'0006'


;----- ADACT Bits -----------------------------------------------------
ADACT0           EQU  H'0000'
ADACT1           EQU  H'0001'
ADACT2           EQU  H'0002'
ADACT3           EQU  H'0003'
ADACT4           EQU  H'0004'


;----- LATA Bits -----------------------------------------------------
LATA0            EQU  H'0000'
LATA1            EQU  H'0001'
LATA2            EQU  H'0002'
LATA4            EQU  H'0004'
LATA5            EQU  H'0005'


;----- LATC Bits -----------------------------------------------------
LATC0            EQU  H'0000'
LATC1            EQU  H'0001'
LATC2            EQU  H'0002'
LATC3            EQU  H'0003'
LATC4            EQU  H'0004'
LATC5            EQU  H'0005'


;----- CM1CON0 Bits -----------------------------------------------------
C1SYNC           EQU  H'0000'
C1HYS            EQU  H'0001'
C1SP             EQU  H'0002'
C1POL            EQU  H'0004'
C1OUT            EQU  H'0006'
C1ON             EQU  H'0007'


;----- CM1CON1 Bits -----------------------------------------------------
C1INTN           EQU  H'0006'
C1INTP           EQU  H'0007'

C1NCH0           EQU  H'0000'
C1NCH1           EQU  H'0001'
C1NCH2           EQU  H'0002'
C1PCH0           EQU  H'0003'
C1PCH1           EQU  H'0004'
C1PCH2           EQU  H'0005'


;----- CM2CON0 Bits -----------------------------------------------------
C2SYNC           EQU  H'0000'
C2HYS            EQU  H'0001'
C2SP             EQU  H'0002'
C2POL            EQU  H'0004'
C2OUT            EQU  H'0006'
C2ON             EQU  H'0007'


;----- CM2CON1 Bits -----------------------------------------------------
C2INTN           EQU  H'0006'
C2INTP           EQU  H'0007'

C2NCH0           EQU  H'0000'
C2NCH1           EQU  H'0001'
C2NCH2           EQU  H'0002'
C2PCH0           EQU  H'0003'
C2PCH1           EQU  H'0004'
C2PCH2           EQU  H'0005'


;----- CMOUT Bits -----------------------------------------------------
MC1OUT           EQU  H'0000'
MC2OUT           EQU  H'0001'


;----- BORCON Bits -----------------------------------------------------
BORRDY           EQU  H'0000'
SBOREN           EQU  H'0007'


;----- FVRCON Bits -----------------------------------------------------
TSRNG            EQU  H'0004'
TSEN             EQU  H'0005'
FVRRDY           EQU  H'0006'
FVREN            EQU  H'0007'

ADFVR0           EQU  H'0000'
ADFVR1           EQU  H'0001'
CDAFVR0          EQU  H'0002'
CDAFVR1          EQU  H'0003'


;----- DACCON0 Bits -----------------------------------------------------
DAC1NSS          EQU  H'0000'
DAC1OE           EQU  H'0005'
DAC1EN           EQU  H'0007'

DAC1PSS0         EQU  H'0002'
DAC1PSS1         EQU  H'0003'


;----- DACCON1 Bits -----------------------------------------------------
DAC1R0           EQU  H'0000'
DAC1R1           EQU  H'0001'
DAC1R2           EQU  H'0002'
DAC1R3           EQU  H'0003'
DAC1R4           EQU  H'0004'


;----- ANSELA Bits -----------------------------------------------------
ANSA0            EQU  H'0000'
ANSA1            EQU  H'0001'
ANSA2            EQU  H'0002'
ANSA4            EQU  H'0004'
ANSA5            EQU  H'0005'


;----- ANSELC Bits -----------------------------------------------------
ANSC0            EQU  H'0000'
ANSC1            EQU  H'0001'
ANSC2            EQU  H'0002'
ANSC3            EQU  H'0003'
ANSC4            EQU  H'0004'
ANSC5            EQU  H'0005'


;----- VREGCON Bits -----------------------------------------------------
VREGPM           EQU  H'0001'


;----- RC1STA Bits -----------------------------------------------------
RX9D             EQU  H'0000'
OERR             EQU  H'0001'
FERR             EQU  H'0002'
ADDEN            EQU  H'0003'
CREN             EQU  H'0004'
SREN             EQU  H'0005'
RX9              EQU  H'0006'
SPEN             EQU  H'0007'


;----- RCSTA Bits -----------------------------------------------------
RX9D             EQU  H'0000'
OERR             EQU  H'0001'
FERR             EQU  H'0002'
ADDEN            EQU  H'0003'
CREN             EQU  H'0004'
SREN             EQU  H'0005'
RX9              EQU  H'0006'
SPEN             EQU  H'0007'


;----- RCSTA1 Bits -----------------------------------------------------
RX9D             EQU  H'0000'
OERR             EQU  H'0001'
FERR             EQU  H'0002'
ADDEN            EQU  H'0003'
CREN             EQU  H'0004'
SREN             EQU  H'0005'
RX9              EQU  H'0006'
SPEN             EQU  H'0007'


;----- TX1STA Bits -----------------------------------------------------
TX9D             EQU  H'0000'
TRMT             EQU  H'0001'
BRGH             EQU  H'0002'
SENDB            EQU  H'0003'
SYNC             EQU  H'0004'
TXEN             EQU  H'0005'
TX9              EQU  H'0006'
CSRC             EQU  H'0007'


;----- TXSTA Bits -----------------------------------------------------
TX9D             EQU  H'0000'
TRMT             EQU  H'0001'
BRGH             EQU  H'0002'
SENDB            EQU  H'0003'
SYNC             EQU  H'0004'
TXEN             EQU  H'0005'
TX9              EQU  H'0006'
CSRC             EQU  H'0007'


;----- TXSTA1 Bits -----------------------------------------------------
TX9D             EQU  H'0000'
TRMT             EQU  H'0001'
BRGH             EQU  H'0002'
SENDB            EQU  H'0003'
SYNC             EQU  H'0004'
TXEN             EQU  H'0005'
TX9              EQU  H'0006'
CSRC             EQU  H'0007'


;----- BAUD1CON Bits -----------------------------------------------------
ABDEN            EQU  H'0000'
WUE              EQU  H'0001'
BRG16            EQU  H'0003'
SCKP             EQU  H'0004'
RCIDL            EQU  H'0006'
ABDOVF           EQU  H'0007'


;----- BAUDCON Bits -----------------------------------------------------
ABDEN            EQU  H'0000'
WUE              EQU  H'0001'
BRG16            EQU  H'0003'
SCKP             EQU  H'0004'
RCIDL            EQU  H'0006'
ABDOVF           EQU  H'0007'


;----- BAUDCON1 Bits -----------------------------------------------------
ABDEN            EQU  H'0000'
WUE              EQU  H'0001'
BRG16            EQU  H'0003'
SCKP             EQU  H'0004'
RCIDL            EQU  H'0006'
ABDOVF           EQU  H'0007'


;----- BAUDCTL Bits -----------------------------------------------------
ABDEN            EQU  H'0000'
WUE              EQU  H'0001'
BRG16            EQU  H'0003'
SCKP             EQU  H'0004'
RCIDL            EQU  H'0006'
ABDOVF           EQU  H'0007'


;----- BAUDCTL1 Bits -----------------------------------------------------
ABDEN            EQU  H'0000'
WUE              EQU  H'0001'
BRG16            EQU  H'0003'
SCKP             EQU  H'0004'
RCIDL            EQU  H'0006'
ABDOVF           EQU  H'0007'


;----- WPUA Bits -----------------------------------------------------
WPUA0            EQU  H'0000'
WPUA1            EQU  H'0001'
WPUA2            EQU  H'0002'
WPUA3            EQU  H'0003'
WPUA4            EQU  H'0004'
WPUA5            EQU  H'0005'


;----- WPUC Bits -----------------------------------------------------
WPUC0            EQU  H'0000'
WPUC1            EQU  H'0001'
WPUC2            EQU  H'0002'
WPUC3            EQU  H'0003'
WPUC4            EQU  H'0004'
WPUC5            EQU  H'0005'


;----- SSP1BUF Bits -----------------------------------------------------
SSP1BUF0         EQU  H'0000'
SSP1BUF1         EQU  H'0001'
SSP1BUF2         EQU  H'0002'
SSP1BUF3         EQU  H'0003'
SSP1BUF4         EQU  H'0004'
SSP1BUF5         EQU  H'0005'
SSP1BUF6         EQU  H'0006'
SSP1BUF7         EQU  H'0007'


BUF0             EQU  H'0000'
BUF1             EQU  H'0001'
BUF2             EQU  H'0002'
BUF3             EQU  H'0003'
BUF4             EQU  H'0004'
BUF5             EQU  H'0005'
BUF6             EQU  H'0006'
BUF7             EQU  H'0007'



;----- SSPBUF Bits -----------------------------------------------------
SSP1BUF0         EQU  H'0000'
SSP1BUF1         EQU  H'0001'
SSP1BUF2         EQU  H'0002'
SSP1BUF3         EQU  H'0003'
SSP1BUF4         EQU  H'0004'
SSP1BUF5         EQU  H'0005'
SSP1BUF6         EQU  H'0006'
SSP1BUF7         EQU  H'0007'


BUF0             EQU  H'0000'
BUF1             EQU  H'0001'
BUF2             EQU  H'0002'
BUF3             EQU  H'0003'
BUF4             EQU  H'0004'
BUF5             EQU  H'0005'
BUF6             EQU  H'0006'
BUF7             EQU  H'0007'



;----- SSP1ADD Bits -----------------------------------------------------
SSP1ADD0         EQU  H'0000'
SSP1ADD1         EQU  H'0001'
SSP1ADD2         EQU  H'0002'
SSP1ADD3         EQU  H'0003'
SSP1ADD4         EQU  H'0004'
SSP1ADD5         EQU  H'0005'
SSP1ADD6         EQU  H'0006'
SSP1ADD7         EQU  H'0007'


ADD0             EQU  H'0000'
ADD1             EQU  H'0001'
ADD2             EQU  H'0002'
ADD3             EQU  H'0003'
ADD4             EQU  H'0004'
ADD5             EQU  H'0005'
ADD6             EQU  H'0006'
ADD7             EQU  H'0007'



;----- SSPADD Bits -----------------------------------------------------
SSP1ADD0         EQU  H'0000'
SSP1ADD1         EQU  H'0001'
SSP1ADD2         EQU  H'0002'
SSP1ADD3         EQU  H'0003'
SSP1ADD4         EQU  H'0004'
SSP1ADD5         EQU  H'0005'
SSP1ADD6         EQU  H'0006'
SSP1ADD7         EQU  H'0007'


ADD0             EQU  H'0000'
ADD1             EQU  H'0001'
ADD2             EQU  H'0002'
ADD3             EQU  H'0003'
ADD4             EQU  H'0004'
ADD5             EQU  H'0005'
ADD6             EQU  H'0006'
ADD7             EQU  H'0007'



;----- SSP1MSK Bits -----------------------------------------------------
SSP1MSK0         EQU  H'0000'
SSP1MSK1         EQU  H'0001'
SSP1MSK2         EQU  H'0002'
SSP1MSK3         EQU  H'0003'
SSP1MSK4         EQU  H'0004'
SSP1MSK5         EQU  H'0005'
SSP1MSK6         EQU  H'0006'
SSP1MSK7         EQU  H'0007'


MSK0             EQU  H'0000'
MSK1             EQU  H'0001'
MSK2             EQU  H'0002'
MSK3             EQU  H'0003'
MSK4             EQU  H'0004'
MSK5             EQU  H'0005'
MSK6             EQU  H'0006'
MSK7             EQU  H'0007'



;----- SSPMSK Bits -----------------------------------------------------
SSP1MSK0         EQU  H'0000'
SSP1MSK1         EQU  H'0001'
SSP1MSK2         EQU  H'0002'
SSP1MSK3         EQU  H'0003'
SSP1MSK4         EQU  H'0004'
SSP1MSK5         EQU  H'0005'
SSP1MSK6         EQU  H'0006'
SSP1MSK7         EQU  H'0007'


MSK0             EQU  H'0000'
MSK1             EQU  H'0001'
MSK2             EQU  H'0002'
MSK3             EQU  H'0003'
MSK4             EQU  H'0004'
MSK5             EQU  H'0005'
MSK6             EQU  H'0006'
MSK7             EQU  H'0007'



;----- SSP1STAT Bits -----------------------------------------------------
BF               EQU  H'0000'
UA               EQU  H'0001'
R_NOT_W          EQU  H'0002'
S                EQU  H'0003'
P                EQU  H'0004'
D_NOT_A          EQU  H'0005'
CKE              EQU  H'0006'
SMP              EQU  H'0007'


;----- SSPSTAT Bits -----------------------------------------------------
BF               EQU  H'0000'
UA               EQU  H'0001'
R_NOT_W          EQU  H'0002'
S                EQU  H'0003'
P                EQU  H'0004'
D_NOT_A          EQU  H'0005'
CKE              EQU  H'0006'
SMP              EQU  H'0007'


;----- SSP1CON Bits -----------------------------------------------------
CKP              EQU  H'0004'
SSPEN            EQU  H'0005'
SSPOV            EQU  H'0006'
WCOL             EQU  H'0007'

SSPM0            EQU  H'0000'
SSPM1            EQU  H'0001'
SSPM2            EQU  H'0002'
SSPM3            EQU  H'0003'


;----- SSP1CON1 Bits -----------------------------------------------------
CKP              EQU  H'0004'
SSPEN            EQU  H'0005'
SSPOV            EQU  H'0006'
WCOL             EQU  H'0007'

SSPM0            EQU  H'0000'
SSPM1            EQU  H'0001'
SSPM2            EQU  H'0002'
SSPM3            EQU  H'0003'


;----- SSPCON Bits -----------------------------------------------------
CKP              EQU  H'0004'
SSPEN            EQU  H'0005'
SSPOV            EQU  H'0006'
WCOL             EQU  H'0007'

SSPM0            EQU  H'0000'
SSPM1            EQU  H'0001'
SSPM2            EQU  H'0002'
SSPM3            EQU  H'0003'


;----- SSPCON1 Bits -----------------------------------------------------
CKP              EQU  H'0004'
SSPEN            EQU  H'0005'
SSPOV            EQU  H'0006'
WCOL             EQU  H'0007'

SSPM0            EQU  H'0000'
SSPM1            EQU  H'0001'
SSPM2            EQU  H'0002'
SSPM3            EQU  H'0003'


;----- SSP1CON2 Bits -----------------------------------------------------
SEN              EQU  H'0000'
RSEN             EQU  H'0001'
PEN              EQU  H'0002'
RCEN             EQU  H'0003'
ACKEN            EQU  H'0004'
ACKDT            EQU  H'0005'
ACKSTAT          EQU  H'0006'
GCEN             EQU  H'0007'


;----- SSPCON2 Bits -----------------------------------------------------
SEN              EQU  H'0000'
RSEN             EQU  H'0001'
PEN              EQU  H'0002'
RCEN             EQU  H'0003'
ACKEN            EQU  H'0004'
ACKDT            EQU  H'0005'
ACKSTAT          EQU  H'0006'
GCEN             EQU  H'0007'


;----- SSP1CON3 Bits -----------------------------------------------------
DHEN             EQU  H'0000'
AHEN             EQU  H'0001'
SBCDE            EQU  H'0002'
SDAHT            EQU  H'0003'
BOEN             EQU  H'0004'
SCIE             EQU  H'0005'
PCIE             EQU  H'0006'
ACKTIM           EQU  H'0007'


;----- SSPCON3 Bits -----------------------------------------------------
DHEN             EQU  H'0000'
AHEN             EQU  H'0001'
SBCDE            EQU  H'0002'
SDAHT            EQU  H'0003'
BOEN             EQU  H'0004'
SCIE             EQU  H'0005'
PCIE             EQU  H'0006'
ACKTIM           EQU  H'0007'


;----- SSP2BUF Bits -----------------------------------------------------
SSP2BUF0         EQU  H'0000'
SSP2BUF1         EQU  H'0001'
SSP2BUF2         EQU  H'0002'
SSP2BUF3         EQU  H'0003'
SSP2BUF4         EQU  H'0004'
SSP2BUF5         EQU  H'0005'
SSP2BUF6         EQU  H'0006'
SSP2BUF7         EQU  H'0007'


BUF0             EQU  H'0000'
BUF1             EQU  H'0001'
BUF2             EQU  H'0002'
BUF3             EQU  H'0003'
BUF4             EQU  H'0004'
BUF5             EQU  H'0005'
BUF6             EQU  H'0006'
BUF7             EQU  H'0007'



;----- SSP2ADD Bits -----------------------------------------------------
SSP2ADD0         EQU  H'0000'
SSP2ADD1         EQU  H'0001'
SSP2ADD2         EQU  H'0002'
SSP2ADD3         EQU  H'0003'
SSP2ADD4         EQU  H'0004'
SSP2ADD5         EQU  H'0005'
SSP2ADD6         EQU  H'0006'
SSP2ADD7         EQU  H'0007'


ADD0             EQU  H'0000'
ADD1             EQU  H'0001'
ADD2             EQU  H'0002'
ADD3             EQU  H'0003'
ADD4             EQU  H'0004'
ADD5             EQU  H'0005'
ADD6             EQU  H'0006'
ADD7             EQU  H'0007'



;----- SSP2MSK Bits -----------------------------------------------------
SSP2MSK0         EQU  H'0000'
SSP2MSK1         EQU  H'0001'
SSP2MSK2         EQU  H'0002'
SSP2MSK3         EQU  H'0003'
SSP2MSK4         EQU  H'0004'
SSP2MSK5         EQU  H'0005'
SSP2MSK6         EQU  H'0006'
SSP2MSK7         EQU  H'0007'


MSK0             EQU  H'0000'
MSK1             EQU  H'0001'
MSK2             EQU  H'0002'
MSK3             EQU  H'0003'
MSK4             EQU  H'0004'
MSK5             EQU  H'0005'
MSK6             EQU  H'0006'
MSK7             EQU  H'0007'



;----- SSP2STAT Bits -----------------------------------------------------
BF               EQU  H'0000'
UA               EQU  H'0001'
R_NOT_W          EQU  H'0002'
S                EQU  H'0003'
P                EQU  H'0004'
D_NOT_A          EQU  H'0005'
CKE              EQU  H'0006'
SMP              EQU  H'0007'


;----- SSP2CON Bits -----------------------------------------------------
CKP              EQU  H'0004'
SSPEN            EQU  H'0005'
SSPOV            EQU  H'0006'
WCOL             EQU  H'0007'

SSPM0            EQU  H'0000'
SSPM1            EQU  H'0001'
SSPM2            EQU  H'0002'
SSPM3            EQU  H'0003'


;----- SSP2CON1 Bits -----------------------------------------------------
CKP              EQU  H'0004'
SSPEN            EQU  H'0005'
SSPOV            EQU  H'0006'
WCOL             EQU  H'0007'

SSPM0            EQU  H'0000'
SSPM1            EQU  H'0001'
SSPM2            EQU  H'0002'
SSPM3            EQU  H'0003'


;----- SSP2CON2 Bits -----------------------------------------------------
SEN              EQU  H'0000'
RSEN             EQU  H'0001'
PEN              EQU  H'0002'
RCEN             EQU  H'0003'
ACKEN            EQU  H'0004'
ACKDT            EQU  H'0005'
ACKSTAT          EQU  H'0006'
GCEN             EQU  H'0007'


;----- SSP2CON3 Bits -----------------------------------------------------
DHEN             EQU  H'0000'
AHEN             EQU  H'0001'
SBCDE            EQU  H'0002'
SDAHT            EQU  H'0003'
BOEN             EQU  H'0004'
SCIE             EQU  H'0005'
PCIE             EQU  H'0006'
ACKTIM           EQU  H'0007'


;----- ODCONA Bits -----------------------------------------------------
ODCA0            EQU  H'0000'
ODCA1            EQU  H'0001'
ODCA2            EQU  H'0002'
ODCA4            EQU  H'0004'
ODCA5            EQU  H'0005'


;----- ODCONC Bits -----------------------------------------------------
ODCC0            EQU  H'0000'
ODCC1            EQU  H'0001'
ODCC2            EQU  H'0002'
ODCC3            EQU  H'0003'
ODCC4            EQU  H'0004'
ODCC5            EQU  H'0005'


;----- CCP1CON Bits -----------------------------------------------------
CCP1FMT          EQU  H'0004'
CCP1OUT          EQU  H'0005'
CCP1EN           EQU  H'0007'

CCP1MODE0        EQU  H'0000'
CCP1MODE1        EQU  H'0001'
CCP1MODE2        EQU  H'0002'
CCP1MODE3        EQU  H'0003'


;----- CCP1CAP Bits -----------------------------------------------------
CCP1CTS0         EQU  H'0000'
CCP1CTS1         EQU  H'0001'
CCP1CTS2         EQU  H'0002'
CCP1CTS3         EQU  H'0003'


;----- CCP2CON Bits -----------------------------------------------------
CCP2FMT          EQU  H'0004'
CCP2OUT          EQU  H'0005'
CCP2EN           EQU  H'0007'

CCP2MODE0        EQU  H'0000'
CCP2MODE1        EQU  H'0001'
CCP2MODE2        EQU  H'0002'
CCP2MODE3        EQU  H'0003'


;----- CCP2CAP Bits -----------------------------------------------------
CCP2CTS0         EQU  H'0000'
CCP2CTS1         EQU  H'0001'
CCP2CTS2         EQU  H'0002'
CCP2CTS3         EQU  H'0003'


;----- CCPTMRS Bits -----------------------------------------------------
C1TSEL0          EQU  H'0000'
C1TSEL1          EQU  H'0001'
C2TSEL0          EQU  H'0002'
C2TSEL1          EQU  H'0003'
C3TSEL0          EQU  H'0004'
C3TSEL1          EQU  H'0005'
C4TSEL0          EQU  H'0006'
C4TSEL1          EQU  H'0007'


;----- SLRCONA Bits -----------------------------------------------------
SLRA0            EQU  H'0000'
SLRA1            EQU  H'0001'
SLRA2            EQU  H'0002'
SLRA4            EQU  H'0004'
SLRA5            EQU  H'0005'


;----- SLRCONC Bits -----------------------------------------------------
SLRC0            EQU  H'0000'
SLRC1            EQU  H'0001'
SLRC2            EQU  H'0002'
SLRC3            EQU  H'0003'
SLRC4            EQU  H'0004'
SLRC5            EQU  H'0005'


;----- CCP3CON Bits -----------------------------------------------------
CCP3FMT          EQU  H'0004'
CCP3OUT          EQU  H'0005'
CCP3EN           EQU  H'0007'

CCP3MODE0        EQU  H'0000'
CCP3MODE1        EQU  H'0001'
CCP3MODE2        EQU  H'0002'
CCP3MODE3        EQU  H'0003'


;----- CCP3CAP Bits -----------------------------------------------------
CCP3CTS0         EQU  H'0000'
CCP3CTS1         EQU  H'0001'
CCP3CTS2         EQU  H'0002'
CCP3CTS3         EQU  H'0003'


;----- CCP4CON Bits -----------------------------------------------------
CCP4FMT          EQU  H'0004'
CCP4OUT          EQU  H'0005'
CCP4EN           EQU  H'0007'

CCP4MODE0        EQU  H'0000'
CCP4MODE1        EQU  H'0001'
CCP4MODE2        EQU  H'0002'
CCP4MODE3        EQU  H'0003'


;----- CCP4CAP Bits -----------------------------------------------------
CCP4CTS0         EQU  H'0000'
CCP4CTS1         EQU  H'0001'
CCP4CTS2         EQU  H'0002'
CCP4CTS3         EQU  H'0003'


;----- INLVLA Bits -----------------------------------------------------
INLVLA0          EQU  H'0000'
INLVLA1          EQU  H'0001'
INLVLA2          EQU  H'0002'
INLVLA3          EQU  H'0003'
INLVLA4          EQU  H'0004'
INLVLA5          EQU  H'0005'


;----- INLVLC Bits -----------------------------------------------------
INLVLC0          EQU  H'0000'
INLVLC1          EQU  H'0001'
INLVLC2          EQU  H'0002'
INLVLC3          EQU  H'0003'
INLVLC4          EQU  H'0004'
INLVLC5          EQU  H'0005'


;----- IOCAP Bits -----------------------------------------------------
IOCAP0           EQU  H'0000'
IOCAP1           EQU  H'0001'
IOCAP2           EQU  H'0002'
IOCAP3           EQU  H'0003'
IOCAP4           EQU  H'0004'
IOCAP5           EQU  H'0005'


;----- IOCAN Bits -----------------------------------------------------
IOCAN0           EQU  H'0000'
IOCAN1           EQU  H'0001'
IOCAN2           EQU  H'0002'
IOCAN3           EQU  H'0003'
IOCAN4           EQU  H'0004'
IOCAN5           EQU  H'0005'


;----- IOCAF Bits -----------------------------------------------------
IOCAF0           EQU  H'0000'
IOCAF1           EQU  H'0001'
IOCAF2           EQU  H'0002'
IOCAF3           EQU  H'0003'
IOCAF4           EQU  H'0004'
IOCAF5           EQU  H'0005'


;----- IOCCP Bits -----------------------------------------------------
IOCCP0           EQU  H'0000'
IOCCP1           EQU  H'0001'
IOCCP2           EQU  H'0002'
IOCCP3           EQU  H'0003'
IOCCP4           EQU  H'0004'
IOCCP5           EQU  H'0005'


;----- IOCCN Bits -----------------------------------------------------
IOCCN0           EQU  H'0000'
IOCCN1           EQU  H'0001'
IOCCN2           EQU  H'0002'
IOCCN3           EQU  H'0003'
IOCCN4           EQU  H'0004'
IOCCN5           EQU  H'0005'


;----- IOCCF Bits -----------------------------------------------------
IOCCF0           EQU  H'0000'
IOCCF1           EQU  H'0001'
IOCCF2           EQU  H'0002'
IOCCF3           EQU  H'0003'
IOCCF4           EQU  H'0004'
IOCCF5           EQU  H'0005'


;----- CLKRCON Bits -----------------------------------------------------
CLKREN           EQU  H'0007'

CLKRDIV0         EQU  H'0000'
CLKRDIV1         EQU  H'0001'
CLKRDIV2         EQU  H'0002'
CLKRDC0          EQU  H'0003'
CLKRDC1          EQU  H'0004'


;----- MDCON Bits -----------------------------------------------------
MDBIT            EQU  H'0000'
MDOUT            EQU  H'0003'
MDOPOL           EQU  H'0004'
MDEN             EQU  H'0007'


;----- MDSRC Bits -----------------------------------------------------
MDMS0            EQU  H'0000'
MDMS1            EQU  H'0001'
MDMS2            EQU  H'0002'
MDMS3            EQU  H'0003'


;----- MDCARH Bits -----------------------------------------------------
MDCHSYNC         EQU  H'0005'
MDCHPOL          EQU  H'0006'

MDCH0            EQU  H'0000'
MDCH1            EQU  H'0001'
MDCH2            EQU  H'0002'
MDCH3            EQU  H'0003'


;----- MDCARL Bits -----------------------------------------------------
MDCLSYNC         EQU  H'0005'
MDCLPOL          EQU  H'0006'

MDCL0            EQU  H'0000'
MDCL1            EQU  H'0001'
MDCL2            EQU  H'0002'
MDCL3            EQU  H'0003'


;----- T3CON Bits -----------------------------------------------------
TMR3ON           EQU  H'0000'
T3SYNC           EQU  H'0002'
T3SOSC           EQU  H'0003'

T3CKPS0          EQU  H'0004'
T3CKPS1          EQU  H'0005'
TMR3CS0          EQU  H'0006'
TMR3CS1          EQU  H'0007'


;----- T3GCON Bits -----------------------------------------------------
T3GVAL           EQU  H'0002'
T3GGO_NOT_DONE   EQU  H'0003'
T3GSPM           EQU  H'0004'
T3GTM            EQU  H'0005'
T3GPOL           EQU  H'0006'
TMR3GE           EQU  H'0007'

T3GSS0           EQU  H'0000'
T3GSS1           EQU  H'0001'


;----- T4CON Bits -----------------------------------------------------
TMR4ON           EQU  H'0002'

T4CKPS0          EQU  H'0000'
T4CKPS1          EQU  H'0001'
T4OUTPS0         EQU  H'0003'
T4OUTPS1         EQU  H'0004'
T4OUTPS2         EQU  H'0005'
T4OUTPS3         EQU  H'0006'


;----- T5CON Bits -----------------------------------------------------
TMR5ON           EQU  H'0000'
T5SYNC           EQU  H'0002'
T5SOSC           EQU  H'0003'

T5CKPS0          EQU  H'0004'
T5CKPS1          EQU  H'0005'
TMR5CS0          EQU  H'0006'
TMR5CS1          EQU  H'0007'


;----- T5GCON Bits -----------------------------------------------------
T5GVAL           EQU  H'0002'
T5GGO_NOT_DONE   EQU  H'0003'
T5GSPM           EQU  H'0004'
T5GTM            EQU  H'0005'
T5GPOL           EQU  H'0006'
TMR5GE           EQU  H'0007'

T5GSS0           EQU  H'0000'
T5GSS1           EQU  H'0001'


;----- T6CON Bits -----------------------------------------------------
TMR6ON           EQU  H'0002'

T6CKPS0          EQU  H'0000'
T6CKPS1          EQU  H'0001'
T6OUTPS0         EQU  H'0003'
T6OUTPS1         EQU  H'0004'
T6OUTPS2         EQU  H'0005'
T6OUTPS3         EQU  H'0006'


;----- CCDCON Bits -----------------------------------------------------
CCDEN            EQU  H'0007'

CCDS0            EQU  H'0000'
CCDS1            EQU  H'0001'


;----- NCO1CON Bits -----------------------------------------------------
N1PFM            EQU  H'0000'
N1POL            EQU  H'0004'
N1OUT            EQU  H'0005'
N1EN             EQU  H'0007'


;----- PWM5DCL Bits -----------------------------------------------------
PWM5DCL0         EQU  H'0006'
PWM5DCL1         EQU  H'0007'


;----- PWM5DCH Bits -----------------------------------------------------
PWM5DCH0         EQU  H'0000'
PWM5DCH1         EQU  H'0001'
PWM5DCH2         EQU  H'0002'
PWM5DCH3         EQU  H'0003'
PWM5DCH4         EQU  H'0004'
PWM5DCH5         EQU  H'0005'
PWM5DCH6         EQU  H'0006'
PWM5DCH7         EQU  H'0007'


;----- PWM5CON Bits -----------------------------------------------------
PWM5POL          EQU  H'0004'
PWM5OUT          EQU  H'0005'
PWM5EN           EQU  H'0007'


;----- PWM5CON0 Bits -----------------------------------------------------
PWM5POL          EQU  H'0004'
PWM5OUT          EQU  H'0005'
PWM5EN           EQU  H'0007'


;----- PWM6DCL Bits -----------------------------------------------------
PWM6DCL0         EQU  H'0006'
PWM6DCL1         EQU  H'0007'


;----- PWM6DCH Bits -----------------------------------------------------
PWM6DCH0         EQU  H'0000'
PWM6DCH1         EQU  H'0001'
PWM6DCH2         EQU  H'0002'
PWM6DCH3         EQU  H'0003'
PWM6DCH4         EQU  H'0004'
PWM6DCH5         EQU  H'0005'
PWM6DCH6         EQU  H'0006'
PWM6DCH7         EQU  H'0007'


;----- PWM6CON Bits -----------------------------------------------------
PWM6POL          EQU  H'0004'
PWM6OUT          EQU  H'0005'
PWM6EN           EQU  H'0007'


;----- PWM6CON0 Bits -----------------------------------------------------
PWM6POL          EQU  H'0004'
PWM6OUT          EQU  H'0005'
PWM6EN           EQU  H'0007'


;----- PWMTMRS Bits -----------------------------------------------------
P5TSEL0          EQU  H'0000'
P5TSEL1          EQU  H'0001'
P6TSEL0          EQU  H'0002'
P6TSEL1          EQU  H'0003'


;----- CWG1CLKCON Bits -----------------------------------------------------
CS               EQU  H'0000'

CWG1CS           EQU  H'0000'


;----- CWG1DAT Bits -----------------------------------------------------
CWG1DAT0         EQU  H'0000'
CWG1DAT1         EQU  H'0001'
CWG1DAT2         EQU  H'0002'
CWG1DAT3         EQU  H'0003'


;----- CWG1DBR Bits -----------------------------------------------------
DBR0             EQU  H'0000'
DBR1             EQU  H'0001'
DBR2             EQU  H'0002'
DBR3             EQU  H'0003'
DBR4             EQU  H'0004'
DBR5             EQU  H'0005'


CWG1DBR0         EQU  H'0000'
CWG1DBR1         EQU  H'0001'
CWG1DBR2         EQU  H'0002'
CWG1DBR3         EQU  H'0003'
CWG1DBR4         EQU  H'0004'
CWG1DBR5         EQU  H'0005'


;----- CWG1DBF Bits -----------------------------------------------------
DBF0             EQU  H'0000'
DBF1             EQU  H'0001'
DBF2             EQU  H'0002'
DBF3             EQU  H'0003'
DBF4             EQU  H'0004'
DBF5             EQU  H'0005'


CWG1DBF0         EQU  H'0000'
CWG1DBF1         EQU  H'0001'
CWG1DBF2         EQU  H'0002'
CWG1DBF3         EQU  H'0003'
CWG1DBF4         EQU  H'0004'
CWG1DBF5         EQU  H'0005'


;----- CWG1CON0 Bits -----------------------------------------------------
LD               EQU  H'0006'
EN               EQU  H'0007'

MODE0            EQU  H'0000'
MODE1            EQU  H'0001'
MODE2            EQU  H'0002'
G1EN             EQU  H'0007'

CWG1LD           EQU  H'0006'
CWG1EN           EQU  H'0007'

CWG1MODE0        EQU  H'0000'
CWG1MODE1        EQU  H'0001'
CWG1MODE2        EQU  H'0002'


;----- CWG1CON1 Bits -----------------------------------------------------
POLA             EQU  H'0000'
POLB             EQU  H'0001'
POLC             EQU  H'0002'
POLD             EQU  H'0003'
IN               EQU  H'0005'

CWG1POLA         EQU  H'0000'
CWG1POLB         EQU  H'0001'
CWG1POLC         EQU  H'0002'
CWG1POLD         EQU  H'0003'
CWG1IN           EQU  H'0005'


;----- CWG1AS0 Bits -----------------------------------------------------
REN              EQU  H'0006'
SHUTDOWN         EQU  H'0007'

LSAC0            EQU  H'0002'
LSAC1            EQU  H'0003'
LSBD0            EQU  H'0004'
LSBD1            EQU  H'0005'

CWG1REN          EQU  H'0006'
CWG1SHUTDOWN     EQU  H'0007'

CWG1LSAC0        EQU  H'0002'
CWG1LSAC1        EQU  H'0003'
CWG1LSBD0        EQU  H'0004'
CWG1LSBD1        EQU  H'0005'


;----- CWG1AS1 Bits -----------------------------------------------------
AS0E             EQU  H'0000'
AS1E             EQU  H'0001'
AS2E             EQU  H'0002'
AS3E             EQU  H'0003'
AS4E             EQU  H'0004'


;----- CWG1STR Bits -----------------------------------------------------
STRA             EQU  H'0000'
STRB             EQU  H'0001'
STRC             EQU  H'0002'
STRD             EQU  H'0003'
OVRA             EQU  H'0004'
OVRB             EQU  H'0005'
OVRC             EQU  H'0006'
OVRD             EQU  H'0007'

CWG1STRA         EQU  H'0000'
CWG1STRB         EQU  H'0001'
CWG1STRC         EQU  H'0002'
CWG1STRD         EQU  H'0003'
CWG1OVRA         EQU  H'0004'
CWG1OVRB         EQU  H'0005'
CWG1OVRC         EQU  H'0006'
CWG1OVRD         EQU  H'0007'


;----- CWG2CLKCON Bits -----------------------------------------------------
CS               EQU  H'0000'

CWG2CS           EQU  H'0000'


;----- CWG2DAT Bits -----------------------------------------------------
CWG2DAT0         EQU  H'0000'
CWG2DAT1         EQU  H'0001'
CWG2DAT2         EQU  H'0002'
CWG2DAT3         EQU  H'0003'


;----- CWG2DBR Bits -----------------------------------------------------
DBR0             EQU  H'0000'
DBR1             EQU  H'0001'
DBR2             EQU  H'0002'
DBR3             EQU  H'0003'
DBR4             EQU  H'0004'
DBR5             EQU  H'0005'


CWG2DBR0         EQU  H'0000'
CWG2DBR1         EQU  H'0001'
CWG2DBR2         EQU  H'0002'
CWG2DBR3         EQU  H'0003'
CWG2DBR4         EQU  H'0004'
CWG2DBR5         EQU  H'0005'


;----- CWG2DBF Bits -----------------------------------------------------
DBF0             EQU  H'0000'
DBF1             EQU  H'0001'
DBF2             EQU  H'0002'
DBF3             EQU  H'0003'
DBF4             EQU  H'0004'
DBF5             EQU  H'0005'


CWG2DBF0         EQU  H'0000'
CWG2DBF1         EQU  H'0001'
CWG2DBF2         EQU  H'0002'
CWG2DBF3         EQU  H'0003'
CWG2DBF4         EQU  H'0004'
CWG2DBF5         EQU  H'0005'


;----- CWG2CON0 Bits -----------------------------------------------------
LD               EQU  H'0006'
EN               EQU  H'0007'

MODE0            EQU  H'0000'
MODE1            EQU  H'0001'
MODE2            EQU  H'0002'
G2EN             EQU  H'0007'

CWG2LD           EQU  H'0006'
CWG2EN           EQU  H'0007'

CWG2MODE0        EQU  H'0000'
CWG2MODE1        EQU  H'0001'
CWG2MODE2        EQU  H'0002'


;----- CWG2CON1 Bits -----------------------------------------------------
POLA             EQU  H'0000'
POLB             EQU  H'0001'
POLC             EQU  H'0002'
POLD             EQU  H'0003'
IN               EQU  H'0005'

CWG2POLA         EQU  H'0000'
CWG2POLB         EQU  H'0001'
CWG2POLC         EQU  H'0002'
CWG2POLD         EQU  H'0003'
CWG2IN           EQU  H'0005'


;----- CWG2AS0 Bits -----------------------------------------------------
REN              EQU  H'0006'
SHUTDOWN         EQU  H'0007'

LSAC0            EQU  H'0002'
LSAC1            EQU  H'0003'
LSBD0            EQU  H'0004'
LSBD1            EQU  H'0005'

CWG2REN          EQU  H'0006'
CWG2SHUTDOWN     EQU  H'0007'

CWG2LSAC0        EQU  H'0002'
CWG2LSAC1        EQU  H'0003'
CWG2LSBD0        EQU  H'0004'
CWG2LSBD1        EQU  H'0005'


;----- CWG2AS1 Bits -----------------------------------------------------
AS0E             EQU  H'0000'
AS1E             EQU  H'0001'
AS2E             EQU  H'0002'
AS3E             EQU  H'0003'
AS4E             EQU  H'0004'


;----- CWG2STR Bits -----------------------------------------------------
STRA             EQU  H'0000'
STRB             EQU  H'0001'
STRC             EQU  H'0002'
STRD             EQU  H'0003'
OVRA             EQU  H'0004'
OVRB             EQU  H'0005'
OVRC             EQU  H'0006'
OVRD             EQU  H'0007'

CWG2STRA         EQU  H'0000'
CWG2STRB         EQU  H'0001'
CWG2STRC         EQU  H'0002'
CWG2STRD         EQU  H'0003'
CWG2OVRA         EQU  H'0004'
CWG2OVRB         EQU  H'0005'
CWG2OVRC         EQU  H'0006'
CWG2OVRD         EQU  H'0007'


;----- EEADRL Bits -----------------------------------------------------
NVMADR0          EQU  H'0000'
NVMADR1          EQU  H'0001'
NVMADR2          EQU  H'0002'
NVMADR3          EQU  H'0003'
NVMADR4          EQU  H'0004'
NVMADR5          EQU  H'0005'
NVMADR6          EQU  H'0006'
NVMADR7          EQU  H'0007'




;----- NVMADRL Bits -----------------------------------------------------
NVMADR0          EQU  H'0000'
NVMADR1          EQU  H'0001'
NVMADR2          EQU  H'0002'
NVMADR3          EQU  H'0003'
NVMADR4          EQU  H'0004'
NVMADR5          EQU  H'0005'
NVMADR6          EQU  H'0006'
NVMADR7          EQU  H'0007'




;----- PMADRL Bits -----------------------------------------------------
NVMADR0          EQU  H'0000'
NVMADR1          EQU  H'0001'
NVMADR2          EQU  H'0002'
NVMADR3          EQU  H'0003'
NVMADR4          EQU  H'0004'
NVMADR5          EQU  H'0005'
NVMADR6          EQU  H'0006'
NVMADR7          EQU  H'0007'




;----- EEADRH Bits -----------------------------------------------------
NVMADR8          EQU  H'0000'
NVMADR9          EQU  H'0001'
NVMADR10         EQU  H'0002'
NVMADR11         EQU  H'0003'
NVMADR12         EQU  H'0004'
NVMADR13         EQU  H'0005'
NVMADR14         EQU  H'0006'




;----- NVMADRH Bits -----------------------------------------------------
NVMADR8          EQU  H'0000'
NVMADR9          EQU  H'0001'
NVMADR10         EQU  H'0002'
NVMADR11         EQU  H'0003'
NVMADR12         EQU  H'0004'
NVMADR13         EQU  H'0005'
NVMADR14         EQU  H'0006'




;----- PMADRH Bits -----------------------------------------------------
NVMADR8          EQU  H'0000'
NVMADR9          EQU  H'0001'
NVMADR10         EQU  H'0002'
NVMADR11         EQU  H'0003'
NVMADR12         EQU  H'0004'
NVMADR13         EQU  H'0005'
NVMADR14         EQU  H'0006'




;----- EEDATL Bits -----------------------------------------------------
NVMDAT0          EQU  H'0000'
NVMDAT1          EQU  H'0001'
NVMDAT2          EQU  H'0002'
NVMDAT3          EQU  H'0003'
NVMDAT4          EQU  H'0004'
NVMDAT5          EQU  H'0005'
NVMDAT6          EQU  H'0006'
NVMDAT7          EQU  H'0007'




;----- NVMDATL Bits -----------------------------------------------------
NVMDAT0          EQU  H'0000'
NVMDAT1          EQU  H'0001'
NVMDAT2          EQU  H'0002'
NVMDAT3          EQU  H'0003'
NVMDAT4          EQU  H'0004'
NVMDAT5          EQU  H'0005'
NVMDAT6          EQU  H'0006'
NVMDAT7          EQU  H'0007'




;----- PMDATL Bits -----------------------------------------------------
NVMDAT0          EQU  H'0000'
NVMDAT1          EQU  H'0001'
NVMDAT2          EQU  H'0002'
NVMDAT3          EQU  H'0003'
NVMDAT4          EQU  H'0004'
NVMDAT5          EQU  H'0005'
NVMDAT6          EQU  H'0006'
NVMDAT7          EQU  H'0007'




;----- EEDATH Bits -----------------------------------------------------
NVMDAT8          EQU  H'0000'
NVMDAT9          EQU  H'0001'
NVMDAT10         EQU  H'0002'
NVMDAT11         EQU  H'0003'
NVMDAT12         EQU  H'0004'
NVMDAT13         EQU  H'0005'




;----- NVMDATH Bits -----------------------------------------------------
NVMDAT8          EQU  H'0000'
NVMDAT9          EQU  H'0001'
NVMDAT10         EQU  H'0002'
NVMDAT11         EQU  H'0003'
NVMDAT12         EQU  H'0004'
NVMDAT13         EQU  H'0005'




;----- PMDATH Bits -----------------------------------------------------
NVMDAT8          EQU  H'0000'
NVMDAT9          EQU  H'0001'
NVMDAT10         EQU  H'0002'
NVMDAT11         EQU  H'0003'
NVMDAT12         EQU  H'0004'
NVMDAT13         EQU  H'0005'




;----- EECON1 Bits -----------------------------------------------------
RD               EQU  H'0000'
WR               EQU  H'0001'
WREN             EQU  H'0002'
WRERR            EQU  H'0003'
FREE             EQU  H'0004'
LWLO             EQU  H'0005'
NVMREGS          EQU  H'0006'

CFGS             EQU  H'0006'


;----- NVMCON1 Bits -----------------------------------------------------
RD               EQU  H'0000'
WR               EQU  H'0001'
WREN             EQU  H'0002'
WRERR            EQU  H'0003'
FREE             EQU  H'0004'
LWLO             EQU  H'0005'
NVMREGS          EQU  H'0006'

CFGS             EQU  H'0006'


;----- PMCON1 Bits -----------------------------------------------------
RD               EQU  H'0000'
WR               EQU  H'0001'
WREN             EQU  H'0002'
WRERR            EQU  H'0003'
FREE             EQU  H'0004'
LWLO             EQU  H'0005'
NVMREGS          EQU  H'0006'

CFGS             EQU  H'0006'


;----- PCON0 Bits -----------------------------------------------------
NOT_BOR          EQU  H'0000'
NOT_POR          EQU  H'0001'
NOT_RI           EQU  H'0002'
NOT_RMCLR        EQU  H'0003'
NOT_RWDT         EQU  H'0004'
STKUNF           EQU  H'0006'
STKOVF           EQU  H'0007'


;----- PMD0 Bits -----------------------------------------------------
IOCMD            EQU  H'0000'
CLKRMD           EQU  H'0001'
NVMMD            EQU  H'0002'
FVRMD            EQU  H'0006'
SYSCMD           EQU  H'0007'


;----- PMD1 Bits -----------------------------------------------------
TMR0MD           EQU  H'0000'
TMR1MD           EQU  H'0001'
TMR2MD           EQU  H'0002'
TMR3MD           EQU  H'0003'
TMR4MD           EQU  H'0004'
TMR5MD           EQU  H'0005'
TMR6MD           EQU  H'0006'
NCOMD            EQU  H'0007'


;----- PMD2 Bits -----------------------------------------------------
CMP1MD           EQU  H'0001'
CMP2MD           EQU  H'0002'
ADCMD            EQU  H'0005'
DACMD            EQU  H'0006'


;----- PMD3 Bits -----------------------------------------------------
CCP1MD           EQU  H'0000'
CCP2MD           EQU  H'0001'
CCP3MD           EQU  H'0002'
CCP4MD           EQU  H'0003'
PWM5MD           EQU  H'0004'
PWM6MD           EQU  H'0005'
CWG1MD           EQU  H'0006'
CWG2MD           EQU  H'0007'


;----- PMD4 Bits -----------------------------------------------------
MSSP1MD          EQU  H'0001'
MSSP2MD          EQU  H'0002'
UART1MD          EQU  H'0005'


;----- PMD5 Bits -----------------------------------------------------
DSMMD            EQU  H'0000'
CLC1MD           EQU  H'0001'
CLC2MD           EQU  H'0002'
CLC3MD           EQU  H'0003'
CLC4MD           EQU  H'0004'


;----- CPUDOZE Bits -----------------------------------------------------
DOE              EQU  H'0004'
ROI              EQU  H'0005'
DOZEN            EQU  H'0006'
IDLEN            EQU  H'0007'

DOZE0            EQU  H'0000'
DOZE1            EQU  H'0001'
DOZE2            EQU  H'0002'


;----- OSCCON1 Bits -----------------------------------------------------
NDIV0            EQU  H'0000'
NDIV1            EQU  H'0001'
NDIV2            EQU  H'0002'
NDIV3            EQU  H'0003'
NOSC0            EQU  H'0004'
NOSC1            EQU  H'0005'
NOSC2            EQU  H'0006'


;----- OSCCON2 Bits -----------------------------------------------------
CDIV0            EQU  H'0000'
CDIV1            EQU  H'0001'
CDIV2            EQU  H'0002'
CDIV3            EQU  H'0003'
COSC0            EQU  H'0004'
COSC1            EQU  H'0005'
COSC2            EQU  H'0006'


;----- OSCCON3 Bits -----------------------------------------------------
NOSCR            EQU  H'0003'
ORDY             EQU  H'0004'
SOSCBE           EQU  H'0005'
SOSCPWR          EQU  H'0006'
CSWHOLD          EQU  H'0007'


;----- OSCSTAT1 Bits -----------------------------------------------------
PLLR             EQU  H'0000'
ADOR             EQU  H'0002'
SOR              EQU  H'0003'
LFOR             EQU  H'0004'
HFOR             EQU  H'0006'
EXTOR            EQU  H'0007'


;----- OSCEN Bits -----------------------------------------------------
ADOEN            EQU  H'0002'
SOSCEN           EQU  H'0003'
LFOEN            EQU  H'0004'
HFOEN            EQU  H'0006'
EXTOEN           EQU  H'0007'


;----- OSCTUNE Bits -----------------------------------------------------
HFTUN0           EQU  H'0000'
HFTUN1           EQU  H'0001'
HFTUN2           EQU  H'0002'
HFTUN3           EQU  H'0003'
HFTUN4           EQU  H'0004'
HFTUN5           EQU  H'0005'


;----- OSCFRQ Bits -----------------------------------------------------
HFFRQ0           EQU  H'0000'
HFFRQ1           EQU  H'0001'
HFFRQ2           EQU  H'0002'
HFFRQ3           EQU  H'0003'


;----- PPSLOCK Bits -----------------------------------------------------
PPSLOCKED        EQU  H'0000'


;----- INTPPS Bits -----------------------------------------------------
INTPPS0          EQU  H'0000'
INTPPS1          EQU  H'0001'
INTPPS2          EQU  H'0002'
INTPPS3          EQU  H'0003'
INTPPS4          EQU  H'0004'


;----- T0CKIPPS Bits -----------------------------------------------------
T0CKIPPS0        EQU  H'0000'
T0CKIPPS1        EQU  H'0001'
T0CKIPPS2        EQU  H'0002'
T0CKIPPS3        EQU  H'0003'
T0CKIPPS4        EQU  H'0004'


;----- T1CKIPPS Bits -----------------------------------------------------
T1CKIPPS0        EQU  H'0000'
T1CKIPPS1        EQU  H'0001'
T1CKIPPS2        EQU  H'0002'
T1CKIPPS3        EQU  H'0003'
T1CKIPPS4        EQU  H'0004'


;----- T1GPPS Bits -----------------------------------------------------
T1GPPS0          EQU  H'0000'
T1GPPS1          EQU  H'0001'
T1GPPS2          EQU  H'0002'
T1GPPS3          EQU  H'0003'
T1GPPS4          EQU  H'0004'


;----- CCP1PPS Bits -----------------------------------------------------
CCP1PPS0         EQU  H'0000'
CCP1PPS1         EQU  H'0001'
CCP1PPS2         EQU  H'0002'
CCP1PPS3         EQU  H'0003'
CCP1PPS4         EQU  H'0004'


;----- CCP2PPS Bits -----------------------------------------------------
CCP2PPS0         EQU  H'0000'
CCP2PPS1         EQU  H'0001'
CCP2PPS2         EQU  H'0002'
CCP2PPS3         EQU  H'0003'
CCP2PPS4         EQU  H'0004'


;----- CCP3PPS Bits -----------------------------------------------------
CCP3PPS0         EQU  H'0000'
CCP3PPS1         EQU  H'0001'
CCP3PPS2         EQU  H'0002'
CCP3PPS3         EQU  H'0003'
CCP3PPS4         EQU  H'0004'


;----- CCP4PPS Bits -----------------------------------------------------
CCP4PPS0         EQU  H'0000'
CCP4PPS1         EQU  H'0001'
CCP4PPS2         EQU  H'0002'
CCP4PPS3         EQU  H'0003'
CCP4PPS4         EQU  H'0004'


;----- CWG1PPS Bits -----------------------------------------------------
CWG1PPS0         EQU  H'0000'
CWG1PPS1         EQU  H'0001'
CWG1PPS2         EQU  H'0002'
CWG1PPS3         EQU  H'0003'
CWG1PPS4         EQU  H'0004'


;----- CWG2PPS Bits -----------------------------------------------------
CWG2PPS0         EQU  H'0000'
CWG2PPS1         EQU  H'0001'
CWG2PPS2         EQU  H'0002'
CWG2PPS3         EQU  H'0003'
CWG2PPS4         EQU  H'0004'


;----- MDCIN1PPS Bits -----------------------------------------------------
MDCIN1PPS0       EQU  H'0000'
MDCIN1PPS1       EQU  H'0001'
MDCIN1PPS2       EQU  H'0002'
MDCIN1PPS3       EQU  H'0003'
MDCIN1PPS4       EQU  H'0004'


;----- MDCIN2PPS Bits -----------------------------------------------------
MDCIN2PPS0       EQU  H'0000'
MDCIN2PPS1       EQU  H'0001'
MDCIN2PPS2       EQU  H'0002'
MDCIN2PPS3       EQU  H'0003'
MDCIN2PPS4       EQU  H'0004'


;----- MDMINPPS Bits -----------------------------------------------------
MDMINPPS0        EQU  H'0000'
MDMINPPS1        EQU  H'0001'
MDMINPPS2        EQU  H'0002'
MDMINPPS3        EQU  H'0003'
MDMINPPS4        EQU  H'0004'


;----- SSP2CLKPPS Bits -----------------------------------------------------
SSP2CLKPPS0      EQU  H'0000'
SSP2CLKPPS1      EQU  H'0001'
SSP2CLKPPS2      EQU  H'0002'
SSP2CLKPPS3      EQU  H'0003'
SSP2CLKPPS4      EQU  H'0004'


;----- SSP2DATPPS Bits -----------------------------------------------------
SSP2DATPPS0      EQU  H'0000'
SSP2DATPPS1      EQU  H'0001'
SSP2DATPPS2      EQU  H'0002'
SSP2DATPPS3      EQU  H'0003'
SSP2DATPPS4      EQU  H'0004'


;----- SSP2SSPPS Bits -----------------------------------------------------
SSP2SSPPS0       EQU  H'0000'
SSP2SSPPS1       EQU  H'0001'
SSP2SSPPS2       EQU  H'0002'
SSP2SSPPS3       EQU  H'0003'
SSP2SSPPS4       EQU  H'0004'


;----- SSP1CLKPPS Bits -----------------------------------------------------
SSP1CLKPPS0      EQU  H'0000'
SSP1CLKPPS1      EQU  H'0001'
SSP1CLKPPS2      EQU  H'0002'
SSP1CLKPPS3      EQU  H'0003'
SSP1CLKPPS4      EQU  H'0004'


;----- SSP1DATPPS Bits -----------------------------------------------------
SSP1DATPPS0      EQU  H'0000'
SSP1DATPPS1      EQU  H'0001'
SSP1DATPPS2      EQU  H'0002'
SSP1DATPPS3      EQU  H'0003'
SSP1DATPPS4      EQU  H'0004'


;----- SSP1SSPPS Bits -----------------------------------------------------
SSP1SSPPS0       EQU  H'0000'
SSP1SSPPS1       EQU  H'0001'
SSP1SSPPS2       EQU  H'0002'
SSP1SSPPS3       EQU  H'0003'
SSP1SSPPS4       EQU  H'0004'


;----- RXPPS Bits -----------------------------------------------------
RXDTPPS0         EQU  H'0000'
RXDTPPS1         EQU  H'0001'
RXDTPPS2         EQU  H'0002'
RXDTPPS3         EQU  H'0003'
RXDTPPS4         EQU  H'0004'


;----- TXPPS Bits -----------------------------------------------------
TXCKPPS0         EQU  H'0000'
TXCKPPS1         EQU  H'0001'
TXCKPPS2         EQU  H'0002'
TXCKPPS3         EQU  H'0003'
TXCKPPS4         EQU  H'0004'


;----- CLCIN0PPS Bits -----------------------------------------------------
CLCIN0PPS0       EQU  H'0000'
CLCIN0PPS1       EQU  H'0001'
CLCIN0PPS2       EQU  H'0002'
CLCIN0PPS3       EQU  H'0003'
CLCIN0PPS4       EQU  H'0004'


;----- CLCIN1PPS Bits -----------------------------------------------------
CLCIN1PPS0       EQU  H'0000'
CLCIN1PPS1       EQU  H'0001'
CLCIN1PPS2       EQU  H'0002'
CLCIN1PPS3       EQU  H'0003'
CLCIN1PPS4       EQU  H'0004'


;----- CLCIN2PPS Bits -----------------------------------------------------
CLCIN2PPS0       EQU  H'0000'
CLCIN2PPS1       EQU  H'0001'
CLCIN2PPS2       EQU  H'0002'
CLCIN2PPS3       EQU  H'0003'
CLCIN2PPS4       EQU  H'0004'


;----- CLCIN3PPS Bits -----------------------------------------------------
CLCIN3PPS0       EQU  H'0000'
CLCIN3PPS1       EQU  H'0001'
CLCIN3PPS2       EQU  H'0002'
CLCIN3PPS3       EQU  H'0003'
CLCIN3PPS4       EQU  H'0004'


;----- RA0PPS Bits -----------------------------------------------------
RA0PPS0          EQU  H'0000'
RA0PPS1          EQU  H'0001'
RA0PPS2          EQU  H'0002'
RA0PPS3          EQU  H'0003'
RA0PPS4          EQU  H'0004'


;----- RA1PPS Bits -----------------------------------------------------
RA1PPS0          EQU  H'0000'
RA1PPS1          EQU  H'0001'
RA1PPS2          EQU  H'0002'
RA1PPS3          EQU  H'0003'
RA1PPS4          EQU  H'0004'


;----- RA2PPS Bits -----------------------------------------------------
RA2PPS0          EQU  H'0000'
RA2PPS1          EQU  H'0001'
RA2PPS2          EQU  H'0002'
RA2PPS3          EQU  H'0003'
RA2PPS4          EQU  H'0004'


;----- RA4PPS Bits -----------------------------------------------------
RA4PPS0          EQU  H'0000'
RA4PPS1          EQU  H'0001'
RA4PPS2          EQU  H'0002'
RA4PPS3          EQU  H'0003'
RA4PPS4          EQU  H'0004'


;----- RA5PPS Bits -----------------------------------------------------
RA5PPS0          EQU  H'0000'
RA5PPS1          EQU  H'0001'
RA5PPS2          EQU  H'0002'
RA5PPS3          EQU  H'0003'
RA5PPS4          EQU  H'0004'


;----- RC0PPS Bits -----------------------------------------------------
RC0PPS0          EQU  H'0000'
RC0PPS1          EQU  H'0001'
RC0PPS2          EQU  H'0002'
RC0PPS3          EQU  H'0003'
RC0PPS4          EQU  H'0004'


;----- RC1PPS Bits -----------------------------------------------------
RC1PPS0          EQU  H'0000'
RC1PPS1          EQU  H'0001'
RC1PPS2          EQU  H'0002'
RC1PPS3          EQU  H'0003'
RC1PPS4          EQU  H'0004'


;----- RC2PPS Bits -----------------------------------------------------
RC2PPS0          EQU  H'0000'
RC2PPS1          EQU  H'0001'
RC2PPS2          EQU  H'0002'
RC2PPS3          EQU  H'0003'
RC2PPS4          EQU  H'0004'


;----- RC3PPS Bits -----------------------------------------------------
RC3PPS0          EQU  H'0000'
RC3PPS1          EQU  H'0001'
RC3PPS2          EQU  H'0002'
RC3PPS3          EQU  H'0003'
RC3PPS4          EQU  H'0004'


;----- RC4PPS Bits -----------------------------------------------------
RC4PPS0          EQU  H'0000'
RC4PPS1          EQU  H'0001'
RC4PPS2          EQU  H'0002'
RC4PPS3          EQU  H'0003'
RC4PPS4          EQU  H'0004'


;----- RC5PPS Bits -----------------------------------------------------
RC5PPS0          EQU  H'0000'
RC5PPS1          EQU  H'0001'
RC5PPS2          EQU  H'0002'
RC5PPS3          EQU  H'0003'
RC5PPS4          EQU  H'0004'


;----- CLCDATA Bits -----------------------------------------------------
MLC1OUT          EQU  H'0000'
MLC2OUT          EQU  H'0001'
MLC3OUT          EQU  H'0002'
MLC4OUT          EQU  H'0003'


;----- CLC1CON Bits -----------------------------------------------------
LC1INTN          EQU  H'0003'
LC1INTP          EQU  H'0004'
LC1OUT           EQU  H'0005'
LC1EN            EQU  H'0007'

LC1MODE0         EQU  H'0000'
LC1MODE1         EQU  H'0001'
LC1MODE2         EQU  H'0002'

INTN             EQU  H'0003'
INTP             EQU  H'0004'
OUT              EQU  H'0005'
EN               EQU  H'0007'

MODE0            EQU  H'0000'
MODE1            EQU  H'0001'
MODE2            EQU  H'0002'


;----- CLC1POL Bits -----------------------------------------------------
LC1G1POL         EQU  H'0000'
LC1G2POL         EQU  H'0001'
LC1G3POL         EQU  H'0002'
LC1G4POL         EQU  H'0003'
LC1POL           EQU  H'0007'

G1POL            EQU  H'0000'
G2POL            EQU  H'0001'
G3POL            EQU  H'0002'
G4POL            EQU  H'0003'
POL              EQU  H'0007'


;----- CLC1SEL0 Bits -----------------------------------------------------
LC1D1S0          EQU  H'0000'
LC1D1S1          EQU  H'0001'
LC1D1S2          EQU  H'0002'
LC1D1S3          EQU  H'0003'
LC1D1S4          EQU  H'0004'
LC1D1S5          EQU  H'0005'



D1S0             EQU  H'0000'
D1S1             EQU  H'0001'
D1S2             EQU  H'0002'
D1S3             EQU  H'0003'
D1S4             EQU  H'0004'
D1S5             EQU  H'0005'


;----- CLC1SEL1 Bits -----------------------------------------------------
LC1D2S0          EQU  H'0000'
LC1D2S1          EQU  H'0001'
LC1D2S2          EQU  H'0002'
LC1D2S3          EQU  H'0003'
LC1D2S4          EQU  H'0004'
LC1D2S5          EQU  H'0005'



D2S0             EQU  H'0000'
D2S1             EQU  H'0001'
D2S2             EQU  H'0002'
D2S3             EQU  H'0003'
D2S4             EQU  H'0004'
D2S5             EQU  H'0005'


;----- CLC1SEL2 Bits -----------------------------------------------------
LC1D3S0          EQU  H'0000'
LC1D3S1          EQU  H'0001'
LC1D3S2          EQU  H'0002'
LC1D3S3          EQU  H'0003'
LC1D3S4          EQU  H'0004'
LC1D3S5          EQU  H'0005'



D3S0             EQU  H'0000'
D3S1             EQU  H'0001'
D3S2             EQU  H'0002'
D3S3             EQU  H'0003'
D3S4             EQU  H'0004'
D3S5             EQU  H'0005'


;----- CLC1SEL3 Bits -----------------------------------------------------
LC1D4S0          EQU  H'0000'
LC1D4S1          EQU  H'0001'
LC1D4S2          EQU  H'0002'
LC1D4S3          EQU  H'0003'
LC1D4S4          EQU  H'0004'
LC1D4S5          EQU  H'0005'



D4S0             EQU  H'0000'
D4S1             EQU  H'0001'
D4S2             EQU  H'0002'
D4S3             EQU  H'0003'
D4S4             EQU  H'0004'
D4S5             EQU  H'0005'


;----- CLC1GLS0 Bits -----------------------------------------------------
LC1G1D1N         EQU  H'0000'
LC1G1D1T         EQU  H'0001'
LC1G1D2N         EQU  H'0002'
LC1G1D2T         EQU  H'0003'
LC1G1D3N         EQU  H'0004'
LC1G1D3T         EQU  H'0005'
LC1G1D4N         EQU  H'0006'
LC1G1D4T         EQU  H'0007'

D1N              EQU  H'0000'
D1T              EQU  H'0001'
D2N              EQU  H'0002'
D2T              EQU  H'0003'
D3N              EQU  H'0004'
D3T              EQU  H'0005'
D4N              EQU  H'0006'
D4T              EQU  H'0007'


;----- CLC1GLS1 Bits -----------------------------------------------------
LC1G2D1N         EQU  H'0000'
LC1G2D1T         EQU  H'0001'
LC1G2D2N         EQU  H'0002'
LC1G2D2T         EQU  H'0003'
LC1G2D3N         EQU  H'0004'
LC1G2D3T         EQU  H'0005'
LC1G2D4N         EQU  H'0006'
LC1G2D4T         EQU  H'0007'

D1N              EQU  H'0000'
D1T              EQU  H'0001'
D2N              EQU  H'0002'
D2T              EQU  H'0003'
D3N              EQU  H'0004'
D3T              EQU  H'0005'
D4N              EQU  H'0006'
D4T              EQU  H'0007'


;----- CLC1GLS2 Bits -----------------------------------------------------
LC1G3D1N         EQU  H'0000'
LC1G3D1T         EQU  H'0001'
LC1G3D2N         EQU  H'0002'
LC1G3D2T         EQU  H'0003'
LC1G3D3N         EQU  H'0004'
LC1G3D3T         EQU  H'0005'
LC1G3D4N         EQU  H'0006'
LC1G3D4T         EQU  H'0007'

D1N              EQU  H'0000'
D1T              EQU  H'0001'
D2N              EQU  H'0002'
D2T              EQU  H'0003'
D3N              EQU  H'0004'
D3T              EQU  H'0005'
D4N              EQU  H'0006'
D4T              EQU  H'0007'


;----- CLC1GLS3 Bits -----------------------------------------------------
LC1G4D1N         EQU  H'0000'
LC1G4D1T         EQU  H'0001'
LC1G4D2N         EQU  H'0002'
LC1G4D2T         EQU  H'0003'
LC1G4D3N         EQU  H'0004'
LC1G4D3T         EQU  H'0005'
LC1G4D4N         EQU  H'0006'
LC1G4D4T         EQU  H'0007'

G4D1N            EQU  H'0000'
G4D1T            EQU  H'0001'
G4D2N            EQU  H'0002'
G4D2T            EQU  H'0003'
G4D3N            EQU  H'0004'
G4D3T            EQU  H'0005'
G4D4N            EQU  H'0006'
G4D4T            EQU  H'0007'


;----- CLC2CON Bits -----------------------------------------------------
LC2INTN          EQU  H'0003'
LC2INTP          EQU  H'0004'
LC2OUT           EQU  H'0005'
LC2EN            EQU  H'0007'

LC2MODE0         EQU  H'0000'
LC2MODE1         EQU  H'0001'
LC2MODE2         EQU  H'0002'

INTN             EQU  H'0003'
INTP             EQU  H'0004'
OUT              EQU  H'0005'
EN               EQU  H'0007'

MODE0            EQU  H'0000'
MODE1            EQU  H'0001'
MODE2            EQU  H'0002'


;----- CLC2POL Bits -----------------------------------------------------
LC2G1POL         EQU  H'0000'
LC2G2POL         EQU  H'0001'
LC2G3POL         EQU  H'0002'
LC2G4POL         EQU  H'0003'
LC2POL           EQU  H'0007'

G1POL            EQU  H'0000'
G2POL            EQU  H'0001'
G3POL            EQU  H'0002'
G4POL            EQU  H'0003'
POL              EQU  H'0007'


;----- CLC2SEL0 Bits -----------------------------------------------------
LC2D1S0          EQU  H'0000'
LC2D1S1          EQU  H'0001'
LC2D1S2          EQU  H'0002'
LC2D1S3          EQU  H'0003'
LC2D1S4          EQU  H'0004'
LC2D1S5          EQU  H'0005'



D1S0             EQU  H'0000'
D1S1             EQU  H'0001'
D1S2             EQU  H'0002'
D1S3             EQU  H'0003'
D1S4             EQU  H'0004'
D1S5             EQU  H'0005'


;----- CLC2SEL1 Bits -----------------------------------------------------
LC2D2S0          EQU  H'0000'
LC2D2S1          EQU  H'0001'
LC2D2S2          EQU  H'0002'
LC2D2S3          EQU  H'0003'
LC2D2S4          EQU  H'0004'
LC2D2S5          EQU  H'0005'



D2S0             EQU  H'0000'
D2S1             EQU  H'0001'
D2S2             EQU  H'0002'
D2S3             EQU  H'0003'
D2S4             EQU  H'0004'
D2S5             EQU  H'0005'


;----- CLC2SEL2 Bits -----------------------------------------------------
LC2D3S0          EQU  H'0000'
LC2D3S1          EQU  H'0001'
LC2D3S2          EQU  H'0002'
LC2D3S3          EQU  H'0003'
LC2D3S4          EQU  H'0004'
LC2D3S5          EQU  H'0005'



D3S0             EQU  H'0000'
D3S1             EQU  H'0001'
D3S2             EQU  H'0002'
D3S3             EQU  H'0003'
D3S4             EQU  H'0004'
D3S5             EQU  H'0005'


;----- CLC2SEL3 Bits -----------------------------------------------------
LC2D4S0          EQU  H'0000'
LC2D4S1          EQU  H'0001'
LC2D4S2          EQU  H'0002'
LC2D4S3          EQU  H'0003'
LC2D4S4          EQU  H'0004'
LC2D4S5          EQU  H'0005'



D4S0             EQU  H'0000'
D4S1             EQU  H'0001'
D4S2             EQU  H'0002'
D4S3             EQU  H'0003'
D4S4             EQU  H'0004'
D4S5             EQU  H'0005'


;----- CLC2GLS0 Bits -----------------------------------------------------
LC2G1D1N         EQU  H'0000'
LC2G1D1T         EQU  H'0001'
LC2G1D2N         EQU  H'0002'
LC2G1D2T         EQU  H'0003'
LC2G1D3N         EQU  H'0004'
LC2G1D3T         EQU  H'0005'
LC2G1D4N         EQU  H'0006'
LC2G1D4T         EQU  H'0007'

D1N              EQU  H'0000'
D1T              EQU  H'0001'
D2N              EQU  H'0002'
D2T              EQU  H'0003'
D3N              EQU  H'0004'
D3T              EQU  H'0005'
D4N              EQU  H'0006'
D4T              EQU  H'0007'


;----- CLC2GLS1 Bits -----------------------------------------------------
LC2G2D1N         EQU  H'0000'
LC2G2D1T         EQU  H'0001'
LC2G2D2N         EQU  H'0002'
LC2G2D2T         EQU  H'0003'
LC2G2D3N         EQU  H'0004'
LC2G2D3T         EQU  H'0005'
LC2G2D4N         EQU  H'0006'
LC2G2D4T         EQU  H'0007'

D1N              EQU  H'0000'
D1T              EQU  H'0001'
D2N              EQU  H'0002'
D2T              EQU  H'0003'
D3N              EQU  H'0004'
D3T              EQU  H'0005'
D4N              EQU  H'0006'
D4T              EQU  H'0007'


;----- CLC2GLS2 Bits -----------------------------------------------------
LC2G3D1N         EQU  H'0000'
LC2G3D1T         EQU  H'0001'
LC2G3D2N         EQU  H'0002'
LC2G3D2T         EQU  H'0003'
LC2G3D3N         EQU  H'0004'
LC2G3D3T         EQU  H'0005'
LC2G3D4N         EQU  H'0006'
LC2G3D4T         EQU  H'0007'

D1N              EQU  H'0000'
D1T              EQU  H'0001'
D2N              EQU  H'0002'
D2T              EQU  H'0003'
D3N              EQU  H'0004'
D3T              EQU  H'0005'
D4N              EQU  H'0006'
D4T              EQU  H'0007'


;----- CLC2GLS3 Bits -----------------------------------------------------
LC2G4D1N         EQU  H'0000'
LC2G4D1T         EQU  H'0001'
LC2G4D2N         EQU  H'0002'
LC2G4D2T         EQU  H'0003'
LC2G4D3N         EQU  H'0004'
LC2G4D3T         EQU  H'0005'
LC2G4D4N         EQU  H'0006'
LC2G4D4T         EQU  H'0007'

G4D1N            EQU  H'0000'
G4D1T            EQU  H'0001'
G4D2N            EQU  H'0002'
G4D2T            EQU  H'0003'
G4D3N            EQU  H'0004'
G4D3T            EQU  H'0005'
G4D4N            EQU  H'0006'
G4D4T            EQU  H'0007'


;----- CLC3CON Bits -----------------------------------------------------
LC3INTN          EQU  H'0003'
LC3INTP          EQU  H'0004'
LC3OUT           EQU  H'0005'
LC3EN            EQU  H'0007'

LC3MODE0         EQU  H'0000'
LC3MODE1         EQU  H'0001'
LC3MODE2         EQU  H'0002'

INTN             EQU  H'0003'
INTP             EQU  H'0004'
OUT              EQU  H'0005'
EN               EQU  H'0007'

MODE0            EQU  H'0000'
MODE1            EQU  H'0001'
MODE2            EQU  H'0002'


;----- CLC3POL Bits -----------------------------------------------------
LC3G1POL         EQU  H'0000'
LC3G2POL         EQU  H'0001'
LC3G3POL         EQU  H'0002'
LC3G4POL         EQU  H'0003'
LC3POL           EQU  H'0007'

G1POL            EQU  H'0000'
G2POL            EQU  H'0001'
G3POL            EQU  H'0002'
G4POL            EQU  H'0003'
POL              EQU  H'0007'


;----- CLC3SEL0 Bits -----------------------------------------------------
LC3D1S0          EQU  H'0000'
LC3D1S1          EQU  H'0001'
LC3D1S2          EQU  H'0002'
LC3D1S3          EQU  H'0003'
LC3D1S4          EQU  H'0004'
LC3D1S5          EQU  H'0005'



D1S0             EQU  H'0000'
D1S1             EQU  H'0001'
D1S2             EQU  H'0002'
D1S3             EQU  H'0003'
D1S4             EQU  H'0004'
D1S5             EQU  H'0005'


;----- CLC3SEL1 Bits -----------------------------------------------------
LC3D2S0          EQU  H'0000'
LC3D2S1          EQU  H'0001'
LC3D2S2          EQU  H'0002'
LC3D2S3          EQU  H'0003'
LC3D2S4          EQU  H'0004'
LC3D2S5          EQU  H'0005'



D2S0             EQU  H'0000'
D2S1             EQU  H'0001'
D2S2             EQU  H'0002'
D2S3             EQU  H'0003'
D2S4             EQU  H'0004'
D2S5             EQU  H'0005'


;----- CLC3SEL2 Bits -----------------------------------------------------
LC3D3S0          EQU  H'0000'
LC3D3S1          EQU  H'0001'
LC3D3S2          EQU  H'0002'
LC3D3S3          EQU  H'0003'
LC3D3S4          EQU  H'0004'
LC3D3S5          EQU  H'0005'



D3S0             EQU  H'0000'
D3S1             EQU  H'0001'
D3S2             EQU  H'0002'
D3S3             EQU  H'0003'
D3S4             EQU  H'0004'
D3S5             EQU  H'0005'


;----- CLC3SEL3 Bits -----------------------------------------------------
LC3D4S0          EQU  H'0000'
LC3D4S1          EQU  H'0001'
LC3D4S2          EQU  H'0002'
LC3D4S3          EQU  H'0003'
LC3D4S4          EQU  H'0004'
LC3D4S5          EQU  H'0005'



D4S0             EQU  H'0000'
D4S1             EQU  H'0001'
D4S2             EQU  H'0002'
D4S3             EQU  H'0003'
D4S4             EQU  H'0004'
D4S5             EQU  H'0005'


;----- CLC3GLS0 Bits -----------------------------------------------------
LC3G1D1N         EQU  H'0000'
LC3G1D1T         EQU  H'0001'
LC3G1D2N         EQU  H'0002'
LC3G1D2T         EQU  H'0003'
LC3G1D3N         EQU  H'0004'
LC3G1D3T         EQU  H'0005'
LC3G1D4N         EQU  H'0006'
LC3G1D4T         EQU  H'0007'

D1N              EQU  H'0000'
D1T              EQU  H'0001'
D2N              EQU  H'0002'
D2T              EQU  H'0003'
D3N              EQU  H'0004'
D3T              EQU  H'0005'
D4N              EQU  H'0006'
D4T              EQU  H'0007'


;----- CLC3GLS1 Bits -----------------------------------------------------
LC3G2D1N         EQU  H'0000'
LC3G2D1T         EQU  H'0001'
LC3G2D2N         EQU  H'0002'
LC3G2D2T         EQU  H'0003'
LC3G2D3N         EQU  H'0004'
LC3G2D3T         EQU  H'0005'
LC3G2D4N         EQU  H'0006'
LC3G2D4T         EQU  H'0007'

D1N              EQU  H'0000'
D1T              EQU  H'0001'
D2N              EQU  H'0002'
D2T              EQU  H'0003'
D3N              EQU  H'0004'
D3T              EQU  H'0005'
D4N              EQU  H'0006'
D4T              EQU  H'0007'


;----- CLC3GLS2 Bits -----------------------------------------------------
LC3G3D1N         EQU  H'0000'
LC3G3D1T         EQU  H'0001'
LC3G3D2N         EQU  H'0002'
LC3G3D2T         EQU  H'0003'
LC3G3D3N         EQU  H'0004'
LC3G3D3T         EQU  H'0005'
LC3G3D4N         EQU  H'0006'
LC3G3D4T         EQU  H'0007'

D1N              EQU  H'0000'
D1T              EQU  H'0001'
D2N              EQU  H'0002'
D2T              EQU  H'0003'
D3N              EQU  H'0004'
D3T              EQU  H'0005'
D4N              EQU  H'0006'
D4T              EQU  H'0007'


;----- CLC3GLS3 Bits -----------------------------------------------------
LC3G4D1N         EQU  H'0000'
LC3G4D1T         EQU  H'0001'
LC3G4D2N         EQU  H'0002'
LC3G4D2T         EQU  H'0003'
LC3G4D3N         EQU  H'0004'
LC3G4D3T         EQU  H'0005'
LC3G4D4N         EQU  H'0006'
LC3G4D4T         EQU  H'0007'

G4D1N            EQU  H'0000'
G4D1T            EQU  H'0001'
G4D2N            EQU  H'0002'
G4D2T            EQU  H'0003'
G4D3N            EQU  H'0004'
G4D3T            EQU  H'0005'
G4D4N            EQU  H'0006'
G4D4T            EQU  H'0007'


;----- CLC4CON Bits -----------------------------------------------------
LC4INTN          EQU  H'0003'
LC4INTP          EQU  H'0004'
LC4OUT           EQU  H'0005'
LC4EN            EQU  H'0007'

LC4MODE0         EQU  H'0000'
LC4MODE1         EQU  H'0001'
LC4MODE2         EQU  H'0002'

INTN             EQU  H'0003'
INTP             EQU  H'0004'
OUT              EQU  H'0005'
EN               EQU  H'0007'

MODE0            EQU  H'0000'
MODE1            EQU  H'0001'
MODE2            EQU  H'0002'


;----- CLC4POL Bits -----------------------------------------------------
LC4G1POL         EQU  H'0000'
LC4G2POL         EQU  H'0001'
LC4G3POL         EQU  H'0002'
LC4G4POL         EQU  H'0003'
LC4POL           EQU  H'0007'

G1POL            EQU  H'0000'
G2POL            EQU  H'0001'
G3POL            EQU  H'0002'
G4POL            EQU  H'0003'
POL              EQU  H'0007'


;----- CLC4SEL0 Bits -----------------------------------------------------
LC4D1S0          EQU  H'0000'
LC4D1S1          EQU  H'0001'
LC4D1S2          EQU  H'0002'
LC4D1S3          EQU  H'0003'
LC4D1S4          EQU  H'0004'
LC4D1S5          EQU  H'0005'



D1S0             EQU  H'0000'
D1S1             EQU  H'0001'
D1S2             EQU  H'0002'
D1S3             EQU  H'0003'
D1S4             EQU  H'0004'
D1S5             EQU  H'0005'


;----- CLC4SEL1 Bits -----------------------------------------------------
LC4D2S0          EQU  H'0000'
LC4D2S1          EQU  H'0001'
LC4D2S2          EQU  H'0002'
LC4D2S3          EQU  H'0003'
LC4D2S4          EQU  H'0004'
LC4D2S5          EQU  H'0005'



D2S0             EQU  H'0000'
D2S1             EQU  H'0001'
D2S2             EQU  H'0002'
D2S3             EQU  H'0003'
D2S4             EQU  H'0004'
D2S5             EQU  H'0005'


;----- CLC4SEL2 Bits -----------------------------------------------------
LC4D3S0          EQU  H'0000'
LC4D3S1          EQU  H'0001'
LC4D3S2          EQU  H'0002'
LC4D3S3          EQU  H'0003'
LC4D3S4          EQU  H'0004'
LC4D3S5          EQU  H'0005'



D3S0             EQU  H'0000'
D3S1             EQU  H'0001'
D3S2             EQU  H'0002'
D3S3             EQU  H'0003'
D3S4             EQU  H'0004'
D3S5             EQU  H'0005'


;----- CLC4SEL3 Bits -----------------------------------------------------
LC4D4S0          EQU  H'0000'
LC4D4S1          EQU  H'0001'
LC4D4S2          EQU  H'0002'
LC4D4S3          EQU  H'0003'
LC4D4S4          EQU  H'0004'
LC4D4S5          EQU  H'0005'



D4S0             EQU  H'0000'
D4S1             EQU  H'0001'
D4S2             EQU  H'0002'
D4S3             EQU  H'0003'
D4S4             EQU  H'0004'
D4S5             EQU  H'0005'


;----- CLC4GLS0 Bits -----------------------------------------------------
LC4G1D1N         EQU  H'0000'
LC4G1D1T         EQU  H'0001'
LC4G1D2N         EQU  H'0002'
LC4G1D2T         EQU  H'0003'
LC4G1D3N         EQU  H'0004'
LC4G1D3T         EQU  H'0005'
LC4G1D4N         EQU  H'0006'
LC4G1D4T         EQU  H'0007'

D1N              EQU  H'0000'
D1T              EQU  H'0001'
D2N              EQU  H'0002'
D2T              EQU  H'0003'
D3N              EQU  H'0004'
D3T              EQU  H'0005'
D4N              EQU  H'0006'
D4T              EQU  H'0007'


;----- CLC4GLS1 Bits -----------------------------------------------------
LC4G2D1N         EQU  H'0000'
LC4G2D1T         EQU  H'0001'
LC4G2D2N         EQU  H'0002'
LC4G2D2T         EQU  H'0003'
LC4G2D3N         EQU  H'0004'
LC4G2D3T         EQU  H'0005'
LC4G2D4N         EQU  H'0006'
LC4G2D4T         EQU  H'0007'

D1N              EQU  H'0000'
D1T              EQU  H'0001'
D2N              EQU  H'0002'
D2T              EQU  H'0003'
D3N              EQU  H'0004'
D3T              EQU  H'0005'
D4N              EQU  H'0006'
D4T              EQU  H'0007'


;----- CLC4GLS2 Bits -----------------------------------------------------
LC4G3D1N         EQU  H'0000'
LC4G3D1T         EQU  H'0001'
LC4G3D2N         EQU  H'0002'
LC4G3D2T         EQU  H'0003'
LC4G3D3N         EQU  H'0004'
LC4G3D3T         EQU  H'0005'
LC4G3D4N         EQU  H'0006'
LC4G3D4T         EQU  H'0007'

D1N              EQU  H'0000'
D1T              EQU  H'0001'
D2N              EQU  H'0002'
D2T              EQU  H'0003'
D3N              EQU  H'0004'
D3T              EQU  H'0005'
D4N              EQU  H'0006'
D4T              EQU  H'0007'


;----- CLC4GLS3 Bits -----------------------------------------------------
LC4G4D1N         EQU  H'0000'
LC4G4D1T         EQU  H'0001'
LC4G4D2N         EQU  H'0002'
LC4G4D2T         EQU  H'0003'
LC4G4D3N         EQU  H'0004'
LC4G4D3T         EQU  H'0005'
LC4G4D4N         EQU  H'0006'
LC4G4D4T         EQU  H'0007'

G4D1N            EQU  H'0000'
G4D1T            EQU  H'0001'
G4D2N            EQU  H'0002'
G4D2T            EQU  H'0003'
G4D3N            EQU  H'0004'
G4D3T            EQU  H'0005'
G4D4N            EQU  H'0006'
G4D4T            EQU  H'0007'


;----- STATUS_SHAD Bits -----------------------------------------------------
C_SHAD           EQU  H'0000'
DC_SHAD          EQU  H'0001'
Z_SHAD           EQU  H'0002'



;==========================================================================
;
;       RAM Definitions
;
;==========================================================================
       __MAXRAM  H'0FFF'
       __BADRAM  H'000D'
       __BADRAM  H'000F'
       __BADRAM  H'008D'
       __BADRAM  H'008F'
       __BADRAM  H'0095'
       __BADRAM  H'0096'
       __BADRAM  H'0098'
       __BADRAM  H'0099'
       __BADRAM  H'009A'
       __BADRAM  H'010D'
       __BADRAM  H'010F'-H'0110'
       __BADRAM  H'011A'-H'011F'
       __BADRAM  H'018D'
       __BADRAM  H'018F'-H'0196'
       __BADRAM  H'0198'
       __BADRAM  H'020D'
       __BADRAM  H'020F'-H'0210'
       __BADRAM  H'0218'
       __BADRAM  H'028D'
       __BADRAM  H'028F'-H'0290'
       __BADRAM  H'0299'-H'029E'
       __BADRAM  H'030D'
       __BADRAM  H'030F'-H'0310'
       __BADRAM  H'0319'-H'031F'
       __BADRAM  H'038D'
       __BADRAM  H'038F'-H'0390'
       __BADRAM  H'0394'-H'0396'
       __BADRAM  H'039B'
       __BADRAM  H'040C'-H'0410'
       __BADRAM  H'048C'-H'0497'
       __BADRAM  H'050C'-H'051F'
       __BADRAM  H'058C'-H'059F'
       __BADRAM  H'060C'-H'0616'
       __BADRAM  H'061D'-H'061E'
       __BADRAM  H'068C'-H'0690'
       __BADRAM  H'069A'-H'069F'
       __BADRAM  H'070C'-H'0710'
       __BADRAM  H'071A'-H'071F'
       __BADRAM  H'078C'-H'079F'
       __BADRAM  H'080C'-H'081F'
       __BADRAM  H'088C'-H'0890'
       __BADRAM  H'0897'-H'089A'
       __BADRAM  H'089C'-H'089F'
       __BADRAM  H'090C'-H'0910'
       __BADRAM  H'0917'
       __BADRAM  H'098C'-H'099F'
       __BADRAM  H'0A0C'-H'0A1F'
       __BADRAM  H'0A8C'-H'0A9F'
       __BADRAM  H'0B0C'-H'0B1F'
       __BADRAM  H'0B8C'-H'0B9F'
       __BADRAM  H'0C0C'-H'0C1F'
       __BADRAM  H'0C8C'-H'0C9F'
       __BADRAM  H'0CC0'-H'0CEF'
       __BADRAM  H'0D0C'-H'0D13'
       __BADRAM  H'0D14'-H'0D1F'
       __BADRAM  H'0D20'-H'0D6F'
       __BADRAM  H'0D8C'-H'0D9F'
       __BADRAM  H'0DA0'-H'0DEF'
       __BADRAM  H'0E0C'-H'0E0E'
       __BADRAM  H'0E23'
       __BADRAM  H'0E26'-H'0E27'
       __BADRAM  H'0E30'-H'0E6F'
       __BADRAM  H'0E8C'-H'0E8F'
       __BADRAM  H'0E93'
       __BADRAM  H'0E96'-H'0E9F'
       __BADRAM  H'0EA6'-H'0EEF'
       __BADRAM  H'0F0C'-H'0F0E'
       __BADRAM  H'0F38'-H'0F6F'
       __BADRAM  H'0F8C'-H'0FE3'
       __BADRAM  H'0FEC'

;==========================================================================
;
;       Configuration Bits
;
;   NAME            Address
;   CONFIG1           8007h
;   CONFIG2           8008h
;   CONFIG3           8009h
;   CONFIG4           800Ah
;
;==========================================================================

; The following is an assignment of address values for all of the
; configuration registers for the purpose of table reads
_CONFIG1        EQU  H'8007'
_CONFIG2        EQU  H'8008'
_CONFIG3        EQU  H'8009'
_CONFIG4        EQU  H'800A'

;----- CONFIG1 Options --------------------------------------------------
_FEXTOSC_LP          EQU  H'3FF8'; LP (crystal oscillator) optimized for 32.768 kHz
_FEXTOSC_XT          EQU  H'3FF9'; XT (crystal oscillator) from 100 kHz to 4 MHz
_FEXTOSC_HS          EQU  H'3FFA'; HS (crystal oscillator) above 4 MHz
_FEXTOSC_OFF         EQU  H'3FFC'; Oscillator not enabled
_FEXTOSC_ECL         EQU  H'3FFD'; EC (external clock) below 100 kHz
_FEXTOSC_ECM         EQU  H'3FFE'; EC (external clock) for 100 kHz to 8 MHz
_FEXTOSC_ECH         EQU  H'3FFF'; EC (external clock) above 8 MHz

_RSTOSC_HFINT32      EQU  H'3F8F'; HFINTOSC with 2x PLL (32MHz)
_RSTOSC_EXT4X        EQU  H'3F9F'; EXTOSC with 4x PLL, with EXTOSC operating per FEXTOSC bits
_RSTOSC_SOSC         EQU  H'3FBF'; SOSC (31kHz)
_RSTOSC_LFINT        EQU  H'3FCF'; LFINTOSC (31kHz)
_RSTOSC_HFINT1       EQU  H'3FEF'; HFINTOSC (1MHz)
_RSTOSC_EXT1X        EQU  H'3FFF'; EXTOSC operating per FEXTOSC bits

_CLKOUTEN_ON         EQU  H'3EFF'; CLKOUT function is enabled; FOSC/4 clock appears at OSC2
_CLKOUTEN_OFF        EQU  H'3FFF'; CLKOUT function is disabled; I/O or oscillator function on OSC2

_CSWEN_OFF           EQU  H'37FF'; The NOSC and NDIV bits cannot be changed by user software
_CSWEN_ON            EQU  H'3FFF'; Writing to NOSC and NDIV is allowed

_FCMEN_OFF           EQU  H'1FFF'; Fail-Safe Clock Monitor is disabled
_FCMEN_ON            EQU  H'3FFF'; Fail-Safe Clock Monitor is enabled

;----- CONFIG2 Options --------------------------------------------------
_MCLRE_OFF           EQU  H'3FFE'; MCLR/VPP pin function is digital input; MCLR internally disabled; Weak pull-up under control of port pin's WPU control bit.
_MCLRE_ON            EQU  H'3FFF'; MCLR/VPP pin function is MCLR; Weak pull-up enabled

_PWRTE_ON            EQU  H'3FFD'; PWRT enabled
_PWRTE_OFF           EQU  H'3FFF'; PWRT disabled

_WDTE_OFF            EQU  H'3FF3'; WDT disabled; SWDTEN is ignored
_WDTE_SWDTEN         EQU  H'3FF7'; WDT controlled by the SWDTEN bit in the WDTCON register
_WDTE_SLEEP          EQU  H'3FFB'; WDT enabled while running and disabled in SLEEP/IDLE; SWDTEN is ignored
_WDTE_ON             EQU  H'3FFF'; WDT enabled, SWDTEN is ignored

_LPBOREN_ON          EQU  H'3FDF'; ULPBOR enabled
_LPBOREN_OFF         EQU  H'3FFF'; ULPBOR disabled

_BOREN_OFF           EQU  H'3F3F'; Brown-out Reset disabled
_BOREN_SBOREN        EQU  H'3F7F'; Brown-out Reset enabled according to SBOREN
_BOREN_SLEEP         EQU  H'3FBF'; Brown-out Reset enabled while running, disabled in Sleep; SBOREN is ignored
_BOREN_ON            EQU  H'3FFF'; Brown-out Reset enabled, SBOREN bit ignored

_BORV_HIGH           EQU  H'3DFF'; Brown-out voltage (Vbor) set to 2.7V
_BORV_LOW            EQU  H'3FFF'; Brown-out voltage (Vbor) set to 2.45V

_PPS1WAY_OFF         EQU  H'37FF'; The PPSLOCK bit can be set and cleared repeatedly (subject to the unlock sequence)
_PPS1WAY_ON          EQU  H'3FFF'; The PPSLOCK bit can be cleared and set only once; PPS registers remain locked after one clear/set cycle

_STVREN_OFF          EQU  H'2FFF'; Stack Overflow or Underflow will not cause a Reset
_STVREN_ON           EQU  H'3FFF'; Stack Overflow or Underflow will cause a Reset

_DEBUG_ON            EQU  H'1FFF'; Background debugger enabled
_DEBUG_OFF           EQU  H'3FFF'; Background debugger disabled

;----- CONFIG3 Options --------------------------------------------------
_WRT_ALL             EQU  H'3FFC'; 0000h to 3FFFh write protected, no addresses may be modified
_WRT_HALF            EQU  H'3FFD'; 0000h to 1FFFh write-protected, 2000h to 3FFFh may be modified
_WRT_BOOT            EQU  H'3FFE'; 0000h to 01FFh write-protected, 0200h to 3FFFh may be modified
_WRT_OFF             EQU  H'3FFF'; Write protection off

_LVP_OFF             EQU  H'1FFF'; High Voltage on MCLR/VPP must be used for programming.
_LVP_ON              EQU  H'3FFF'; Low Voltage programming enabled. MCLR/VPP pin function is MCLR. MCLRE configuration bit is ignored.

;----- CONFIG4 Options --------------------------------------------------
_CP_ON               EQU  H'3FFE'; User NVM code protection enabled
_CP_OFF              EQU  H'3FFF'; User NVM code protection disabled

_CPD_ON              EQU  H'3FFD'; Data NVM code protection enabled
_CPD_OFF             EQU  H'3FFF'; Data NVM code protection disabled

;----- DEVID Equates --------------------------------------------------
_DEVID1          EQU  H'8006'

;----- IDLOC Equates --------------------------------------------------
_IDLOC0          EQU  H'8000'
_IDLOC1          EQU  H'8001'
_IDLOC2          EQU  H'8002'
_IDLOC3          EQU  H'8003'

        LIST
