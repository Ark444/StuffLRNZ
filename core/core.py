import config 
import os

class Core(object):

    def __init__(self, args):
        self.verbose = args.verbose
        self.list_dicts = args.list_dicts
        self.list_guis = args.list_gui
        
        self.setGUI(args.gui)
        if self.verbose == True:
            print('Loaded GUI: %s' % (self.gui.GUI_NAME,))

    def run(self):

        if self.list_dicts == True:
            self.list_dictionaries()
            return
        elif self.list_guis == True:
            self.list_gui()
            return

    def list_dictionaries(self):
        print('Not implemented yet.')

    def list_gui(self):
        print('Available GUI are:')
        gui_path = config.config.get('Global', 'gui_path')
        for f in os.listdir(gui_path):
            if os.path.isdir(os.path.join(gui_path, f)) and f.endswith('GUI'):
                try:
                    with open(os.path.join(gui_path, f, 'description.txt'), 'r') as d:
                        description = d.read().strip()
                except FileNotFoundError:
                    description = '<No description available>'
                    if self.verbose == True:
                        description += ' (please add description.txt file in %s)' % (
                                os.path.join(gui_path, f))
                print('  * %s:\t%s' % (f, description))

    def setGUI(self, gui_name):
        self.gui = getattr(__import__(gui_name), gui_name)()
