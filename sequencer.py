import pianohat
import time
import threading
from pygame import mixer
import settings

pianohat.auto_leds(False)
pianohat.set_led(13, False)
pianohat.set_led(14, True)
pianohat.set_led(15, True)

# 120 beats per minute is 0.125 sec per position
bpm = 0.125
bank = 1
position = 0

mixer.init(22050, -16, 2, 512)
mixer.set_num_channels(13)

validkeys = [0,2,4,5,7,9,11,12]
keymap = [0,0,1,1,2,3,3,4,4,5,5,6,7]
sounds = []
recordings = [[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1]]

# begin wit a basic beat
# recordings = [[1,0],[0,-1],[0,-1],[0,-1],[1,0],[0,-1],[0,-1],[0,-1]]
rec = True
# todo recording moet arrays en bank bevatten, meer sounds simultaan

def handleNote(key, pressed):
    global position
    global rec
    global bank
    if pressed and (key in validkeys):
        index = keymap[key]
        print("position {} bank {} key {}".format(position, bank, key))
        
        if(rec == True):
            recordings[position][0] = bank
            recordings[position].append(index)
        else :
            sounds[bank][index].play(loops=0)

# pass over all 8 positions, light the led, play recorded sound
def nextStep():
    global position
    recarray = recordings[position]
    recbank = recarray[0]
    # check if there is a recording
    if(recbank != -1):
        # todo play all sounds not just 1
        # sounds[recbank][i].play(loops=0)
        for index in range(1, len(recarray)):
            sounds[recbank][recarray[index]].play(loops=0)

    #led
    pianohat.set_led(validkeys[position], False)
    position+=1
    if(position == 8):
        position = 0
    pianohat.set_led(validkeys[position], True)
    # next
    threading.Timer(bpm, nextStep).start()

# change bank and erase recording
def changeSettings(ch, evt):
    global bank
    global recordings
    global rec
    if(evt == True): 
        if(ch == 13):
            bank = 0
            pianohat.set_led(13, True)
            pianohat.set_led(14, False)
        if(ch == 14):
            bank = 1
            pianohat.set_led(13, False)
            pianohat.set_led(14, True)
        # toggle record on off, off also erases
        if(ch == 15):
            if(rec == True):
                rec = False
                recordings = [[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1]]
                pianohat.set_led(15, False)
            else:
                rec = True
                pianohat.set_led(15, True)
            



# create sound objects for all .wav files
sounds.append(settings.createSoundObjects(settings.files1))
sounds.append(settings.createSoundObjects(settings.files2))

# piano key handlers
pianohat.on_octave_up(changeSettings)
pianohat.on_octave_down(changeSettings)
pianohat.on_instrument(changeSettings)

pianohat.on_note(handleNote)

# start the led animation, also causes the app to keep listening for key presses
nextStep()

