#!/usr/bin/env python3
"""
Author: Lunamare

Simple pomodoro timer
"""

"""
TODO:
- break timer (use time_remaining logic to start a new timer on 00:00)
- progress bar
- add/subtract second on j/k & minute on J/K
- add/subtract 5 {second,minute} on {j/k,J/K}
"""

import argparse
import time
import sys
from datetime import datetime, timedelta

from blessed import Terminal


def get_args():
    """argument parser"""
    parser = argparse.ArgumentParser(description='Simple pomodoro timer')

    parser.add_argument('-s',
                        '--show-timer',
                        action='store_true',
                        help='show timer duration and exit')

    return parser.parse_args()


def set_timer():
    """timer logic: returns total timer length; default 25 minutes"""
    return datetime.now() + timedelta(minutes=25)


def tui():
    """tui display logic"""
    term = Terminal()
    timer = set_timer()
    state = 'play'
    time_remaining = ''
    countdown = timer - datetime.now()

    with term.hidden_cursor(), term.fullscreen(), term.cbreak():
        keypress = ''

        while time_remaining != '00:00':
            keypress = term.inkey(timeout=0.01)
            time_remaining = ':'.join(
                str(countdown).split(':')[1:3]).split('.', maxsplit=1)[0]

            if keypress.lower() == 'q':
                sys.exit(0)

            if keypress.lower() == 'p':
                if state == 'play':
                    state = 'pause'
                elif state == 'pause':
                    state = 'play'
                else:
                    sys.exit(1)

            if state == 'play':
                countdown = countdown - timedelta(seconds=1)

            print(term.home +
                  term.light_slate_grey_on_black +
                  term.clear +
                  term.move_y(term.height // 2))

            print(term.center(time_remaining))

            time.sleep(1)


def main():
    """handle arguments and run"""
    args = get_args()
    timer = set_timer()

    if args.show_timer:
        countdown = timer - datetime.now()
        time_remaining = ':'.join(str(countdown)
                                  .split(':')[1:3]).split('.', maxsplit=1)[0]

        print(time_remaining)
        sys.exit(0)

    tui()


if __name__ == '__main__':
    main()
