from textblob import TextBlob
import sqlite3

neg_polarity = []
neg_subjectivity = []

with open('negative.txt', 'r') as n:
	negative_file = n.read().split('\n')
	for line in negative_file:
		neg_analysis = TextBlob(line)
		neg_polarity.append(neg_analysis.sentiment.polarity)
		neg_subjectivity.append(neg_analysis.sentiment.subjectivity)

polarity_round = [round(i,2) for i in neg_polarity]
subjectivity_round = [round(i,2) for i in neg_subjectivity]
x_value = [i+1 for i in range(len(polarity_round))]

conn = sqlite3.connect('movie_reviews.db')
c = conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS allNegative(X_range REAL, polarity REAL, subjectivity REAL)")

def dynamic_data_entry():
	rows = zip(x_value,polarity_round,subjectivity_round)
	values = ', '.join(map(str, rows))
	c.execute("INSERT INTO allNegative(X_range, polarity, subjectivity) VALUES {}".format(values))
	conn.commit()
'''
create_table()
dynamic_data_entry()
'''
c.close()
conn.close()