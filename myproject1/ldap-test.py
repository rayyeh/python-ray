import ldap,sys,os
try:
    l = ldap.initialize('ldap://192.168.10.71')
    l.protocol_version = ldap.VERSION3
    username = "CN=葉清宏,CN=Users,DC=uitctest,DC=com,DC=tw"
    password  = "p@ssw0rd"
    l.simple_bind_s(username, password)
    print 'login successfully'
    base_dn = 'CN=Users,DC=uitctest,DC=com,DC=tw'
    filter = '(sAMAccountName=rayyeh)'
    attrs = ['sn']
    results = l.search_s( base_dn, ldap.SCOPE_SUBTREE, filter, attrs )
    if len(results) == 0:
        print 'Can not find in AD'
    else:
        print results[0]
        for i in results[0]:
            print i
	
except ldap.INVALID_CREDENTIALS:
    print "Your username or password is incorrect."
    sys.exit()
    



     
  
