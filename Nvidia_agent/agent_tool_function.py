# Writing two python functions to read and write data to a file

# Importing the necessary libraries
import os
import json
from openai import OpenAI

# defining the function/tool to write data to a file
def write_note(content:str)-> str:
    """Saves a note or memo to a local text file."""
    with open('workspace_notes.txt',"a") as f:
        f.write(content + '\n')
    return 'Sucess:Note saved securly'
    
# defining the function/tool to read data to a file

# 2. Define a tool to read notes
def read_notes() -> str:
    """Retrieves all saved notes from the file."""
    if not os.path.exists("workspace_notes.txt"):
        return "No notes found. The file is empty."
    with open("workspace_notes.txt", "r") as f:
        return f.read()


    
    
    

