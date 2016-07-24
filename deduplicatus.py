"""
DeDuplicatus: A Deduplication-Enabled Multi-Cloud App

Usage:
  deduplicatus.py sync
  deduplicatus.py config

Options:
  -h --help            show this help message and exit
  --version            show version and exit
"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1.0')

    if arguments['sync']:
        pass
    elif arguments['config']:
        pass
    else:
        print arguments
