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
 * purpose: wait for input and read from a non-blocking socket.
 *
 * parms  : sock     = socket handle (integer number).
 *          timeOut  = time to wait for input on the specified socket
 *                     in sec.
 *                     A timeout value of 0 means endless wait.
 *
 * return : number of read bytes, or zero if timeout has been reached,
 *          followed by the received text, if any.
 */

parse arg sock, timeOut

if \dataType(timeOut, 'N') then
   timeOut = 0

recvText = ''
recvSize = 0
rList.0  = 1
rList.1  = sock

do until SockSelect('rList.', '', '', 1) > 0 | timeOut = 0
   timeOut = timeOut - 1
end

if timeOut = 0 then
   return 0

do until size < 10
   size = SockRecv(sock, 'text', 10)
   if size > 0 then do
      recvText = recvText || text
      recvSize = recvSize + size
   end
end

return recvSize recvText
