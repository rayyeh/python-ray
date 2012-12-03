drop table if exists smslog;
create table smslog (
  trandate DATETIME not null,
  trantime DATETIME not null,
  pan   TEXT not null,
  pwd   TEXT,
  tel   TEXT,
  retndate TEXT,
  retncode TEXT,
  retndesc TEXT,
  msgid    TEXT,
  resp     TEXT
);
