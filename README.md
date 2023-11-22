# 🧶 Knittingmachine <img alt="Python: 3.11" src="https://img.shields.io/badge/python-3.11-blue.svg" target="_blank"/> <img alt="License: GNU GPL v2" src="https://img.shields.io/badge/license-GNU_GPL_v2-blue.svg" target="_blank"/>

A simple, light, and clean UI to write threads — built with Python and Streamlit.

## Motivation
I've always preferred the depth and narrative flow of threads over single posts. However, the existing interfaces and third-party apps felt too cluttered and distracting for this purpose. This led me to test my newly acquired Python skills into creating a simple, clean, and intuitive UI for writing and managing threads. Bear in mind, the code may be a bit unpolished, but it's a genuine reflection of my learning journey building my first app!

## Features
* Label and write threads that auto-save in a `thread_label.txt` local file
* Add and remove text areas from your thread
* Text areas feature character count with a color warning when you exceed the 280 character limit
* Character count manages URL and emoji count exceptions
* Navigate and delete saved threads from the `Threads` tab

## Installing Knittingmachine

### Prerequisits
* [Python 3.11](https://www.python.org/downloads/)
* [Streamlit](https://docs.streamlit.io/library/get-started/installation)

### Set up your environment
Regardless of which package management tool you're using, I recommend running the commands on this page in a virtual environment. This ensures that the dependencies pulled in for Knittingmachine don't impact any other Python projects you're working on.

### Install and run Knittingmachine
1. Navigate to your project directory:

    `cd your_project_directory`
2. Activate your virtual environment
3. Install project requirements:
    
    `pip install -r requirements.txt`
4. Test that you have Streamlit installed:
    
    `streamlit hello`
5. Streamlit's Hello app should appear in a new tab in your web browser! To stop the Streamlit server, press ctrl-C.
6. Create a local [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) of Knittingmachine to your project directory:
    
    `git clone https://github.com/monicazng/knittingmachine`
7. Now you can use Python and Streamlit to run Knittingmachine locally!
    
    `streamlit run app.py`
    
    A new tab in your web browser should pop up running Knittingmachine locally!

Remember that this is app runs locally on your computer. 

## Limitations
* When the thread label is empty and a text area is edited, an empty name `.py` file is created with no warning and subsequent threads following this pattern will replace the content of previous threads with no thread label
* When the thread label is filled after a text area has been edited, a `thread_label.py` file is created but it won't show in the `Threads` dropdown until a new text area is created or the app is refreshed
* Since images don't affect the character count, they have been disregarded in this implementation

## Roadmap
- [X] Saved threads: add delete thread functionality
- [ ] New threads: add change text order functionality
- [ ] Saved threads: addd editing functionality

## Contributions
Contributions, issues and feature requests are welcome.

## Author
* Twitter: [@monicazng](https://twitter.com/monicazng)
* Github: [@monicazng](https://github.com/monicazng)

## License
This project is [GNU GPL v2](https://github.com/monicazng/knittingmachine/blob/master/LICENSE) licensed.