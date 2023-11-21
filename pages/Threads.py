import streamlit as st
import os

# Set page configuration
st.set_page_config(page_icon='🧶', page_title='knittingmachine/threads')
st.title(':orange[Threads]')
st.subheader('Explore your saved threads.')

# Function to list .txt documents
def list_files():
    if os.path.exists('threads'):
        return [f for f in os.listdir('threads') if f.endswith('.txt')]
    else:
        return []
file_list = list_files()

# Function to delete files
def delete_file(file_name):
    file_path = os.path.join('threads', file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
        st.success(f'*{file_name}* deleted successfully.')
    else:
        st.error(f'File "{file_name}" not found.')

# Selectbox to display chosen thread
selected_file = st.selectbox('Select a file', file_list, index=None)
if selected_file:
    file_path = os.path.join('threads', selected_file)
    with open(file_path, 'r') as file:
        file_content = file.read()
        st.markdown(file_content)
    # Button to delete file
    st.divider()
    if st.button('Delete this thread', help=':warning: This action is permanent and can\'t be undone'):
        delete_file(selected_file)
        st.rerun() # Refresh the file list and UI