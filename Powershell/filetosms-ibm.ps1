<#
  read file , check file is exist, get file content and send sms
#>


$user= "UITC04"  
$pwd = "password"
$path = "d:\ray\whatsup.txt"  #message content 


$time = (Get-Date).ToString("yyyy/MM/dd H:mm:ss")
#Write-Host "Time :"$time

if ( Test-Path $path -PathType Leaf) {
    Write-Host "(1)I get the file:"$path
    
    Add-Type -AssemblyName System.Web
    $file_data = Get-Content $path
    $msg = $time + ' ' + $file_data    

    $encmsg = [System.Web.HttpUtility]::UrlEncode($msg)
    $encmsg1 =$encmsg.replace('+', ' ')
    Write-Host "(2)Message content:" $msg  #Display

    Write-Host "(3)Sending SMS"
    $uri = "http://172.28.223.13:9080/SmSendGet.asp?username=$user&password=$pwd&dstaddr=0910014182&DestName=Oncall&dlvtime=0&vldtime=60&smbody=$encmsg1"
    $response =  Invoke-WebRequest -URI $uri            
    Write-Host "(4)SMS Response:"$response 

    #Write-Host "(5)After send SMS ,Remove File:"$path
    #Remove-Item $path
    
    <# Inquery by msgid , check status 
    #$uri1 ="http://172.28.223.13:9080/SmQueryGet.asp?username=UITC04&password=222222&msgid=0103576111"
    #$response1 =  Invoke-WebRequest -URI $uri1
    #Write-Host "Http Response:"$response1
    #>

    
}
else{
    Write-Host "File is Empty,Have nice day"
}


