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
 *  purpose : TCP/IP Socket Echo-Example-Server for Workstations
 *  syntax  : rexx serverw.rex [<port>]
 *  systems : AIX, Linux, OS/2, Win32
 *  requires:
 *  author  : Thorsten Schaper, IBM
 *  created : 04/18/2000
 *  last mod: 03/09/2001
 *_____________________________________________________code_structure__
 *
 *  main:
 *  HALT:
 *  NOVALUE:
 *  exit_With_Error:
 *
 *  initialize_Usage_Of_Sockets_IP_Interface:
 *  create_The_Server_Socket:
 *
 *  establish_The_Service:
 *  run_The_Service:
 *  accept_A_New_Client:
 *  handle_A_Clients_Request:
 *  shutdown_The_Service:
 *
 *  add_Socket_To_List:
 *  remove_Socket_From_List:
 */

SIGNAL ON NOVALUE
SIGNAL ON HALT

main:
   parse arg port

   sockList = ''
   sockTranslate. = 0

   call initialize_Usage_Of_Sockets_IP_Interface
   call establish_The_Service
   call run_The_Service

HALT:
   call shutdown_The_Service
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

create_The_Server_Socket:

   parse value 'newSock'() with errRC errPos
   if errRC \= 0 then
      call exit_With_Error errPos, errRC
   else
      socket = errPos

   return socket

/*===================================================================*/

establish_The_Service:

   srvSock = create_The_Server_Socket()

   call add_Socket_To_List srvSock 0

   /* build server address.
    */
   if port = '' then do
      port = 5000
      addr = '127.0.0.1'
   end
   else do
      if \dataType(port, 'N') then
         call exit_With_Error 'port number must be NUMERIC', -1
      addr = SockGetHostId()
   end

   address.!family  = "AF_INET"
   address.!port    = port
   address.!addr    = addr

   say '-> trying to bind service to:'
   say '   host =' address.!addr
   say '   port =' address.!port

   RC = SockBind(srvSock, 'address.!')       /* bind the server socket to    */
   if RC \= 0 then                           /* an IP address and port.      */
      call exit_With_Error 'SockBind', RC

   RC = SockListen(srvSock, 1024)            /* create a connection request  */
   if RC \= 0 then                           /* queue for incoming requests. */
      call exit_With_Error 'SockListen', RC

   say '...listening for clients on socket:' srvSock
   say

   return

/*===================================================================*/

run_The_Service:

   do forever
      /*  check, if there are any connection request pending or if any       */
      /*  of the already accepted clients has sent some data.                */
      rList.0 = words(sockList)
      do i = 1 to rList.0
         rList.i = word(sockList, i)
      end

      nrOfReadySockets = SockSelect('rList.', '', '', 1)

      if nrOfReadySockets > 0 then do
         do i = 1 to rList.0                 /*  process each socket that    */
            rSock = rList.i                  /*  has been found to be ready  */
            if rSock = srvSock then          /*  for reading.                */
               call accept_A_New_Client
            else
               call handle_A_Clients_Request
         end
      end
   end

   return

/*===================================================================*/

accept_A_New_Client:

   say '-> trying to accept a new client'
   clSock = SockAccept(srvSock)
   if clSock < 0 then
      call exit_With_Error 'Accept', clSock
   say '...OK, new client is connected on socket:' clSock

   /* Set newly accepted socket to NON-BLOCKING mode also.
    * -> on Windows platforms this is already done by the accept call,
    *    so this is only necessary for UNIX platforms.
    */
   RC = SockIOCtl(clSock, 'FIONBIO', '1')
   if RC \= 0 then
      call exit_With_Error 'SockIOCtl', RC

   /* Receive information about client-machine-environment.
    */
   parse value 'rcvfSock'(clSock, 5) with recvSize recvText
   if recvSize <= 0 then
      call exit_With_Error 'SockRecv', -1

   /* Decide, if EBCDIC -> ASCII translation is necessary.
    */
   if \datatype(left(recvText, 1), 'Alphanumeric') then do
      translate = 1
      recvText = trnslate(recvText, 'E', 'A')
   end
   else
      translate = 0

   say '...clientInfo:' recvText

   /* send 'OK' as acknowledgement
    */
   sendText = 'OK'
   if translate then
      sendText = trnslate(sendText, 'A', 'E')
   RC = SockSend(clSock, sendText)
   if RC <= 0  then
      call exit_With_Error 'SockSend', RC

   call add_Socket_To_List clSock translate

   return

/*===================================================================*/

handle_A_Clients_Request:

   say '-> got a request from client connected at socket:' rSock

   parse value 'rcvfSock'(rSock, 5) with recvSize recvText

   if recvSize < 0 then
      call exit_With_Error 'SockRecv', -1

   if recvSize = 0 then do
      say '+++ nothing received from socket:' rsock
      say '+++ assuming that client has diconnected!'
      say '+++ shutting down socket:' rSock

      call remove_Socket_From_List rSock
      call SockShutdown rSock, 2
      call SockSoClose  rSock

      return
   end

   if sockTranslate.rSock then
      recvText = trnslate(recvText, 'E', 'A')

   say "...received:  '"recvText"'"

   select
      /* received a 'TXT'-message from client.
       */
      when abbrev(recvText, 'TXT') then do
         text = substr(recvText, 4)
         answer = "server has received your text :'"recvText"'"
         say "...answering: '"answer"'"
         if sockTranslate.rSock then
            answer = trnslate(answer, 'A', 'E')
         RC = SockSend(rSock, answer)
         if RC <= 0 then
            call exit_With_Error 'SockSend', RC
      end

      /* received a 'CMD'-message from client.
       */
      when abbrev(recvText, 'CMD') then do
         recvText = substr(recvText, 4)
         if recvText = 'shutDownService' then do
            call shutdown_The_Service
            exit 0
         end
      end

      otherwise do
         say '+++ ERROR: unknown message format sent by client!'
         say '+++ ignoring client''s request'
      end
   end

   return

/*===================================================================*/

shutdown_The_Service:

   say "-> shutting down all sockets..."
   do i = words(sockList) to 1 by -1
      sock = word(sockList, i)
      RC = SockShutDown(sock, 2)
      if RC = 0 then
         ext = 'is down.'
      else
         ext = 'had problems -> RC = 'rc
      say right(sock, 6)': 'ext
   end

   say "-> Socket REXX-API functions NOT dropped to avoid crashing other"
   say "   REXX programs that are using the Socket API at the moment."
   say "good bye"

   return

/*===================================================================*/

add_Socket_To_List:
   parse arg newSocket translate

   sockList = sockList newSocket
   sockTranslate.newSocket = translate

   return

/*===================================================================*/

remove_Socket_From_List:
   parse arg remSocket

   sockList = delStr(sockList, pos(remSocket, sockList), length(remSocket)+1)

   return