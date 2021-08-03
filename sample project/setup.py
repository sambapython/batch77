import db 
con,cur = db.get_connection()
q="create table if not exists customer(name varchar(250), age integer)"
cur.execute(q)
