import streamlit as st  # stramlit for webapps
from streamlit import session_state

import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)




st.title("My todo app")
st.subheader("This is my todo app")
st.write("Hello user")

for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        if todo and todo in st.session_state:
            del st.session_state[todo]
        st.rerun()

st.text_input(label="enter todo", placeholder="Enter todo...",
              on_change=add_todo, key="new_todo")
