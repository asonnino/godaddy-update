# godaddy-update
Simple script to update Godaddy DNS.
This script needs to be configured with a [GoDaddy's API key](https://developer.godaddy.com/getstarted).

# Install
Install the following dependencies:
```
pip3 install godaddypy
```

# Run the script as a cronjob.
Add the following line to your crontab:
```
*/5 * * * * /usr/bin/python3 godaddy-update.py
```
