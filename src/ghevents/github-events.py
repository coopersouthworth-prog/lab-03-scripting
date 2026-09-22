#!/opt/miniconda3/bin/python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'
print(GHUSER)

def retrieve_events(url):
	"""
	takes a url and retrieves its events
	"""
	resptxt = requests.get(url).text
	answer = json.loads(resptxt)
	return answer

def print_events(events, n=5):
	"""
	Prints events
	"""
	for x in events[:n]:
    		event = x['type'] + ' :: ' + x['repo']['name']
    		print(event)

def main():
	"""
	does everything
	"""
	print(GHUSER)
	print(url)
	retrieved=retrieve_events(url)
	print_events(retrieved)

if __name__ == "__main__":
    main()
