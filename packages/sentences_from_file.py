import keyboard
import time
import sys

def wait_seconds(seconds: float):
    time_start = time.time()
    while (time.time() - time_start < seconds):
        if keyboard.is_pressed('shift'):
            break

def read(filename):
    list_of_strings = []
    with open(filename, encoding="utf-8") as file:
        for line in file.readlines():
            list_of_strings.append(line.strip())
    return list_of_strings

def send(filename):
    print("ACTIVATE!")
    
    sentences = read(filename)
    
    for index, sentence in enumerate(sentences):
        if index != 0:
            wait_seconds(2.5)
        if keyboard.is_pressed('shift'):
            break
        print(sentence)
        keyboard.write(sentence)
        wait_seconds(0.75)
        print("SEND!")
        keyboard.send('enter')


if __name__ == '__main__':
    filename = sys.argv[1]
    print(filename)
    wait_seconds(3)
    send(filename)
