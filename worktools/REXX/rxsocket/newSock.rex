/*REXX*****************************************************************
 *
 * (C) Copyright IBM Corp. 2000 - All Rights Reserved.
 *
 * DISCLAIMER OF WARRANTIES.  The following [enclosed] code is sample
 * code created by IBM Corporation. This sample code is not part of
 * any standard or IBM product and is provided to you solely for the
 * purpose of assisting you in the development of your applications.
 * The code is provided "AS IS", without warranty of any kind.
 * IBM shall not be liable for any damages arising out of your use of
 * the sample code,  even if they have been advised of the possibility
 * of such damages.
 *
 *=====================================================================
 *
 * purpose: create and configure a new socket.
 *
 * parms  :
 *
 * return : socket handle (integer number).
 */

/* create a new socket for the TCP/IP protocol.
 */
socket = SockSocket('AF_INET', 'SOCK_STREAM', 'IPPROTO_TCP')
if socket < 0 then
   return socket 'newSock-SockSocket',

/* 'keep-alive' ensures that the connection won't get closed
 *          even if there has been no traffic for a longer time.
 */
RC = SockSetSockOpt(socket, 'SOL_SOCKET', 'SO_KEEPALIVE', '1')
if RC \= 0 then
   return RC 'newSock-SockSetSockOpt-SO_KEEPALIVE'

/* 'linger' mode makes sure that data that is still to be sent
 *          won't get lost when a closeSocket call occurs.
 *          -> it blocks the application at socket closing for
 *             the specified amount of seconds.
 */
RC = SockSetSockOpt(socket, 'SOL_SOCKET', 'SO_LINGER', '1 5')
if RC \= 0 then
   return RC 'newSock-SockSetSockOpt-SO_LINGER'

/* DISabled(0) 'non-blocking' mode makes I/O statements block
 *             the execution of the program until they've been
 *             satisfied, because I/O has been TCP/IP-acknowledged.
 *
 * ENabled(1) 'non-blocking' mode makes I/O statements return
 *             promptly a RC = -1 instead of blocking execution.
 */
RC = SockIOCtl(socket, 'FIONBIO', '1')
if RC \= 0 then
   return RC 'newSock-SockIOCtl'

return 0 socket

