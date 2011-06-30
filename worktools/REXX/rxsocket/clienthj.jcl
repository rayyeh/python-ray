000001 //TPCLIENT JOB ,'CLIENTHJ',CLASS=B,MSGLEVEL=(1,1),                      
000002 //         MSGCLASS=B,REGION=32M,NOTIFY=&SYSUID,TYPRUN=HOLD             
000003 //*                                                                     
000004 //* DOC: THIS JOB CONNECTS TO A NAME REGISTRAR SERVER AND QUERIES       
000005 //*      A DOMAINS REGISTRATION RECORD.                                 
000006 //*                                                                     
000007 //IKJACCNT EXEC PGM=IKJEFT01                                            
000008 //SYSEXEC  DD  DSN=CARDPAC.APYCH.PGMLIB,DISP=SHR                        
000009 //*TCPIP    DD  DISP=SHR,DSN=SYS1.PROCLIB(TCPIP)                        
000010 //SYSTCPD  DD  DSN=CARDPAC.APYCH.PGMLIB(TCPDATA),DISP=SHR               
000011 //SYSTSPRT DD  SYSOUT=*                                                 
000012 //SYSPRINT DD  SYSOUT=*                                                 
000013 //SYSTSIN  DD  *                                                        
000014    CLIENTH 192.168.110.1 9999                                           
000015 /*                                                                      
000016 //*                                                                   
000017 //                                                                    