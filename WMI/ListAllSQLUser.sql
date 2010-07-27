/**
Script: list all Usernames, Roles for all the databases.
Author: Shiva Challa (http://challa.info)
and the database Roles that the user belongs to in all the databases. 
Also, you can use this script to get the roles of one user in all the databases. 

Directions of Use:
For All Users list: You can directly run this script in SQL Server Management studio
For a specific user:
	1. Find this code and u.name like ''tester''
	2. Uncomment the code 
	3. Replace the Name ''tester'' with the username you want to search on. 

Resultset:
	DBName: Database name that the user exists in.
	Name: user name.
	GroupName: Group/Database Role that the user is a part of. 
	LoginName: Actual login name, if this is null, Name is used to connect.
		default_database_name
		default_schema_name
		principal_id
		sid

Change History:
8/26/2008    Removed the misc characters from the "Select of EXEC sp_MSForEachdb" statement. 


9/2/2008 Cathy Greenselder - Convert to SQL2000
		(default_database_name  not in SQL2K)
		(default_schema_name	not in SQL2K)
		(principal_id           not in SQL2K)
		 uid                    is in SQL2K

**/

USE MASTER
GO

BEGIN

IF  EXISTS (SELECT * FROM dbo.sysobjects 
                     WHERE id = OBJECT_ID(N'[dbo].#TUser') 
                       AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
DROP TABLE #TUser

CREATE TABLE #tuser (
 DBName VARCHAR(50),
 UserName SYSNAME,
 GroupName SYSNAME NULL,
 LoginName SYSNAME NULL,
 uid INT,
 sid VARBINARY(85))

INSERT INTO #TUser
EXEC sp_MSForEachdb
 '
 SELECT ''?'' as DBName,
        u.name As UserName,
        CASE 
                WHEN (r.uid IS NULL) THEN ''public''
                ELSE r.name
                END  AS GroupName,
        l.name AS LoginName,
        u.uid,
        u.sid
 FROM ?.dbo.sysUsers u
        LEFT JOIN (?.dbo.sysMembers m
                         JOIN ?.dbo.sysUsers r
                                ON m.memberuid = r.uid)
        ON m.memberuid = u.uid
        LEFT JOIN dbo.sysLogins l
        ON u.sid = l.sid
WHERE u.islogin = 1 OR u.isntname = 1 OR u.isntgroup = 1
 /*and u.name like ''tester''*/
 ORDER BY u.name
 '

SELECT *
FROM #TUser
ORDER BY DBName,
 UserName,
 GroupName

DROP TABLE #TUser
END
