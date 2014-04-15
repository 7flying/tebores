from sys import argv
from twitter import Twitter, OAuth

OAUTH_TOKEN = ''
OAUTH_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

def search_tweets(q, count=100):
	return t.search.tweets(q=q, result_type='recent', count=count)


if __name__ == '__main__':
	result = search_tweets(argv[1:], 1)
	print result