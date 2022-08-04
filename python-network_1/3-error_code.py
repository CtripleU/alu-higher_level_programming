#!/usr/bin/python3
'''This script takes in a URL,
sends a request to the URL,
and displays the body of the response
'''

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
