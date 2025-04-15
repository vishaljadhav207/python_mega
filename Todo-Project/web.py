import streamlit as st #stramlit for webapps
import functions

todos=functions.get_todos()

st.title("My todo app")
st.subheader("This is my todo app")
st.write("Hello user")

for index, todo in enumerate(todos):
    st.checkbox(todo, key=f"todo_{index}")

st.text_input(label="enter todo",placeholder="Enter todo...")


