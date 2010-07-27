select tablename =object_name(parent_obj),* from sysobjects
where type ='tr'