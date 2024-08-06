#!/usr/bin/python3
"""Load Libraries"""
from flask import Flask, make_response
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

@app.errorhandler(404)
def not_found(error):
    """Handles a 404 error"""
    return make_response(jsonify({'error': 'not found'}), 404)

if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"), threaded=True)
