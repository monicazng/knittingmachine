import streamlit as st
import os
import re

# Set page configuration
st.set_page_config(page_icon='🧶', page_title='Knittingmachine')
st.title(':yarn: :orange[Knittingmachine]')
st.subheader('A simple, light and clean UI to write threads.')

# Create a Tips section for correct formatting
add_tips = st.sidebar.caption('''
    🪡 __Tips__
    * Make sure to enter a thread label to save your progress.
    * Include 'http' or 'https' to URLs to help :orange[Knittingmachine] update the character count correctly.
    * Navigate and delete saved threads from the `Threads` tab.
    ''')

# Initialize 'n' session state if it's not already set
if 'n' not in st.session_state:
    st.session_state.n = 1

# Initialize 'thread_content' for each text area's content in the session state if it's not already set
if 'thread_content' not in st.session_state:
    st.session_state.thread_content = [''] * st.session_state.n 

# Initialize 'thread_label' and create a thread label input to be used as file name
if 'thread_label' not in st.session_state:
    st.session_state.thread_label = ''

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

# Define functionality to update text and save thread to a file using the thread_to_file function
def update_and_save(i):
    # Update the text in session state from the current input
    st.session_state.thread_content[i] = st.session_state[f't{i+1}']
    file_name = st.session_state.thread_label.replace(' ', '_')
    
    # Build a saved_thread list
    saved_thread = []
    for n, thread_text in enumerate(st.session_state.thread_content):
        saved_thread.append(thread_text)

    # Save the updated thread
    thread_to_file(file_name, saved_thread)

# Define functionality to save thread to a file
def thread_to_file(file_name, saved_thread):
    # Check whether or not a threads/ directory exists
    if not os.path.exists('threads'):
        os.makedirs('threads')
    
    # Page title
    file_content = ''
    
    # Add thread content to file
    for text in saved_thread:
        file_content += f'{text}\n\n'
    
    # Create new or update existing file
    with open(f'threads/{file_name}.txt', 'w') as file:
        file.write(file_content)

# Define functionality to remove the last text area
def remove_last_text_area():
    if st.session_state.n > 1:
        st.session_state.n -= 1
        st.session_state.thread_content.pop()

# Display text input for thread label
st.session_state.thread_label = st.text_input('Thread label', value=st.session_state.thread_label, placeholder='Enter a thread label to save your progress.')

# Loop through session states to display text areas and dynamically update and save their content to a file
for i in range(st.session_state.n):
    text = st.text_area(f'{i+1}', 
                        value=st.session_state.thread_content[i], 
                        key=f't{i+1}', 
                        on_change=update_and_save, 
                        args=(i,))
    display_count(st.session_state.thread_content[i])

# Buttons to add and remove a text area
col1, col2 = st.columns([.08,1])
with col1:
    st.button(':white[__＋__]', type='primary', on_click=add_text_area)

with col2:
    if st.button(':white[__—__]'):
        remove_last_text_area()
        st.rerun()