import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Event
import plotly.graph_objs as go
import pandas as pd
from collections import deque
import sqlite3

X = deque(maxlen=50)
Y1 = deque(maxlen=50)
Y2 = deque(maxlen=50)

app = dash.Dash(__name__)

app.layout = html.Div([
			html.H3('Positive reviews'),
			dcc.Graph(id='live_positive',animate=True),
			dcc.Interval(id='graph_update',interval=1000)
		]
	)

@app.callback(Output('live_positive','figure'),
	events=[Event('graph_update','interval')])

def live_update_positive():
	try:
		conn = sqlite3.connect('movie_reviews.db')
		c = conn.cursor()
		df = pd.read_sql("SELECT * FROM allPositive WHERE polarity < 0", conn)

		X = df.X_range.values[-100:]
		Y1 = df.polarity.values[-100:]
		Y2 = df.subjectivity.values[-100:]

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

		return {'data' : traces}

	except Exception as e:
		print('no')

if __name__ == '__main__':
	app.run_server(debug=True)