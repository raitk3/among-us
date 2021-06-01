import keyboard
import time
import random


def wait_seconds(seconds: float):
    time_start = time.time()
    while (time.time() - time_start < seconds):
        if keyboard.is_pressed('shift'):
            break


def send():
    """
    ToDo:
    Make it count rules and increment rule numbers
    """
    print("ACTIVATE!")

    sentences = [
        [
            "Alright, the host has set us {number_of_rules} rules in her Dojo:",
            "So, the host has set us some rules:",
            "Well, the host has set {number_of_rules} rules here:",
            "Some quick rules for better and more enjoyable gameplay:",
            "Follow those {number_of_rules} rules or get Banned:"
        ],

        [
            "We don't say start here",
            "Do NOT say start",
            "''Start'' is forbidden"
        ],

        [
            "Purple is ALWAYS sus (joke)",
            "Purple SUS...ALWAYS (it's a joke)",
            "Purple 24/7 SUS (jokingly but keep that in mind)"
        ],

        [
            "Don't group, team or camp cams",
            "No teaming, No grouping and No camping in cams"
        ],

        [
            "Don't ask where, let the person speak",
            "The one who reports or calls the meeting speaks first"
        ],

        [
            "No sensitive people",
            "Don't be too sensitive"
        ],

        [
            "WooHoo if you understand",
            "WooHoo if you agree to the terms of this lobby"
        ]
    ]

    sentences_to_write = []
    for i, sentence_choices in enumerate(sentences):
        if i == 0 or i == (len(sentences)-1):
            sentences_to_write.append(random.choice(
                sentence_choices).format(number_of_rules=len(sentences)-2))
        else:
            sentence_to_add = f"Rule {i}: "
            sentence_to_add += random.choice(sentence_choices)
            sentences_to_write.append(sentence_to_add)

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
