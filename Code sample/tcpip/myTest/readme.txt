1.myTest 是實驗 Flask web framework 的folder
2.交易curl1.py <---> http-flask.py  <----> sms-flask.py
=============================================================
3.httpserver.py - nativate python http server ,效能很慢
4.http-thread - nativate python http server +thread mode,效能很慢
5.http-flask.py -- flask+gevent +sqlite3
6.http-tornado.py -- flask + Tornado +sqlite3(sqlite3 缺乏安控與concurrency process 功能)
7.http-mongokit.py - 是flask+gevent+mongokit (使用mongodb)
8.http-pymongo.py -- flask+gevent+pymongo (使用 mongodb)
9.http-flask.py 要先執行 set ACSSMS_SETTINGS=settings.ini 
============================================================
8.smsserver.py -nativate python http server ,效能很慢
9.sms-thread.py -nativate python http server +thread mode,效能很慢
10.sms-flask.py - flask+gevent, 效能可以


