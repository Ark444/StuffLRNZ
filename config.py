import configparser

if "config" not in globals():
    globals()["config"] = configparser.ConfigParser()
    globals()["config"].read('stufflrnz.conf')
