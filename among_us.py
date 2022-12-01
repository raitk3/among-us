import subparts.ux
import time

VERSION_NUMBER = str(time.strftime("%y%m%d"))
VERSION = "ALPHA"

def main():
    subparts.ux.Program("Among Us Toolkit", VERSION_NUMBER, VERSION)

if __name__ == '__main__':
    main()