import auto_rejoin
import auto_text
import lyrics


def ask_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return ask_input(prompt)

def main():
    print(ask_input("Insert the action you want to do: "))

if __name__ == '__main__':
    while True:
        main()