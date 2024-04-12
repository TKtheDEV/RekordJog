import mido

rtmidi = mido.Backend('mido.backends.rtmidi', load=True)
midi_inp = rtmidi.open_input("DJControl Inpulse 200 0")
midi_out = rtmidi.open_output("PIONEER DDJ-SX 2")

# OUTPUT SPEED Clock 0x41-0x7F, Counter 0x39-0x01
TURN_CLOCK_SPEED = 0x44
TURN_COUNTER_SPEED = 0x3C
PIONEER_PITCH_CONTROL = 0x70

wheel_messages_counter = 3
pitch_messages_counter = 1

while True:
    ims = midi_inp.receive()
    #print(ims) #DEBUG
    if ims.type == 'control_change':
        if ims.control == 0x09 or ims.control == 0x0A:
            wheel_messages_counter += 1
            # Process every fourth message, otherwise laggy in RB6
            if wheel_messages_counter % 4 == 0:
                if ims.value == 0x01:
                    midi_out.send(mido.Message('control_change', channel=ims.channel, control=ims.control, value=TURN_CLOCK_SPEED))
                elif ims.value == 0x7F:
                    midi_out.send(mido.Message('control_change', channel=ims.channel, control=ims.control, value=TURN_COUNTER_SPEED))

        elif ims.control == 0x08:
            inverted_value = 127 - ims.value  # Invert the value
            midi_out.send(mido.Message('control_change', control=PIONEER_PITCH_CONTROL, value=inverted_value, channel=ims.channel))


    if ims.type == 'note_on' or ims.type == 'note_off':
        midi_out.send(mido.Message(ims.type, channel=ims.channel, note=ims.note, velocity=ims.velocity))