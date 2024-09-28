import os
import mido
import configparser
import time
from functions.py import clear_terminal
from functions.py import select_midi_input
from functions.py import select_midi_output

baseconfig = configparser.ConfigParser()
controllerconfig = configparser.ConfigParser()
# hello welcome


if user_prompt_timeout("are bananas yellow (Y/n)", Y, 15) == Y:
    print("they are")
else:
    print("they arent")

