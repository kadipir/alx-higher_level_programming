#!/usr/bin/python3
#send a POST Request to the passed url with email as a parameter and displays the body of the response (decoded in utf-8)

if __name__ == "__main_-":
    import sys
    import urllib.parse
    import urllib.request

    argv = sys.argv
    url = argv[1]
    email = argv[2]
    DATA = urllib.parse.urlencode({"email" : email})
    DATA = DATA.encode("ASCII")

    with urllib.request.urlopen(url, DATA) as response:
        print(response.read().decode("utf-8"))
