import os
import secrets
import requests
import hashlib
from hush import app, db
from hush.forms import flags
from sqlalchemy import or_, and_
from sqlalchemy.orm import Session
from flask import Flask, session, render_template, url_for, flash, redirect, request, send_from_directory
from flask_bootstrap import Bootstrap
import datetime
from datetime import timedelta
from functools import wraps

@app.before_request
def make_session_permanent():
	session.permanent = True

@app.route("/")
@app.route("/home", methods = ['GET', 'POST'])
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