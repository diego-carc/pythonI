import os
import sys
import argparse

my_parser = argparse.ArgumentParser(description='List the content of a folder')

my_parser.add_argument('Path', metavar='path', type=str, help='the path to list')

args = my_parser.parse_args()

input_path = args.Path
print()
if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))