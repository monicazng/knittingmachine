import streamlit as st
import os

# Set page configuration
st.set_page_config(page_icon='🧶', page_title='knittingmachine')
st.title(':yarn: knittingmachine')
st.subheader('A simple, light and clean UI to write threads.')

file_name = st.text_input('Thread label')

if 'n' not in st.session_state:
    st.session_state.n = 1

if 'thread_content' not in st.session_state:
    st.session_state.thread_content = [''] * st.session_state.n 

def display_count(text):
    chars = len(text)
    if chars <= 280:
        st.write(f'Length: {chars} characters.')
    else:
        st.markdown(f'Length: :red[{chars}] characters.')

def add_text_area():
    st.session_state.n += 1  
    st.session_state.thread_content.append('')  

def update_and_save(i):
    # Update the text in session state from the current input
    st.session_state.thread_content[i] = st.session_state[f't{i+1}']

    # Rebuild the saved_thread list
    saved_thread = []
    for j, thread_text in enumerate(st.session_state.thread_content):
        formatted_text = f'{j+1}\n{thread_text}\n{len(thread_text)} chars.\n'
        saved_thread.append(formatted_text)

    # Save the updated thread
    thread_to_txt(file_name, saved_thread)

def thread_to_txt(file_name, saved_thread):
    if not os.path.exists('threads'):
        os.makedirs('threads')
    
    file_content = f"# {file_name}\n\n"
    for text in saved_thread:
        file_content += f'{text}\n\n'
    
    with open(f'threads/{file_name}.txt', 'w') as file:
        file.write(file_content)

for i in range(st.session_state.n):
    text = st.text_area(f'{i+1}', 
                        value=st.session_state.thread_content[i], 
                        key=f't{i+1}', 
                        on_change=update_and_save, 
                        args=(i,))

    display_count(st.session_state.thread_content[i])

st.button('Add', type='primary', on_click=add_text_area)

# Add Tips section
st.write('''
    🪡 __Tips__
    * Replace spaces for '-' or '_' in your thread label to avoid formatting problems when saving your thread as a file
    * Replace URLs for 'LINK' to help :orange[knittingmachine] update the character count correctly
    ''')