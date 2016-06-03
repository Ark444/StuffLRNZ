#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

import config
import core

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Helps you remember stuff')

    parser.add_argument('--verbose', '-v', action='store_true', default=False,
            help='Be more verbose')
    parser.add_argument('--list-dicts', '-l', action='store_true', default=False,
            help='List imported dictionaries and exit')
    parser.add_argument('--list-gui', '-L', action='store_true', default=False,
            help='List available GUI and exit')
    parser.add_argument('--gui', '-g', default="termGUI",
            help='Choose a GUI to use with StuffLRNZ')

    args = parser.parse_args()
    core = core.Core(args)
    core.run()

