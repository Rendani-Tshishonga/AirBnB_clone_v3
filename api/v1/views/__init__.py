#!/usr/bin/python3
"""Create a Blueprint"""
from flask import Blueprint

app_views = Blueprint('/api/v1', __name__, url_prefix = '/api/v1')
