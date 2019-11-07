import os
import secrets
import requests
import hashlib
from hush import app, db
from hush.forms import flags
from sqlalchemy import or_, and_
from sqlalchemy.orm import Session
from flask import Flask, session, render_template, url_for, flash, redirect, request, send_from_directory, send_file
from flask_bootstrap import Bootstrap
import datetime
from datetime import timedelta
from functools import wraps


@app.before_request
def make_session_permanent():
    session.permanent = True


@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html', title='Home')


@app.route("/flag1")
def flag1():
    return render_template('flag1.html', title='Flag 1')


@app.route("/chicken")
def chicken():
    return render_template('chicken.html', title='Chicken')


@app.route("/stackAnswer")
def stackAnswer():
    return render_template('stackAnswer.html', title='How to approach a CTF when you\'re clueless')


@app.route("/stackoverflow")
def stackoverflow():
    return render_template('stackoverflow.html', title='stackoverflow')


@app.route("/flagName")  # TODO Add flag name
def image_ctf():
    return render_template('network.html', title='Explore!')


@app.route("/myImage")
def image_redirect1():
    # Next flag is c0mpUt3rN3tworK1ng
    return redirect("/image2?type=jpg&imageNo=2&name=myImage&flag=c0mpUt3rN3tworK1ng&size=1080x768")


@app.route("/image2")
def image_redirect2():
    return redirect("/image")


@app.route("/image")
def network_image_sender():
    return send_file(os.path.join('static', 'network.jpg'), mimetype='image/jpeg')


@app.route("/flagName2")  # TODO Add another name
def cat_ctf():
    return render_template('cat.html', title='So cute!')


@app.route("/catImage")
def cat_image_sender():
    return send_file(os.path.join('static', 'cat.png'), mimetype='image/png')
