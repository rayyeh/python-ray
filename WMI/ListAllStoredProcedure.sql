select name as spname
from sysobjects
where (xtype='p') and (name NOT LIKE 'dt%')
Order BY name

exec sp_stored_procedures 

