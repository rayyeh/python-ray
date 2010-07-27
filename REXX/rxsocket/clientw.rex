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
 *______________________________________________________________about__
 *
 *  purpose : TCP/IP Socket Echo-Example-Client for Workstations
 *  syntax  : rexx clientw.rex [<addr> <port>]
 *  systems : AIX, Linux, OS/2, Win32
 *  requires:
 *  author  : Thorsten Schaper, IBM
 *  created : 04/18/2000
 *  last mod: 03/12/2001
 *_____________________________________________________code_structure__
 *
 *  main:
 *  HALT:
 *  NOVALUE:
 *  exit_With_Error:
 *
 *  initialize_Usage_Of_Sockets_IP_Interface:
 *  create_The_Socket_For_Communication_With_Server:
 *
 *  connect_To_The_Given_Server:
 *  display_User_Menu:
 */

SIGNAL ON NOVALUE
SIGNAL ON HALT

main:
   parse source src
   parse arg addr port

   call initialize_Usage_Of_Sockets_IP_Interface
   call connect_To_The_Given_Server
   call display_User_Menu

HALT:
   call SockShutdown socket, 2         /* -> defined to linger up  */
   call SockSoClose  socket            /*    to 5 sec.             */
   exit 0

NOVALUE:
   if SIGL > 0 then
       sl = sourceLine(SIGL)
   else
       sl = ''
   say condition('C') 'runtime condition has been raised:'
   say '  variable name   :' condition('D')
   say '  error line nr   :' SIGL
   say '  error line text :' sl
   return

exit_With_Error:
   parse arg loc, RC

   SIGNAL OFF NOVALUE
   say "!!! ERROR"
   say "  location of error = "loc
   say "  RC                = "RC
   say "  socket error nr   = "SockSock_Errno()
   say "  error description = "errno '/' h_errno
   if datatype(RC, 'N') then
      exit RC
   exit 1

/*===================================================================*/

initialize_Usage_Of_Sockets_IP_Interface:

   parse value 'initSock'() with errRC errPos
   if errRC \= 0 then
      call exit_With_Error errPos, errRC

   return

/*===================================================================*/

create_The_Socket_For_Communication_With_Server:

   parse value 'newSock'() with errRC errPos
   if errRC \= 0 then
      call exit_With_Error errPos, errRC
   else
      socket = errPos

   return socket

/*===================================================================*/

connect_To_The_Given_Server:

   socket = create_The_Socket_For_Communication_With_Server()

   /* Build server address from command line parameters,
    * or apply defaults.
    */
   if addr = '' then addr = '127.0.0.1'
   if port = '' then port = 5000
   address.!family  = 'AF_INET'
   address.!addr    = addr
   address.!port    = port

   say '...trying to connect to service at:'
   say 'host =' address.!addr
   say 'port =' address.!port

   /* Try to connect to server.
    */
   call SockConnect socket, 'address.!'

   /* Check if connection was established.
    */
   wList.0 = 1
   wList.1 = socket
   if SockSelect('', 'wList.', '', 5) = 0 then
      call exit_With_Error 'SockConnect', -1

   say '--> established on socket:' socket
   say

   /* Send string 'src' to the server.
    */
   RC = SockSend(socket, src)
   if RC < 0 then
      call exit_With_Error 'SockSend', RC

   parse value 'rcvfSock'(socket, 5) with recvSize recvText
   if recvSize <= 0 then
      call exit_With_Error 'SockRecv', -1

   if recvText \= 'OK' then do
      call SockShutdown socket, 2
      call SockClose    socket
      call exit_With_Error 'Didn''t receive ACKnowledgement', -1
   end

   return

/*===================================================================*/

display_User_Menu:

   text.  = ''
   text.0 = 4
   text.1 = "send 'TXTHello World!'    text    message"
   text.2 = "enter text for sending a  text    message"
   text.3 = "send 'CMDshutDownService' command message"
   text.4 = 'close connection & exit'

   do forever

      /* Print menu and get selection from user.
       */
      do i = 1 to text.0
         say i".)  "text.i
      end
      pull nr
      if nr = 4 then leave

      /* Build string to send to server.
       */
      select
         when nr = 1 then
            sendStr = 'TXTHello world!'
         when nr = 2 then do
            parse pull inputLine
            sendStr = 'TXT'inputLine
         end
         when nr = 3 then
            sendStr = 'CMDshutDownService'
         otherwise
            sendStr = 'TXTHello confused little world!'
      end

      /* Send string to server.
       */
      RC = SockSend(socket, sendStr)
      if RC < 0 then
         call exit_With_Error 'SockSend', RC

      say copies('=', 72)
      say "...sent text was   : '"sendStr"'"

      if nr = 3 then leave

      /* Wait for reply.
       */
      parse value 'rcvfSock'(socket, 5) with recvSize recvText
      if recvSize < 0 then
         call exit_With_Error 'SockRecv', -1
      if recvSize = 0 then
         say '...nothing received from socket:' socket
      else
         say "...server replied  : '"recvText"'"
      say copies('=', 72)
   end

   return