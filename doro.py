#!/usr/bin/env python3
"""
Author: Lunamare

Simple pomodoro timer
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


def main():
    """handle arguments and run"""
    args = get_args()

    timer = datetime.now() + timedelta(minutes=25)

    if args.show_timer:
        countdown = timer - datetime.now()
        time_remaining = ':'.join(str(countdown)
                                  .split(':')[1:3]).split('.', maxsplit=1)[0]

        print(time_remaining)
        sys.exit(0)

    term = Terminal()

    with term.hidden_cursor(), term.fullscreen():
        while datetime.now() < timer:
            countdown = timer - datetime.now()
            time_remaining = ':'.join(
                str(countdown).split(':')[1:3]).split('.', maxsplit=1)[0]

            print(term.home +
                  term.light_slate_grey_on_black +
                  term.clear +
                  term.move_y(term.height // 2))

            print(term.center(time_remaining))
            time.sleep(1)


if __name__ == '__main__':
    main()
