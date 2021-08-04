$EmailFrom = “rayyeh@uitc.com.tw”
$EmailTo = “rayyeh@uitc.com.tw”
$Subject = “The subject of your email”
$Body = “What do you want your email to say”
$SMTPServer = “192.168.10.5”

$SMTPClient = New-Object Net.Mail.SmtpClient($SMTPServer, 587)
$SMTPClient.EnableSsl = $true
$SMTPClient.Credentials = New-Object System.Net.NetworkCredential(“rayyeh@uitc.com.tw”, “YEHray06!”);
$SMTPClient.Send($EmailFrom, $EmailTo, $Subject, $Body)