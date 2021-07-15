#!/usr/bin/env python3
"""test suite for doropy"""

import os
from subprocess import getstatusoutput, getoutput

PROGRAM = './doro.py'


def test_exists():
    """executable exists"""

    assert os.path.isfile(PROGRAM)


def test_usage():
    """help and usage information displays correctly"""

    for flag in ['-h', '--help']:
        return_value, out = getstatusoutput(f'{PROGRAM} {flag}')
        assert return_value == 0
        assert out.lower().startswith('usage')


def test_timer_duration():
    """test timer duration math"""

    out = getoutput(f'{PROGRAM} --show-timer')

    assert out.strip() == '24:59'
