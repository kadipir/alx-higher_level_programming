#!/usr/bin/python3
#script that fetches https://alx-intranet.hbtn.io/status

if __name__ == "__main__":
    import requests

    r = requests.get("https://alx-intranet.hbtn.io/status")
    t = r.text
    print("Body response:\n \t - type: {}\n \t - content: {}".format(type(r),r))
