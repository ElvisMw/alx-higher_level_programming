#!/usr/bin/python3
"""
Lists 10 commits (from most recent to oldest) of the repository “rails” by the user “rails”
"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner_name, repo_name)
    params = {'per_page': 10}
    response = requests.get(url, params=params)
    
    for commit in response.json():
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author_name))
