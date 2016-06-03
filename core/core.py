import sqlite3
import config
import os

class Core(object):

    def __init__(self, args):
        self.verbose = args.verbose
        self.list_dicts = args.list_dicts
        self.list_guis = args.list_gui

        self.dict = args.select_dict

        self.setGUI(args.gui)
        if self.verbose == True:
            print('Loaded GUI: %s' % (self.gui.GUI_NAME,))

        self.db_conn = sqlite3.connect(args.db)
        self.db_cursor = self.db_conn.cursor()

    def run(self):
        self.running = True

        if self.list_dicts == True:
            self.list_dictionaries()
            return
        elif self.list_guis == True:
            self.list_gui()
            return

        score = 0
        while self.running == True:
            (_, name, data, data_type) = next(self.db_cursor.execute(
                'SELECT * FROM %s ORDER BY RANDOM() LIMIT 1' % (self.dict)))
            self.gui.display_data(data, data_type)
            try:
                user_input = self.gui.get_input()
            except EOFError:
                self.running = False
                print()
                return
            if user_input == 'exit':
                self.running = False
            elif user_input == name:
                score += 1
            else:
                self.gui.display_data('The answer was: %s' %(name), 'TEXT')

    def list_dictionaries(self):
        print('Available dictionaries are:')
        for dic in self.db_cursor.execute('SELECT name FROM sqlite_master WHERE type="table"'):
            print('  * %s' % (dic))

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
