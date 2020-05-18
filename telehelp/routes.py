from flask import render_template, redirect, url_for, flash, request, abort, jsonify
from telehelp.models import User
from telehelp import app



#TEST
@app.route("/")
def index():
    return '<h1>Hello world</h1>'
