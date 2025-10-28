# Wordle

## Overview
Standard game of Wordle but, behind the scenes this is my attempt to use various 
design patterns in order to: (1) learn the Python programming and (2) way over 
complicate things.


## Requirements
Only dependency is pygame or pygame-ce (works for both and choice is up top you). After 
cloning the repository you will need to open your favorite terminal and:

Create a virtual environment:

    python3 -m venv <add_your_venv_name>


If python3 does not work: for zshell and bash

    echo 'export PATH="/path/to/python3/bin:$PATH"' >> ~/.zshrc

If python3 does not work: for fish

    echo 'export PATH="/path/to/python3/bin:$PATH"' >> ~/.config/fish/config.fish

I do not use use windows, in this case google is your friend.

Activate the virtual environment (linux or mac)

    source venv/bin/activate
    
Activate the virtual environment (windows)

    venv\Scripts\activate.bat (cmd)
    venv\Scripts\Activate.ps1 (powershell)
    
Add Pygame

    pip install pygame-ce (or pygame)


## Running Wordle
Using your terminal of choice, navigate to the base/root project directory and type:
    
    python3 main.py


## Contact
Use however you want and let me know if you have any questions or comments at 
ham_bone_willy@yahoo.com 


## Special Thanks
Thanks to DarkerMango for the list of five-letter words (https://github.com/darkermango/5-Letter-words).
