import mido
from utils.clear_terminal import clear_terminal
#while config is empty || user does not want to proceed
    #run set_baseconfig.py
#if user wants to use saved config
    #skip
#else
    #run set_baseconfig.py
#get devices and os from config


if CONFIG_IS_EMPTY:
    set_baseconfig()

while True:
    inp = input("Do you want to use the configured controller? (y/n) ")
    if inp = "y":
        break
    set_baseconfig()


#get config and store it in variables

midi_inp = mido.open_input()
