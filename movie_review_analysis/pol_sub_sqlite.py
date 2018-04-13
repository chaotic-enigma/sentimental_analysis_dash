import sqlite3

x_value = [i+1 for i in range(22)]
pol = [1,2,3,4,1,2,3,1,4,2,5,3,6,3,6,3,1,3,2,4,6,4]
sub = [1,2,3,1,4,2,3,4,2,4,2,5,6,4,6,3,6,4,3,5,6,2]

conn = sqlite3.connect('movie_reviews.db')
c = conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS allReviews(X_range REAL, polarity REAL, subjectivity REAL)")

def dynamic_data_entry():
	rows = zip(x_value,pol,sub)
	values = ', '.join(map(str, rows))
	c.execute("INSERT INTO allReviews (X_range, polarity, subjectivity) VALUES {}".format(values))
	conn.commit()

create_table()
dynamic_data_entry()

c.close()
conn.close()