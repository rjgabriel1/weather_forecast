import streamlit as st
import plotly.express as px
from data import get_weather_data

st.title("Weather Forecast")

place = st.text_input(label="Place:", placeholder="enter a place")
days = st.slider(label="Forecast Days", min_value=1, max_value=5,
                 step=1, help='select the number of days')

option = st.selectbox("Select weather info to view",
                      ["Temperature", "Sky"], )
print(option, days)

st.subheader(f"{option} for the next {days} days in {place}")


# def get_weather_data(_days):
#     dates = ["2023-25-08", "2023-26-08", "2023-27-08"]
#     temperatures = [12, 20, 16]
#     temperatures = [days * temp for temp in temperatures]
#     return dates, temperatures


d, t = get_weather_data(days)

figure = px.line(x=d, y=t,
                 labels={"x": "Date", "y": "Temperatures"})
st.plotly_chart(figure_or_data=figure)
