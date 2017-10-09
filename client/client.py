""" Client app """

import os
import requests
import time

FILE_NAME = os.environ.get('FILE_NAME') or 'file.txt'
REMOTE_ADDR = os.environ.get('REMOTE_ADDR')
API_KEY = 'stdout'

while True:
    with open(FILE_NAME, 'r') as f:
	print(REMOTE_ADDR)
        st = f.read().strip('\n')
    response = requests.get('{}/{}'.format(REMOTE_ADDR,API_KEY),
        params=[('string', "%s" % st),])
    time.sleep(60)

