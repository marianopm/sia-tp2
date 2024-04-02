import configparser
from collections import defaultdict

def main():
    print("TP2")
    config_params = read_config('config_file.config')

def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    params = defaultdict(dict)
    for section in config.sections():
        for key, value in config.items(section):
            params[section][key] = value
    return params

if __name__ == "__main__":
    main()
