#!/usr/bin/python3
#script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

if __name__ == '__main__':
    from sys import argv
    from requests import get

    username = argv[1]
    password = argv[2]

    url = 'https://api.github.com/user'
    response = get(url , auth=(username, password))
    json = response.json()
    print(json.get('id'))

