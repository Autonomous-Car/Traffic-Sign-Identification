# -*- coding: utf-8 -*-
"""
This script runs the Management application using a development server.
"""

from os import environ
from TrafficSignIdentification import app

if __name__ == '__main__':
    DEBUG = environ.get("SVR_DEBUG", False)
    HOST = environ.get('SVR_HOST', '0.0.0.0')
    PORT = 8723
    DEBUG = True
    app.run(HOST, PORT, debug=DEBUG)