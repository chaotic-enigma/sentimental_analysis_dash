import dash
import dash_core_components as dcc
import dash_html_components as html
from textblob import TextBlob

polarity_value = []
subjectivity_value = []

with open('restaurant-review.txt','r') as rs:
	reviews = rs.read().split('\n')
	for line in reviews:
		khana = TextBlob(line)
		polarity_value.append(khana.sentiment.polarity)
		subjectivity_value.append(khana.sentiment.subjectivity)
'''
print(polarity_value,len(polarity_value))
print(subjectivity_value,len(subjectivity_value))
'''

polarity_round = [round(i,2) for i in polarity_value]
subjectivity_round = [round(i,2) for i in subjectivity_value]
x_range = [i+1 for i in range(len(polarity_round))]

'''
print(polarity_round)
print(subjectivity_round)
'''

app = dash.Dash(__name__)

app.layout = html.Div([
		html.H3('Restaurant sentimental analysis'),
		dcc.Graph(id='khana_sentiment',
				figure={
					'data' : [
						{'x' : x_range,'y' : polarity_round,'type' : 'line','name' : 'polarity'},
						{'x' : x_range,'y' : subjectivity_round,'type' : 'line','name' : 'subjectivity'}
					]
				}
			)
	])



if __name__ == '__main__':
	app.run_server(debug=True)