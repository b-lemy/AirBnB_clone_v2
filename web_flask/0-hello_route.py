#!/usr/bin/python3
""" This script starts the wsgi application and the web page
at any ip address of 0.0.0.0 in port 5000
"""

from flask import Flask

apt = Flask(__name__)


@apt.route('/', strict_slashes=False)
def hello():
    """ This function simply renders the string 'Hello HBNB' """
    return ('Hello HBNB!')


if __name__ == "__main__":
    apt.run(host='0.0.0.0', port=5000)
