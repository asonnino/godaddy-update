"""
Simple script to update GoDaddy DNS records.
Add this script to the crontab to run it regularly.
"""
from requests import get
from godaddypy import Client, Account

# ---  start configs. ---

api_key = 'GODADDY API KEY'
api_secret = 'GODADDY API SECRET'

domains = ['domain.com']

# ---  end configs. ---

ip = get('https://api.ipify.org').text

account = Account(api_key=api_key, api_secret=api_secret)
client = Client(account)
ret = client.update_ip(ip, domains=domains)
assert ret
