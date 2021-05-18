import keyboard
import time
import random

def wait_seconds(seconds: float):
    time_start = time.time()
    while (time.time() - time_start < seconds):
        if keyboard.is_pressed('shift'):
            break
            
def send():
    print("ACTIVATE!")
    sentences = []
    
    sentences.append(random.choice(
    ["Alright, the host has set us 5 rules in her Dojo:", 
    "So, the host has set us some rules:", 
    "Well, the host has set 5 rules here:",
    "Some quick rules for better and more enjoyable gameplay:",
    "Follow those 5 rules or get Banned:"]))
    
    sentences.append(random.choice([
    "Rule 1: We don't say start here",
    "Rule 1: Do NOT say start",
    "Rule 1: ''Start'' is forbidden"
    ]))
    
    sentences.append(random.choice([
    "Rule 2: Purple is ALWAYS sus",
    "Rule 2: Purple SUS...ALWAYS",
    "Rule 2: Purple 24/7 SUS"
    ]))
    
    sentences.append(random.choice([
    "Rule 3: Don't group, team or camp cams",
    "Rule 3: No teaming, No grouping and No camping in cams"
    ]))
    
    sentences.append(random.choice([
    "Rule 4: Don't use any hacks",
    "Rule 4: No hacking"
    ]))
    
    sentences.append(random.choice([
    "Rule 5: Don't ask where, let the person speak",
    "Rule 5: The one who reports or calls the meeting speaks first"
    ]))
    
    for i, sentence in enumerate(sentences):
        if i != 0:
            wait_seconds(3)
        if keyboard.is_pressed('shift'):
            break
        print(sentence)
        keyboard.write(sentence)
        wait_seconds(0.1)
        print("SEND!")
        keyboard.send('enter')

if __name__ == '__main__':
    keyboard.add_hotkey('ctrl+space', send, trigger_on_release=True)
    keyboard.wait()
