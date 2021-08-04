# Connet to Vcenter
Connect-VIServer -Server 172.30.2.220  -User administrator@vsphere.ubcard  -Password Ui@90tc!

Get-Datastore | Select-Object Name,
@{Label=”FreespaceGB”;E={“{0:n2}” -f ($_.FreespaceGB)}}, 
@{Label=”CapacityGB”;E={“{0:n2}” -f ($_.CapacityGB)}}, 
#@{Label=”Provisioned”;E={“{0:n2}” -f ($_.CapacityGB – $_.FreespaceGB +($_.extensiondata.summary.uncommitted/1GB))}},
@{Label="Free Space(%)";E={[math]::Round(($_.FreeSpaceGB)/($_.CapacityGB)*100,2)}}| Sort FreeSpaceGB -Descending


#Disconnect-VIServer * -Confirm:$false