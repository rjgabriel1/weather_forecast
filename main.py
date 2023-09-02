import streamlit as st
import plotly.express as px
from data import get_weather_data


# Add page title , input boxes, slider and selectbox
st.title("Weather Forecast")

place = st.text_input(label="Place:", placeholder="enter a place")
days_count = st.slider(label="Forecast Days", min_value=1, max_value=5,
                 step=1, help='select the number of days')

option = st.selectbox("Select weather info to view",
                      ["Temperature", "Sky"], )


subheader_text = f"{option} for the next {days_count} days in {place}"
st.subheader(subheader_text)



if place:
    # Get temperaure/sky data
    try:
         filtered_data = get_weather_data(place, days_count)
  
         match option:
            case 'Temperature':
                temperatures = [result['main']['temp']
                                for result in filtered_data]
                dates = [result['dt_txt'] for result in filtered_data]
                figure = px.line(x=dates, y=temperatures,
                                labels={"x": "Date", "y": "Temperatures"})
                st.plotly_chart(figure_or_data=figure)
        
            case 'Sky':
                images ={
                    'Clear':'images/clear.png',
                    'Clouds':'images/cloud.png',
                    'Rain': 'images/rain.png',
                    'Snow':'images/snow.png'
                }
                sky_conditons = [result['weather'][0]['main']
                                for result in filtered_data]
                images_paths=[images[condition] for condition in sky_conditons]
                st.image(images_paths, width=115)
    except KeyError:
        st.write('Invalid City name')
