'''
For the Band approximation using Numpy Poly fit

'''


import streamlit as st
import numpy as np 
import pandas as pd
import scipy.integrate as integrate
from PIL import Image
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show
import plotly.graph_objects as go

st.image('csi-pacific-logo-reverse.png', width = 150)
st.title("Band Force-Length Calculator")
uploaded_data = st.file_uploader('Load Band Data Here')



if uploaded_data is not None:
	data = uploaded_data
	data = pd.read_csv(data, skiprows=1)
	length = data.iloc[:,0]
	length = length[0:19]

	band_select = st.selectbox("Select Band Brand",
		('-- Select Data Type -- ', 'Rogue','Sorinex'))

	if band_select == '-- Select Data Type -- ':
		data = st.empty()

	if band_select == 'Rogue': 
		col_select = st.selectbox('Select Colour',
			('-- Select Colour --', 'Orange', 'Red', 'Green'))

		if col_select == 'Orange':
			data = data.iloc[:,1]
		if col_select == 'Red':
			data = data.iloc[:,2]
		if col_select == 'Green':
			data = data.iloc[:,3]

	if band_select == 'Sorinex': 
		col_select = st.selectbox('Select Colour',
			('-- Select Colour --', 'Orange', 'Red', 'Purple', 'Green'))

		if col_select == 'Orange':
			data = data.iloc[:,4]
		if col_select == 'Red':
			data = data.iloc[:,5]
		if col_select == 'Purple':
			data = data.iloc[:,6]
		if col_select == 'Green':
			data = data.iloc[:,7]

	data = data[0:19]
	fit = np.polyfit(length,data,2)
	fit = pd.DataFrame(fit)

	fit_x = []
	for i in range(250):
		fit_x.append(i+1)
	
	fit_x = np.array(fit_x)

	fit_y = fit_x**2 *fit[0][0] + fit_x*fit[0][1] + fit[0][2]
	
	

	band_length = st.number_input("Length Input", min_value = 0)

	if band_length is not 0: 
		st.subheader('Fitted force at given length')
		st.write(fit_y[band_length])

	st.header("Polynomial fit Plot")
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=length, y=data,
                    mode='markers',
                    name='Measured Points'))
	fig.add_trace(go.Scatter(x=fit_x, y=fit_y,
                    mode='lines',
                    name='Fitted Curve'))
	fig.update_layout(title = "Poly Fit Plot", 
							xaxis_title = 'Length (cm)', 
							yaxis_title = 'Force (N)')
	st.plotly_chart(fig)



