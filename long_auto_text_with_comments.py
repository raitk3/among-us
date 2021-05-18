# Some syntax to help you understand better
# # -> Comments
# def -> defines a function
#   What is a function?
#   A thing that does some pre-defined things with given stuff 
# while -> do same shit while the condition is True
# for -> do same shit to every thing
# break -> cancel doing what it was doing
# continue -> break and start over
# pass -> do nothing
# print() -> prints the thing into console

#IMPORTS, DO NOT DELETE
import keyboard
import time


#HELPFUL FUNCTIONS
def wait_seconds(seconds: float):
    # This function basically waits a certain amount of time in seconds
    # It will break only if time is up or "shift" is pressed
    
    print(f"Waiting {seconds} seconds")
    time_start = time.time()
    while (time.time() - time_start < seconds):
        if keyboard.is_pressed('shift'):
            break
        continue
    pass


def send(what_to_send: list):
    # This will send all the sentences in the list. 
    
    # For every sentence in the list
    for sentence in what_to_send:
        # Wait 3 seconds (Among Us anti-spam)
        wait_seconds(2.5)
        if keyboard.is_pressed('shift'):
            break
        # Write that text
        print(f"Writing text: {sentence}")
        keyboard.write(sentence) # <- REMOVE THE FIRST HASHTAG IF YOU ARE ACTUALLY GOING TO SEND
        wait_seconds(0.5)
        
        # Press enter to send it
        print("SEND IT")
        keyboard.press_and_release('enter') # <- REMOVE THE FIRST HASHTAG IF YOU ARE ACTUALLY GOING TO SEND
    
    # After sending, let the user know it's done
    print("Done!")


# THE MAIN SHIT THAT RUNS. THE WHOLE PROCESS STARTS HERE
if __name__ == '__main__':
    
    # The sentences:
    sentences = [
    "There are 4 rules in this Dojo:",
    "Rule 1: We don't say start here",
    "Rule 2: Purple is ALWAYS sus",
    "Rule 3: Don't group, team or camp cams",
    "Rule 4: Don't use any hacks"
    ]
    
    # Wait some amount of time to let user open Among Us and select the textbox 
    #(The send-function gives additional 3 seconds)
    wait_seconds(0)
    
    # Send the list of sentences
    # How does it send? Check the send() function
    send(sentences)
