import sqlite3
import sys
import os

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print('Usage: %s <resource_dict>' % (sys.argv[0]))
        exit()
    conn = sqlite3.connect('stufflrnz.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE kana (id int, name text, data text, data_type text)''')


    x = 0
    for f in os.listdir(sys.argv[1]):
        c.execute("INSERT INTO kana VALUES (%d, '%s', '%s', 'IMG')" % (
                x,
                f.split('_')[0],
                os.path.join(sys.argv[1], f),
            ))
        x += 1

    conn.commit()
    conn.close()
