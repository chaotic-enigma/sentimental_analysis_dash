from textblob import TextBlob
import sqlite3

pos_polarity = []
pos_subjectivity = []

with open('positive.txt', 'r') as p:
	positive_file = p.read().split('\n')
	for line in positive_file:
		pos_analysis = TextBlob(line)
		pos_polarity.append(pos_analysis.sentiment.polarity)
		pos_subjectivity.append(pos_analysis.sentiment.subjectivity)

polarity_round = [round(i,2) for i in pos_polarity]
subjectivity_round = [round(i,2) for i in pos_subjectivity]
x_value = [i+1 for i in range(len(polarity_round))]

conn = sqlite3.connect('movie_reviews.db')
c = conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS allPositive(X_range REAL, polarity REAL, subjectivity REAL)")

def dynamic_data_entry():
	rows = zip(x_value,polarity_round,subjectivity_round)
	values = ', '.join(map(str, rows))
	c.execute("INSERT INTO allPositive(X_range, polarity, subjectivity) VALUES {}".format(values))
	conn.commit()
'''
create_table()
dynamic_data_entry()
'''
c.close()
conn.close()