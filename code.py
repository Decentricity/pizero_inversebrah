
import time
import random
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

def expand_key(grammar, key):
    if key not in grammar:
        return key

    phrase = random.choice(grammar[key])
    return expand_phrase(grammar, phrase)

def find_keys(phrase):
    keys = []
    key = ''
    recording = False
    
    for char in phrase:
        if char == '#' and not recording:
            recording = True
        elif char == '#' and recording:
            keys.append(key)
            key = ''
            recording = False
        elif recording:
            key += char
            
    return keys

def expand_phrase(grammar, phrase):
    
    while "#" in phrase:
        keys = find_keys(phrase)
        
        for key in keys:
            phrase = phrase.replace("#" + key + "#", expand_key(grammar, key), 1)
            
    return phrase
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
# inversebrah summon
grammar = {
    "origin": ["#inversebrah# #getmein# #lilshid# #aw#","#aw# #inversebrah# #getmein# #lilshid#"],
    "inversebrah": ["@inversebrah", "", "inversebrah","inverted brother"],
    "getmein": ["get me in", "put me in","me too", "come here", "come on in", "do your thing", "do your job", "screenshot dis", "yo","come in"],
    "lilshid": ["smolting", "lil shid", "#snot# #salamander#",""],
    "snot" : ["snot","ugly","green", "weird","hybrid","mutated"],
    "salamander" : ["salamander","frok","platypus","cucumber","pickle"],
    "aw" : ["aw","lmwo","lmeow","iwo","jfw" ""]
}

while True:
    # Generate inversebrah notifs
    smoltingsummon = expand_phrase(grammar, "#origin#")
    
    # Write 'n' before the generated text ("new post" keyboard shortcut on Twitter)
    keyboard_layout.write('n')

    # Write the generated text
    keyboard_layout.write(smoltingsummon)

    # Send 'Ctrl-Enter' after the generated text (post!)
    keyboard.press(Keycode.CONTROL)
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    
    # Let's not overwhelm the computer, shall we?
    time.sleep(2come in l)
