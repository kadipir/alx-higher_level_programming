#!/usr/bin/python3
"""Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
 """
if __name__ == "__main__":
     from sys import argv
     from requests import get

     url = '"https://api.github.com/repos/{}/{}/commits".format(owner, repo)'
     response = get(url)
     json = response.json()
     i = 0

     repo = argv[1]
     owner = argv[2]

     for element in json:
         if i > 9:
             break
         sha = element.get('sha')
         author = element.get('commit').get('author').get('name')
         print('{}: {}'.format(sha, author))
         i += 1
     
