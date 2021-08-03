import sqlite3
def get_connection():
	con = sqlite3.connect()
	return con, con.cursor()

def close_connection(con):
	con.close()

def commit_connection(con):
	con.commit()

def customer_insert(data):
	name=data.get("name", '')
	age = data.get("age", 0)
	q=f"insert into customer values('{name}',{age})"
	con,cur = get_connection()
	cur.execute(q)
	commit_connection(con)
	close_connection(con)
