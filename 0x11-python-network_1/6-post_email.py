#!/usr/bin/bash
# script that takes in a URL, sends a request to the URL and displays the body of the response.

if __name__ == '__main__':
    from sys import argv
    import requests

    url = argv[1]
    email = argv[2]
    res = request.post(url, {'email': email})
    print(res.text)
