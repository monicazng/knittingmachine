import streamlit as st
import os

# Set page configuration
st.set_page_config(page_icon='🧶', page_title='knittingmachine')
st.title(':yarn: :orange[knittingmachine]')
st.subheader('A simple, light and clean UI to write threads')

# Create a thread label input to be used as file name
file_name = st.text_input('Thread label', placeholder='(avoid spaces)')

# Initialize 'n' in session state if it's not already set
if 'n' not in st.session_state:
    st.session_state.n = 1

# Initialize 'thread_content' in session state if it's not already set
if 'thread_content' not in st.session_state:
    st.session_state.thread_content = [''] * st.session_state.n 

# Define functionality for each text area
def display_count(text):
    chars = len(text)
    if chars <= 280:
        st.write(f'Length: {chars} characters.')
    else:
        st.markdown(f'Length: :red[{chars}] characters.')

def add_text_area():
    st.session_state.n += 1  # Increment 'n' in session state
    st.session_state.thread_content.append('')  # Add a new empty text

# Create a variable to store the text from each text area
saved_thread = []

# Loop to display text areas, update their text, and saved it to saved_thread
for i in range(st.session_state.n):
    text = st.session_state.thread_content[i]
    text = st.text_area(f'{i+1}', placeholder='What\'s in your mind?', value=text, key=f't{i+1}')
    display_count(text)
    formatted_text = f'{i+1}: {text} - {len(text)} chars.'
    saved_thread.append(formatted_text)

# Button to add new text area
st.button('Add', type='primary', on_click=add_text_area)

# Define functionality to save thread to a .txt file
def thread_to_txt(file_name, saved_thread):
    if not os.path.exists('threads'):
        os.makedirs('threads')
    
    file_content = f"# {file_name}\n\n"
    for i in saved_thread:
        file_content += f'{i}\n\n'
    
    with open(f'threads/{file_name}.txt', 'w') as file:
        file.write(file_content)

# Button to save thread as .txt file
if st.button('Save thread'):
    thread_to_txt(file_name, saved_thread)
    st.success('Thread saved successfully to your threads directory!')