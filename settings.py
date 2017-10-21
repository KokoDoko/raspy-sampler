from pygame import mixer

files1 = [
    "cylons/byc.wav",
    "cylons/extermin.wav",
    "cylons/fire_wea.wav",
    "cylons/lv_no_sr.wav",
    "cylons/stbyatt.wav",
    "cylons/attention.wav",
    "cylons/info.wav",
    "cylons/deception.wav"
]
files2 = [
    "drums/thud.wav",
    "drums/smash.wav",
    "drums/clap.wav",
    "drums/hat.wav",
    "drums/rim.wav",
    "drums/ting.wav",
    "drums/crash.wav",
    "drums/hit.wav"
]

def createSoundObjects(fileNames):
    temp = []
    for file in fileNames:
        temp.append(mixer.Sound("/home/pi/yourprojectfolder/" + file))
    return temp
