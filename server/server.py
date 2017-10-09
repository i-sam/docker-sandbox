#!/usr/bin/env python

import sys

from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/stdout', methods=['GET', 'POST'])
def echo_stdout():
    if request.method == 'POST':
        print request.form.get('string')
    else:
        sys.stdout.write(request.args.get('string') + '\n')
    sys.stdout.flush()
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

