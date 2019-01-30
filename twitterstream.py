import requests
from requests_oauthlib import OAuth1
import jsonlines

api_key = "XesdYKaGbBQ3HGMcC6oVGaCEk"
api_secret = "c5jA2VmaWpwPDXfbUhItkcjFRGWev5raK0YQxIz9ZHCQZyI9Jd"
access_token_key = "263706365-o6tFP32yDs7SYVAchkCVJRN1zJTb2p9ujVpIkHHj"
access_token_secret = "wzFOgh8zHBYrh1mXyLNoR5bCLGlVfDdHH4souIAuynpnA"

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(api_key, api_secret, access_token_key, access_token_secret)

r = requests.get(url, auth=auth)
print(r.status_code)

url = 'https://stream.twitter.com/1.1/statuses/sample.json'
r = requests.get(url, auth=auth, stream=True)
if r.encoding is None:
    r.encoding = 'utf-8'

with jsonlines.open('output.json', mode='w') as writer:    
    try:
        for line in r.iter_lines(decode_unicode=True):
            if line:
                writer.write(line)
    except KeyboardInterrupt:
        pass
