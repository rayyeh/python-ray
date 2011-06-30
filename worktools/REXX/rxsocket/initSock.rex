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
 * purpose: initialize usage of the socket API.
 *
 * parms  : none
 *
 * return : 0 = success
 *          x = error
 */

if RxFuncQuery('SockDropFuncs') \= 0 then do
   if RxFuncAdd('SockLoadFuncs', 'rxsock', 'SockLoadFuncs') = 0 then
      call SockLoadFuncs
   else
      return -1 'initSock-RxFuncAdd'
end

return 0
