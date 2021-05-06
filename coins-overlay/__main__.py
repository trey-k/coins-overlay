import sys
import keyboard


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    # arg parsing with argparse

    keyboard.add_hotkey(78, print, args=["coin +1"]) # numpad +
    keyboard.add_hotkey(74, print, args=["coin -1"]) # numpad -
    keyboard.add_hotkey(53, print, args=["reset"]) # numpad /
    keyboard.add_hotkey(55, print, args=["confetti"]) # numpad *

    print("Press ESC to stop.")
    keyboard.wait('esc')


if __name__ == "__main__":
    sys.exit(main())