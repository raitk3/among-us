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

    sentences = [
        [
            "Alright, the host has set us 6 rules in her Dojo:",
            "So, the host has set us some rules:",
            "Well, the host has set 6 rules here:",
            "Some quick rules for better and more enjoyable gameplay:",
            "Follow those 6 rules or get Banned:"
        ],

        [
            "Rule 1: We don't say start here",
            "Rule 1: Do NOT say start",
            "Rule 1: ''Start'' is forbidden"
        ],

        [
            "Rule 2: Purple is ALWAYS sus",
            "Rule 2: Purple SUS...ALWAYS",
            "Rule 2: Purple 24/7 SUS"
        ],

        [
            "Rule 3: Don't group, team or camp cams",
            "Rule 3: No teaming, No grouping and No camping in cams"
        ],

        [
            "Rule 4: Don't use any hacks",
            "Rule 4: No hacking"
        ],

        [
            "Rule 5: Don't ask where, let the person speak",
            "Rule 5: The one who reports or calls the meeting speaks first"
        ],

        [
            "Rule 6: No sensitive people",
            "Rule 6: Don't be sensitive"
        ]
    ]
    
    sentences_to_write = []
    for sentence_choices in sentences:
        sentences_to_write.append(random.choice(sentence_choices))

    for index, sentence in enumerate(sentences_to_write):
        if index != 0:
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
