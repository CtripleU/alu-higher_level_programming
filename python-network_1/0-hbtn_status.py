#!/usr/bin/python3
'''This script fetches https://intranet.hbtn.io/status
using the urlib package
'''

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
