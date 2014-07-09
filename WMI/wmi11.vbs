@echo off
if %os%==Windows_NT goto WINNT
goto NOCON

:WINNT
echo .Using a Windows NT based system
echo ..%computername%

REM set variables
set system=
set manufacturer=
set model=
set serialnumber=
set osname=
set sp=
set cstring=
set ustring=
set pstring=

REM Get Computer Name / IP Address
echo ----------------
echo Type in a Computer Name or IP Address and press Enter
set computer=%computername%
set /p computer=[Press Enter For %computername%] 
echo ----------------

REM Check If Remote Machine
IF NOT %computer% == %computername% goto remote
goto start

:REMOTE
REM It's A Remote Machine
set cstring=/node:"%computer%"

:USERNAME
REM Get Username
echo ----------------
echo Type in a Username and press Enter (with or without DOMAIN)
set user=%username%
set /p user=[Press Enter For %username%] 
echo ----------------

REM Check If Other Username
IF NOT %user% == %username% goto newuser
goto start

:NEWUSER
REM It's A Different User
set ustring=/user:"%user%"

:PASSWORD
REM Get Password
echo ----------------
echo Type in a Password and press Enter (with or without DOMAIN)
set pass=
set /p pass= 
echo ----------------

REM Check if password was entered
IF [%pass%] == [] goto nopass
set pstring=/password:"%pass%"
goto start

:NOPASS
REM No password entered
set pstring=

:START
cls
echo Checking connection [Computer: %computer%]...
echo Please Wait....

REM Check connection
wmic %cstring% %ustring% %pstring% OS Get csname

IF %errorlevel% == -2147023174 goto norpc
IF %errorlevel% == -2147024891 goto baduser

echo Getting data [Computer: %computer%]...
echo Please Wait....

REM Get Computer Name
FOR /F "tokens=2 delims='='" %%A in ('wmic %cstring% %ustring% %pstring% OS Get csname /value') do SET system=%%A

REM Get Computer Manufacturer
FOR /F "tokens=2 delims='='" %%A in ('wmic %cstring% %ustring% %pstring% ComputerSystem Get Manufacturer /value') do SET manufacturer=%%A

REM Get Computer Model
FOR /F "tokens=2 delims='='" %%A in ('wmic %cstring% %ustring% %pstring% ComputerSystem Get Model /value') do SET model=%%A

REM Get Computer Serial Number
FOR /F "tokens=2 delims='='" %%A in ('wmic %cstring% %ustring% %pstring% Bios Get SerialNumber /value') do SET serialnumber=%%A

REM Get Computer OS
FOR /F "tokens=2 delims='='" %%A in ('wmic %cstring% %ustring% %pstring% os get Name /value') do SET osname=%%A
FOR /F "tokens=1 delims='|'" %%A in ("%osname%") do SET osname=%%A

REM Get Computer OS SP
FOR /F "tokens=2 delims='='" %%A in ('wmic %cstring% %ustring% %pstring% os get ServicePackMajorVersion /value') do SET sp=%%A

echo done!

echo ----------------
echo System Name: %system%
echo Manufacturer: %manufacturer%
echo Model: %model%
echo Serial Number: %serialnumber%
echo Operating System: %osname%
echo Service Pack: %sp%
echo ----------------

REM Generate file
SET file="%~dp0%computer%.txt"
echo ---------------- > %file%
echo Details For %computer%: >> %file%
echo System Name: %system% >> %file%
echo Manufacturer: %manufacturer% >> %file%
echo Model: %model% >> %file%
echo Serial Number: %serialnumber% >> %file%
echo Operating System: %osname% >> %file%
echo Service Pack: %sp% >> %file%
echo ---------------- >> %file%

echo File created at %file%

REM request user to push any key to continue
pause

goto END

:NORPC
echo ----------------
echo Error...No connection could be made to [%computer%]...
echo Error...Please try again...
echo ----------------
pause
cls
goto winnt

:BADUSER
echo ----------------
echo Error...Access Denied using [%user%]...
echo Error...Please try again...
echo ----------------
pause
cls
goto username

:NOCON
echo ----------------
echo Error...Invalid Operating System...
echo Error...No actions were made...
echo ----------------
pause
goto END

:END