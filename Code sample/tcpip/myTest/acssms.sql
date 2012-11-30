drop table if exists smslog;
create table smslog (
  trandate DATETIME not null,
  trantime DATETIME not null,
  pan   string not null,
  pwd   string,
  tel   string,
  retndate string,
  retncode string,
  retndesc string,
  msgid    string,
  resp     string
);
