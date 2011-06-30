000001 //TPREXX   JOB ,'CPFTPGLF',CLASS=B,MSGLEVEL=(1,1),                      
000002 //         MSGCLASS=B,REGION=32M,NOTIFY=&SYSUID,TYPRUN=HOLD             
000003 //*                                                                     
000004 //IKJACCNT EXEC PGM=IKJEFT01                                            
000005 //SYSEXEC  DD  DSN=CARDPAC.APYCH.PGMLIB,DISP=SHR                        
000006 //*TCPIP    DD  DISP=SHR,DSN=SYS1.PROCLIB(TCPIP)                        
000007 //SYSTCPD  DD  DSN=CARDPAC.APYCH.PGMLIB(TCPDATA),DISP=SHR               
000008 //SYSTSPRT DD  SYSOUT=*                                                 
000009 //SYSPRINT DD  SYSOUT=*                                                 
000010 //SYSTSIN  DD  *                                                        
000011    REXXCLT                                                              
000012 /*                                                                      
000013 //*                                                                     
000014 //                                                                      