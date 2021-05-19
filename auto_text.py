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
        [   # 1st sentences
            "This is sentence no 1",
            "This could be the first sentence as well",
            "This is the first as well"
        ],

        [   # 2nd ones
            "This is sentence no 2.",
            "This could be the second one as well."
        ],

        [   # 3rd one
            "This is the 3rd sentence without any alternations"
        ] # etcetc
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
