import win32com.client
strComputer = "."
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
colItems = objSWbemServices.ExecQuery("Select * from Win32_NTDomain")
for objItem in colItems:
    print "Caption: ", objItem.Caption
    print "Client Site Name: ", objItem.ClientSiteName
    print "Creation Class Name: ", objItem.CreationClassName
    print "Dc Site Name: ", objItem.DcSiteName
    print "Description: ", objItem.Description
    print "Dns Forest Name: ", objItem.DnsForestName
    print "Domain Controller Address: ", objItem.DomainControllerAddress
    print "Domain Controller Address Type: ", objItem.DomainControllerAddressType
    print "Domain Controller Name: ", objItem.DomainControllerName
    print "Domain Guid: ", objItem.DomainGuid
    print "Domain Name: ", objItem.DomainName
    print "DS Directory Service Flag: ", objItem.DSDirectoryServiceFlag
    print "DS Dns Controller Flag: ", objItem.DSDnsControllerFlag
    print "DS Dns Domain Flag: ", objItem.DSDnsDomainFlag
    print "DS Dns Forest Flag: ", objItem.DSDnsForestFlag
    print "DS Global Catalog Flag: ", objItem.DSGlobalCatalogFlag
    print "DS Kerberos Distribution Center Flag: ", objItem.DSKerberosDistributionCenterFlag
    print "DS Primary Domain Controller Flag: ", objItem.DSPrimaryDomainControllerFlag
    print "DS Time Service Flag: ", objItem.DSTimeServiceFlag
    print "DS Writable Flag: ", objItem.DSWritableFlag
    print "Install Date: ", objItem.InstallDate
    print "Name: ", objItem.Name
    print "Name Format: ", objItem.NameFormat
    print "Primary Owner Contact: ", objItem.PrimaryOwnerContact
    print "Primary Owner Name: ", objItem.PrimaryOwnerName
    z = objItem.Roles
    if z is None:
        a = 1
    else:
        for x in z:
            print "Roles: ", x
    print "Status: ", objItem.Status
