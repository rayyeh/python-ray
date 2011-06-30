000001 //APYCHRXC JOB  SP,APYCH,MSGCLASS=X,MSGLEVEL=(1,1),CLASS=A,REGION=6M,   
000002 //         NOTIFY=&SYSUID,TYPRUN=HOLD                                   
000003 //REXXC    PROC OPTIONS='XREF OBJECT',         REXX Compiler options    
000004 //            COMPDSN='REXX.SFANLMD'  REXX Compiler load lib            
000005 //REXX     EXEC PGM=REXXCOMP,PARM='&OPTIONS'                            
000006 //STEPLIB  DD DSN=&COMPDSN,DISP=SHR                                     
000007 //SYSPRINT DD SYSOUT=*                                                  
000008 //SYSTERM  DD SYSOUT=*                                                  
000009 //SYSIN    DD DSN=CARDPAC.APYCH.PGMLIB(&MBR),DISP=SHR                   
000010 //SYSCEXEC DD DSN=CARDPAC.APYCH.LOADLIB(&MBR),DISP=SHR                  
000011 //SYSPUNCH DD DSN=&&OBJECT,DISP=(MOD,PASS),UNIT=SYSDA,                  
000012 //            SPACE=(800,(800,100))                                     
000013 //   PEND                                                               
000014 //ALTCLAC1 EXEC REXXC,MBR=REXXCLT                                       