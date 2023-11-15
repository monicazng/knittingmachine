# 🧶 knittingmachine <img alt="Python: 3.11" src="https://img.shields.io/badge/python-3.11-blue.svg" target="_blank"/> <img alt="License: GNU GPL v2" src="https://img.shields.io/badge/license-GNU_GPL_v2-blue.svg" target="_blank"/>

A simple, light, and clean UI to write threads — built with Python and Streamlit.

## Motivation
I enjoy writing threads more than single posts because it lets me develop storytelling. However, I found the interface of X and third-party applications too distrating for the task. So I decided to use my recently acquired Python skills to build a simple, light, and clean UI to write and save threads locally. As a more-junior-than-junior developer building my first-ever app, expect very rough code. 

## Features
* Add subsequent text areas to your thread
* Text areas feature character count with a color warning when you exceed the 280 character limit
* Save your thread locally as a `thread_label.txt` file

## Installing knittingmachine

### Prerequisits
* [Python 3.11](https://www.python.org/downloads/)
* [Streamlit](https://docs.streamlit.io/library/get-started/installation)

### Set up your environment
Regardless of which package management tool you're using, I recommend running the commands on this page in a virtual environment. This ensures that the dependencies pulled in for knittingmachine don't impact any other Python projects you're working on.

### Install and run knittingmachine
1. Navigate to your project directory:

    `cd your_project_directory`
2. Activate your virtual environment
3. Install project requirements:
    
    `pip install -r requirements.txt`
4. Test that you have Streamlit installed:
    
    `streamlit hello`
5. Streamlit's Hello app should appear in a new tab in your web browser! To stop the Streamlit server, press ctrl-C.
6. Create a local [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) of knittingmachine to your project directory:
    
    `git clone https://github.com/monicazng/knittingmachine`
7. Now you can use Python and Streamlit to run knittingmachine locally!
    
    `streamlit run app.py`
    A new tab in your web browser should pop up running knittingmachine locally!

Remember that this is app runs locally on your computer. With the current implementation, threads are stored in the session state and you'll lose the content if you refresh the page.

To save the thread, click the `Save thread` button. This will check whether or not there's a `threads/` folder in your project directory, create one if it doesn't exist, and save your thread as a `thread_label.txt` file. You can continue editing via the app during the same session and click `Save thread` to update the files with the changes. 

## Roadmap

### Immediate improvements
- [ ] Save thread using the `text_area` `on_change` variable instead of using the `Save thread` button
- [ ] Character count: add emoji count exception
- [ ] Character count: add URL count exception
- [ ] Add sidemenu navigation for saved threads

### Future improvements
- [ ] Multipage: turn knittingmachine on a multipage app where each saved thread is a page instead of a `.txt` file
- [ ] Saved threads: add editing and remove functionality
- [ ] Saved threads: add change text order functionality

## Contributions
Contributions, issues and feature requests are welcome.

## Author
* Twitter: [@monicazng](https://twitter.com/monicazng)
* Github: [@monicazng](https://github.com/monicazng)

## License
This project is [GNU GPL v2](https://github.com/monicazng/knittingmachine/LICENSE) licensed.