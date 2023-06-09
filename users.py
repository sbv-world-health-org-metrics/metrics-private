#!/usr/bin/env python3

import sys
import json
from sgqlc.endpoint.http import HTTPEndpoint

try:
    token, repo = sys.argv[1:]
except ValueError:
    raise SystemExit('Usage: <token> <user>')

query = '''
query UserInfo($UserName: String!){
  user(login: $UserName) {
            login
            name 
            email
            location
            company
            twitterUsername
            url
            websiteUrl
            isDeveloperProgramMember
            avatarUrl
  }
}
'''

name = repo.replace('\r', '')
variables = {
    'UserName': name,
}

url = 'https://api.github.com/graphql'
headers = {
    'Authorization': 'bearer ' + token,
}

endpoint = HTTPEndpoint(url, headers)
data = endpoint(query, variables)

json.dump(data, sys.stdout, sort_keys=True, indent=2, default=str)
