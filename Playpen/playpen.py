import configparser
from os.path import exists
import os
import argparse
import python_template
import java_template
import cpp_template

USER_NAME = os.getlogin()

CONFIG_FILE = '/home/{}/.playpen.conf'.format(USER_NAME)
config_file_contents = """
[PLAYPEN]
location = {_location}
"""

def generate_files(gen_file, content):
    f = open(gen_file, 'w')
    f.write(content)
    f.close()

def read_config():
    config_parser = configparser.ConfigParser()
    config_parser.read(CONFIG_FILE)
    return config_parser['PLAYPEN']['location']

def main(arg):
    build_file = ''
    file_content = ''
    playpen_file = 'Main.'+arg

    if arg == 'py':
        build_file = python_template.build_template
        file_content = python_template.file_content
    elif arg == 'java':
        build_file = java_template.build_template
        file_content = java_template.file_content
    else:
        build_file = cpp_template.build_template
        file_content = cpp_template.file_content
    file_path = read_config() + '/playpen/'
    os.mkdir(file_path)
    generate_files(file_path + 'WORKSPACE', '')
    generate_files(file_path + 'BUILD', build_file)
    generate_files(file_path + playpen_file, file_content)


## arguments are cc, java, py
if __name__ == '__main__':
    if not exists(CONFIG_FILE):
        location = input('Where would you like to deploy playpen? ')
        generate_files(CONFIG_FILE, config_file_contents.format(_location=location))
    else:
        parser = argparse.ArgumentParser(description='TODO: add description')
        parser.add_argument('--language', type=str, required=True)
        args = parser.parse_args()
    main(args.language)
    