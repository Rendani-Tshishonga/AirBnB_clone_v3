#!/usr/bin/python3
"""Load Libraries"""
from flask import Flask
from models import storage
from api.vi.views import app_views
from os import getenv

"""Initiate a Flask instance"""

app = Flask(__name__)
""" Register a Blueprint for your application"""
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown():
    """Teardown application"""
    storage.close()


if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"), threaded=True)
