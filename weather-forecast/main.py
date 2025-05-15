import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather forecast for the next days")
place=st.text_input("Place: ")
days=st.slider("Forecast Days:",min_value=1,max_value=5,
               help="select no of forecast days")

option=st.selectbox("Select data to view",
                    ("temperature","sky"))
st.subheader(f"{option} for the next {days} data in {place}")

data=get_data(place,days,option)


figure=px.line(x=d,y=t,labels={"x":"date","y":"temperature(c)"})
st.plotly_chart(figure)