Tasks
- Make your own application in Russian on the Streamlit platform with data on Apple quotes using the yfinance library
- Take your research on tips (dataset tips.csv) and visualize it on the Streamlit platform# sheina-streamlit

Create an app

1. The first step is to create a new Python script - app.py.

2. Open app.py in your favorite IDE or text editor, then add these lines:

import streamlit as st
import pandas as pd
import numpy as np
Every good app has a title, so let's add one:

st.title('Uber pickups in NYC')
Now it's time to run Streamlit from the command line:

streamlit run uber_pickups.py
Running a Streamlit app is no different than any other Python script. Whenever you need to view the app, you can use this command.
