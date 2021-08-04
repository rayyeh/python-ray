<#
    #PGM-name:filetosms.ps1 
	#Creator: Ray Yeh
	#Version 1.0
	#用途:檢查發訊檔案是否存在;若存在，要發簡訊;發訊後，將檔案刪除
	#用法:powershell.exe filetosms.ps1
	#設定 Window 工作排程，定期執行
#>


$user= "UITC04"	#SMS 帳號
$pwd = "222222" #SMS 帳號的密碼
$path = "d:\ray\whatsup.txt"  #要發簡訊的檔案路徑
$phone01 = "0912911113"
$phone02 = "0932203770"


#現在時間
$time = (Get-Date).ToString("yyyy/MM/dd H:mm:ss")

#檢查 $path 是否存在,若存在,要發簡訊
if ( Test-Path $path -PathType Leaf) {
    Write-Host "(1)I get the file:"$path
    
    Add-Type -AssemblyName System.Web
    $file_data = Get-Content $path
    $msg = 'Test MSG:' + $time + ' ' + $file_data    

    $encmsg = [System.Web.HttpUtility]::UrlEncode($msg)
    $encmsg1 =$encmsg.replace('+', ' ')
    Write-Host "(2)Message content:" $msg  #Display

    Write-Host "(3)Sending SMS"
	#phone01	
    $uri = "http://172.28.223.13:9080/SmSendGet.asp?username=$user&password=$pwd&dstaddr=$phone01&DestName=Oncall&dlvtime=0&vldtime=60&smbody=$encmsg1"
    $response =  Invoke-WebRequest -URI $uri     
	Write-Host "Phone01 SMS Response:"$response 

	#phone02
    $uri = "http://172.28.223.13:9080/SmSendGet.asp?username=$user&password=$pwd&dstaddr=$phone02&DestName=Oncall&dlvtime=0&vldtime=60&smbody=$encmsg1"
    $response =  Invoke-WebRequest -URI $uri     
	Write-Host "Phone02 SMS Response:"$response 	

    Write-Host "(4)After send SMS ,Remove File:"$path
    Remove-Item $path
    
    <# 用 msgid , 查詢發訊的狀態
    #$uri1 ="http://172.28.223.13:9080/SmQueryGet.asp?username=UITC04&password=222222&msgid=0103576111"
    #$response1 =  Invoke-WebRequest -URI $uri1
    #Write-Host "Http Response:"$response1
    #>

    
}
else{
    Write-Host "File is Empty,Have nice day"
}


