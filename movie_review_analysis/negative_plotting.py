import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Event
from textblob import TextBlob
from collections import deque
import plotly.graph_objs as go

neg_polarity = []
neg_subjectivity = []

with open('negative.txt','r') as n:
	negative_file = n.read().split('\n')
	for line in negative_file:
		neg_analysis = TextBlob(line)
		neg_polarity.append(neg_analysis.sentiment.polarity)
		neg_subjectivity.append(neg_analysis.sentiment.subjectivity)

polarity_round = [round(i,2) for i in neg_polarity]
subjectivity_round = [round(i,2) for i in neg_subjectivity]

X = [i for i in range(50)]
Y1 = []
Y2 = []

#X.append(1)
Y1.append(1)
Y2.append(1)

app = dash.Dash(__name__)

app.layout = html.Div([
		html.H3('Negative Polarity and Subjectivity'),
		dcc.Graph(id='polarity_subjectivity_live',animate=True),
		dcc.Interval(id='interval_component',interval=1000)
	])

@app.callback(
		Output('polarity_subjectivity_live','figure'),
		events=[Event('interval_component','interval')]
	)

def live_polarity_subjectivity():
	X.append(X[-1]+1)
	Y1 = polarity_round
	Y2 = subjectivity_round
	traces = []
	traces.append(go.Scatter(
			x=list(X),
			y=Y1,
			name='polarity',
			mode='lines+markers'
		)
	)
	traces.append(go.Scatter(
			x=list(X),
			y=Y2,
			name='subjectivity',
			mode='lines+markers'
		)
	)
	if len(X) >= 10:
		#X.pop(0)
		polarity_round.pop(0)
		subjectivity_round.pop(0)

	return {'data' : traces}

if __name__ == '__main__':
	app.run_server(debug=True)
