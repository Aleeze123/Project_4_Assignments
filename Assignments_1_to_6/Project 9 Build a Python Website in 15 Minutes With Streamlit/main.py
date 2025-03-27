import streamlit as st
st.title("Welcome to Aleeza's To-Do List 📝")
st.write("This is a simple To-Do List web app built using **Streamlit**. You can add, delete, and view your tasks.")
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []
def add_task(task):
    st.session_state['tasks'].append(task)
def delete_task(task):
    if task in st.session_state['tasks']:
        st.session_state['tasks'].remove(task)

st.header("Add a Task ✍️")
task = st.text_input("Enter a task:", "")
if st.button("Add Task"):
    if task:
        add_task(task)
        st.success(f"Task '{task}' added!")
    else:
        st.warning("Please enter a task before adding.")
st.header("Your To-Do List 📋")
if st.session_state['tasks']:
    for idx, task in enumerate(st.session_state['tasks'], 1):
        st.write(f"{idx}. {task}")
        if st.button(f"Delete Task {idx}"):
            delete_task(task)
            st.success(f"Task '{task}' deleted!")
else:
    st.write("No tasks yet! Start adding tasks above.")
st.write("Thanks for using Aleeza's To-Do List Web App! 🚀")
