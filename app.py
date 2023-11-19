import streamlit as st
import os
import re

# Set page configuration
st.set_page_config(page_icon='🧶', page_title='knittingmachine')
st.title(':yarn: knittingmachine')
st.subheader('A simple, light and clean UI to write threads.')

# Create a thread label input to be used as file name for the save thread functionality
file_name = st.text_input('Thread label')

# Initialize 'n' session state if it's not already set
if 'n' not in st.session_state:
    st.session_state.n = 1

# Initialize 'thread_content' for each text area's content in the session state if it's not already set
if 'thread_content' not in st.session_state:
    st.session_state.thread_content = [''] * st.session_state.n 

# Define functionality for character count
def display_count(text):
    # Count URLs as 23 characters
    url_regex = r'https?://\S+'
    urls = re.findall(url_regex, text)
    url_count = 23 * len(urls)
    
    # Remove URLs from text to avoid double counting
    text_without_urls = re.sub(url_regex, '', text)
    
    # Count characters, treating each emoji as 2 characters
    chars = sum(2 if ord(c) > 0xffff else 1 for c in text_without_urls)
    
    # Add URL count
    chars += url_count
    
    # Display formatted character count
    if chars <= 280:
        st.write(f'Length: {chars} characters.')
    else:
        st.markdown(f'Length: :red[{chars}] characters.')

# Define functionality to add text areas to the thread
def add_text_area():
    st.session_state.n += 1  
    st.session_state.thread_content.append('')  

# Define functionality to update text and save thread to a file using the thread_to_txt function
def update_and_save(i):
    # Update the text in session state from the current input
    st.session_state.thread_content[i] = st.session_state[f't{i+1}']

    # Build a saved_thread list
    saved_thread = []
    for n, thread_text in enumerate(st.session_state.thread_content):
        formatted_text = f'{n+1}\n{thread_text}\n{len(thread_text)} chars.\n'
        saved_thread.append(formatted_text)

    # Save the updated thread
    thread_to_txt(file_name, saved_thread)

# Define functionality to save thread to a file
def thread_to_txt(file_name, saved_thread):
    if not os.path.exists('threads'):
        os.makedirs('threads')
    
    file_content = f"# {file_name}\n\n"
    for text in saved_thread:
        file_content += f'{text}\n\n'
    
    with open(f'threads/{file_name}.txt', 'w') as file:
        file.write(file_content)

# Loop through session states to display text areas and dynamically update and save their content to a file
for i in range(st.session_state.n):
    text = st.text_area(f'{i+1}', 
                        value=st.session_state.thread_content[i], 
                        key=f't{i+1}', 
                        on_change=update_and_save, 
                        args=(i,))

    display_count(st.session_state.thread_content[i])

# Button to add new text area
st.button('\+ Text', type='primary', on_click=add_text_area)

# Create a Tips section for correct formatting
st.write('''
    🪡 __Tips__
    * Replace spaces for '-' or '_' in your thread label to avoid formatting problems when saving your thread as a file
    * Type URLs with 'http' or 'https' to help :orange[knittingmachine] update the character count correctly
    ''')