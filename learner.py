#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os
import PIL
from PIL import Image
import argparse

class Learner(object):

    def __init__(self, lang_dir = 'lang', verbose = False, separator = ':'):
        self.lang_dir = lang_dir
        self.verbose = verbose
        self.separator = separator

    def set_lang(self, lang):
        self.lang = {}
        if os.path.isdir(os.path.join(self.lang_dir, lang)):
            langdir = os.path.join(self.lang_dir, lang)
            for f in os.listdir(langdir):
                if f.lower().endswith('.png'):
                    img = Image.open(os.path.join(langdir, f))
                    width, height = img.size
                    img.resize((30, 30), PIL.Image.ANTIALIAS)

                    img.convert("RGBA")
                    pixdata = img.load()
                    
                    symbol = ""
                    # skiping one pixel line every time to preserve size
                    for j in range(0, height, 2):
                        for i in range(0, width):
                            if pixdata[i, j][3] == 255:
                                symbol += "#"
                            else:
                                symbol += " "
                        symbol += "\n"
                    self.lang[symbol] = f.lower().split('.')[0]
        else:
            lang_file = os.path.join(self.lang_dir, lang + '.txt')
            try:
                if self.verbose == True:
                    print('Loading lang file...')
                with open(lang_file) as f:
                    for l in f.readlines():
                        try:
                            (key, val) = l.strip().split(self.separator)
                            self.lang[key] = val
                        except ValueError:
                            pass
                    if self.verbose == True:
                        print('Loaded lang file ["{}"]'.format(lang_file))
            except FileNotFoundError:
                raise

    def learn(self):
        good_replies = 0
        nb_replies = 0

        while True:
            char = random.choice(list(self.lang.keys()))
            try:
                guess = input('{}) {} ? '.format(nb_replies, char))
            except EOFError:
                print('See you next time!\nScore: {}%'.format(
                    int((good_replies / nb_replies) * 100)
                ))
                break
            if guess == self.lang[char]:
                good_replies += 1
            else:
                print("Wrong: {} -> {}".format(char, self.lang[char]))
            nb_replies += 1


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Helps you remember stuff')

    args = parser.parse_args()

    learner = Learner(verbose = True)
    learner.set_lang('kana')
    #learner.set_lang('katakana')
    learner.learn()
