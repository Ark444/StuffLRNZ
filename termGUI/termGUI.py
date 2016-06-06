import PIL
from PIL import Image

class termGUI(object):
    GUI_NAME = 'termGUI'

    def __init__(self):
        pass

    def display_img(self, img_path):
        img = Image.open(img_path)
        width, height = img.size
        img.resize((30, 30), PIL.Image.ANTIALIAS)
        img.convert("RGBA")
        pixdata = img.load()

        symbol = ''
        for j in range(0, height, 2):
            for i in range(0, width):
                if pixdata[i, j][3] == 255:
                    symbol += '#'
                else:
                    symbol += ' '
            symbol += '\n'
        print(symbol)

    def display_data(self, data, data_type):
        if data_type == 'IMG':
            try:
                self.display_img(data)
            except FileNotFoundError:
                print(data)
        else:
            print(data)

    def get_input(self):
        return input('> ')

    def menu_select(self, items):
        idx = 0
        for item in items:
            print('%d) %s' % (idx, item))
            idx += 1
        while True:
            selection = []
            try:
                for idx in input('> ').split(','):
                    selection.append(items[int(idx)])
            except IndexError:
                print('[-] Error: invalid selection.')
            else:
                break
        return selection
