import sys
import keyboard
import tkinter as tk


class Score:
    scores = []

    def __init__(self):
        self.total = tk.IntVar()
        self.scores.append(self)
    
    def increment(self, value=1):
        self.total.set(self.total.get() + value)

    def decrement(self, value=1):
        self.total.set(self.total.get() - abs(value))


def parse_keys(event):
    Score.scores[0].decrement()
    print(Score.scores[0].total)
    # normalize_name()

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    # arg parsing with argparse
    
    keyboard.on_press(parse_keys)

    window = tk.Tk()
    score = Score()
    label = tk.Label(textvariable=Score.scores[0].total)
    label.pack()

    window.mainloop()

if __name__ == "__main__":
    sys.exit(main())