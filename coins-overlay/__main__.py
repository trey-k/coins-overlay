import sys
import configparser
import keyboard
import tkinter as tk


class Score:
    scores = []

    def __init__(self):
        self.total = tk.IntVar()
        self.scores.append(self)
    
    def increment(self, value=1):
        t = self.total.get()
        self.total.set(t + value)

    def decrement(self, value=1):
        t = self.total.get()
        self.total.set(t - abs(value))


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    # arg parsing with argparse

    def parse_keys(event):
        print(dir(event))
        hotkey = getattr(score, keybinds[event.scan_code])
        hotkey()

    config = configparser.ConfigParser()
    config.read('config.ini')

    keybinds = {}
    for key, value in config.items('BINDS'):
        scan_code = keyboard.key_to_scan_codes(value)
        keybinds[scan_code[0]] = key

    print(keybinds)

    window = tk.Tk()
    score = Score()
    keyboard.on_press(parse_keys)
    label = tk.Label(textvariable=Score.scores[0].total)
    label.pack()

    window.mainloop()

if __name__ == "__main__":
    sys.exit(main())