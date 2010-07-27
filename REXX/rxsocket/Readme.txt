=======================================================================
README for REXX Socket API sample:
      "Communicate between mainframes and workstations via TCP/IP"
=======================================================================

   Contents:

      1.)   Abstract
      2.)   Description
      3.)   Requirements
      4.)   Installation instructions
      5.)   Usage
      6.)   Socket API pitfalls
      7.)   Getting Help

=======================================================================
1.) Abstract
=======================================================================

   This sample demonstrates how workstations and mainframes can
   communicate via TCP/IP networks using REXX Socket APIs.

=======================================================================
2.) Description
=======================================================================

   REXX Socket APIs enable you to code network applications in REXX:

   -  Socket is the standard IP programming interface

   -  Socket APIs are available from IBM for REXX for the following
      systems:
      -  S/390 (VM, MVS, VSE, Linux)
      -  X/86  (OS/2, AIX, Linux, Windows)

   Unfortunately the APIs are not the same - BUT that doesn't mean that
   they wouldn't work together - this sample is the proof:

   -  it implements a simple IP service called 'ECHO':
      -  the client sends a string to the server as request
      -  the server appends a note to the string and sends it back to
         the client as result to his request

   -  Each, server and client, are coded twice:
      - mainframe and
      - workstation version

   -  server may be started on mainframe or workstation

   -  server can handle multiple clients

   -  client may connect from  mainframe or workstation

   -  EBCDIC <-> ASCII translation is taken care of

   VSE:  If you are looking for something VSE specific have a look
         at the VSE/REXX IBM webpages - you'll find sample code and
         more information there.

=======================================================================
3.) Requirements
=======================================================================

   This software is designed and tested for the following platforms:
      - OS/390
      - VM
      - AIX
      - Linux
      - Win32
      - OS/2

   Machines that shall run a socket application must be ready to use
   the TCP/IP protocol stack.

   Workstations shouldn't make any problems, and mainframe users
   should contact their system administrator if TCP/IP installation
   is required.

   To test a socket application on only one machine you even need not
   have a network adapter installed - just use the special loopback IP
   address 127.0.0.1.

=======================================================================
4.) Installation instructions
=======================================================================

   1.) Unzip the *.ZIP file on a workstation.

   2.) You should find following files:

         Readme.txt
         clientw.rex
         clienth.exec
         serverw.rex
         serverh.exec
         initSock.rex
         initSock.exec
         newSock.rex
         newSock.exec
         rcvfSock.rex
         rcvfSock.exec
         trnslate.rex
         trnslate.exec

   3.) For mainframes copy required REXX programs:

         VM:      copy all *.EXEC files to one of your mini disks (with
                  filetype EXEC).
         MVS:     copy all *.EXEC files as members into a PDS that is
                  allocated to the ddName SYSEXEC.
         Linux:   No extra copying necessary - Linux for S/390 uses the
                  *.rex REXX scripts (such as Linux on X/86).

=======================================================================
5.) Usage
=======================================================================

   First you have to start the server program - so it can initialize
   its sockets and start listening on incoming requests:

   - mainframe:   EXEC SERVERH [<port>]
   - workstation: rexx serverw [<port>]

      <port>   is the port number on which the server shall listen
               for requests from clients. The server is said to be
               "offering its service on that port". Clients who want
               to connect to the server must know this port.

   If <port> is not specified 5000 will be taken as default port number
   and 127.0.0.1 as IP address of the service, else the IP address of
   the local machine and the given port number are used.

   Then you can start several clients (on several machines if you like)
   that will be handled sequentially by the server:

   - mainframe:   EXEC CLIENTH [<host> <port>]
   - workstation: rexx clientw [<host> <port>]

      <host>   is the dotted IP address of the server machine,
               which is called the 'remote host' in that context.

      <port>   is the port number on which the server is listening
               for requests.

   If <host> and <port> are not given the server's address defaults
   to 127.0.0.1 and the server's port to 5000.

   For mainframes the maximum number of sockets is set to 10 (see
   variable 'maxSock' in serverh.exec). One socket is needed by the
   server, so the server has enough sockets left for servicing 9
   clients simultaneously.

   For workstations you can/need not specify the maximum number of
   possible sockets directly - as many clients as the system accepts
   may simultaneously connect to the server.

   Looking up hosts by their names is not supported - but can easily
   be implemented using the SockGetHostByName() API function.

=======================================================================
6.) Socket API pitfalls
=======================================================================

   1.) 'SockDropFuncs' - Workstation API

   The 'SockDropFuncs' API function deregisters all API entry points
   from the current REXX runtime environment, so, if other REXX progs
   are active in the same environment and they also use the Socket API
   they will abnormally end with a 'Sock....' function not found error
   message!

   2.) non-blocking sockets and the 'Connect' socket call:

   For non-blocking sockets the return code of a 'Connect' call is
   always '-1'. The best way to check, if the connection has been
   established is to use the 'Select' socket call and test if the
   socket is writable (-> see connect_To_The_Given_Server routine).

   3.) non-blocking sockets and the 'Accept' socket call:

   When a server accepts a new client using a non-blocking socket for
   listening on connection requests the new socket created by the
   Accept socket call will be...
   -  non-blocking for Windows systems.
   -  blocking     for AIX, Linux and Mainframe (VM,MVS) systems.

   4.) lingering on close:

   Lingering on close / shutdown of a socket doesn't always seem to
   work as specified on VM/CMS.

=======================================================================
7.) Getting Help
=======================================================================

   On the IBM BookManager(R) BookServer Library internet page at:

      http://publibz.boulder.ibm.com:80/cgi-bin/bookmgr_OS390/library

   are 2 books about socket programming on mainframes that are
   interesting in that context:

      "TCP/IP V3R2 for MVS: API Reference" (SC31-7187)
      "OS/390 V2R10.0 IBM CS IP API Guide" (SC31-8516)

   The REXX Socket APIs provided for MVS, VM and VSE are pretty much
   the same. You can get online information under CMS by typing:

      HELP REXX

   you should see a list of REXX bifs and keywords and a 'menu item':

      *RXSOCKET

   on the screen - 'click' on that menu item and you'll get a list of
   REXX socket functions.

   Documentation for the workstation APIs is available in form of a
   PDF document from our download page at:

      http://www.ibm.com/software/ad/rexx/download.html

   It says "Object REXX for Windows RxSock Documentation (0.4MB)", but
   the API is pretty much the same on AIX, Linux and OS/2.

   Also an tutorial and other samples can be found there.

   Visit our REXX family webpages at:

      http://www.ibm.com/software/ad/rexx/

   If you experience difficulties in using this sample you can get
   help by writing an e-mail to:

      rexxhelp@vnet.ibm.com

   Also any suggestions for improvement or bug-reports are welcome.
   HAVE FUN WITH REXX!
