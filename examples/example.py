import json
import os
import argparse

try:
    from LibraryName import(Client, __version__ as client_version)
except ImportError:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from LibraryName import(
        Client, __version__ as client_version)


if __name__ == '__main__':

    print('Client version: {0!s}'.format(client_version))

    api = Client()

    #  Example command:
    #  python examples/example.py
    result = api.get_something()
    
    print(result)

    print('All ok')


