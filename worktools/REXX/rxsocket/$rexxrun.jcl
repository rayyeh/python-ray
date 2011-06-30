000001 //YCHREXX  JOB    SP,APYCH,MSGLEVEL=(1,1),                           
000002 //         CLASS=A,MSGCLASS=X,NOTIFY=&SYSUID                         
000003 //IKJACCNT EXEC PGM=IKJEFT01                                         
000004 //SYSEXEC  DD  DSN=CARDPAC.APYCH.PGMLIB,DISP=SHR                     
000005 //SYSPRINT DD  SYSOUT=*                                              
000006 //SYSTSPRT DD  SYSOUT=*                                              
000007 //SYSTSIN  DD  *                                                     
000008    REXXCLT                                                           
000009 /*                                                                   