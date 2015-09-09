import MySQLdb
conn = MySQLdb.connect(db = 'CLU', host = 'localhost', user = 'root', charset ='utf8', use_unicode = True, passwd='yeswanth').cursor()
QUERY1 = 'truncate meghbeladigital_channels_bak'
QUERY2 = 'truncate meghbeladigital_lineup_bak'
QUERY3 = 'truncate meghbeladigital_locations_bak'
QUERY4 = 'truncate sumangali_channels_bak'
QUERY5 = 'truncate sumangali_lineup_bak'
QUERY6 = 'truncate sumangali_locations_bak'
QUERY7 = 'truncate ucnindia_channels_bak'
QUERY8 = 'truncate ucnindia_lineup_bak'
QUERY9 = 'truncate ucnindia_locations_bak'
conn.execute(QUERY1)
conn.execute(QUERY2)
conn.execute(QUERY3)
conn.execute(QUERY4)
conn.execute(QUERY5)
conn.execute(QUERY6)
conn.execute(QUERY7)
conn.execute(QUERY8)
conn.execute(QUERY9)
MOVE1 = 'insert into meghbeladigital_channels_bak select * from meghbeladigital_channels'
MOVE2 = 'insert into meghbeladigital_lineup_bak select * from meghbeladigital_lineup'
MOVE3 = 'insert into meghbeladigital_locations_bak select * from meghbeladigital_locations'
MOVE4 = 'insert into sumangali_channels_bak select * from sumangali_channels'
MOVE5 = 'insert into sumangali_lineup_bak select * from sumangali_lineup'
MOVE6 = 'insert into sumangali_locations_bak select * from sumangali_locations'
MOVE7 = 'insert into ucnindia_channels_bak select * from ucnindia_channels'
MOVE8 = 'insert into ucnindia_lineup_bak select * from ucnindia_lineup'
MOVE9 = 'insert into ucnindia_locations_bak select * from ucnindia_locations'
conn.execute(MOVE1)
conn.execute(MOVE2)
conn.execute(MOVE3)
conn.execute(MOVE4)
conn.execute(MOVE5)
conn.execute(MOVE6)
conn.execute(MOVE7)
conn.execute(MOVE8)
conn.execute(MOVE9)
QUER1 = 'truncate meghbeladigital_channels'
QUER2 = 'truncate meghbeladigital_lineup'
QUER3 = 'truncate meghbeladigital_locations'
QUER4 = 'truncate sumangali_channels'
QUER5 = 'truncate sumangali_lineup'
QUER6 = 'truncate sumangali_locations'
QUER7 = 'truncate ucnindia_channels'
QUER8 = 'truncate ucnindia_lineup'
QUER9 = 'truncate ucnindia_locations'
conn.execute(QUER1)
conn.execute(QUER2)
conn.execute(QUER3)
conn.execute(QUER4)
conn.execute(QUER5)
conn.execute(QUER6)
conn.execute(QUER7)
conn.execute(QUER8)
conn.execute(QUER9)

