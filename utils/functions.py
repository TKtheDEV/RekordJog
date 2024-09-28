import mido
import os
import time

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def user_prompt_timeout(description, default_answer, timeout):
    start_time = time.time()
    while True:
        print(description, end=" ")
        response = input().upper()
        if response == "Y" or response == "N":
            return response
        elif response == "":
            return default_answer
        elif time.time() - start_time > timeout:
            return default_answer


def select_midi_input():
    clear_terminal()
    input_devices = mido.get_input_names()
    for i, device in enumerate(input_devices, start=1):
        print(f"{i}. {device}")

    input_choice = int(input("Select your physical controller (enter number): ")) - 1
    selected_input = input_devices[input_choice] if 0 <= input_choice < len(input_devices) else None
    return select_input


def select_midi_output():
    if os.name == 'nt':
        output_devices = mido.get_output_names()
        for i, device in enumerate(output_devices, start=1):
            print(f"{i}. {device}")

        output_choice = int(input("Select DDJ-SX (emulated controller): ")) - 1
        selected_output = output_devices[output_choice] if 0 <= output_choice < len(output_devices) else None
    else:
        selected_output = onlyForWindows
    return selected_output

