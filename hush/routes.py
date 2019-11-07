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


@app.route("/flagName")  # TODO Add flag name
def image_ctf():
    return render_template('network.html', title='Explore!')

############ REDIR-REDIR: Ali ################## Added 
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


######### FINALE BEGINS ############### ToDo

#### PART 1: S/O ### Nidhee
@app.route("/stackoverflow")
def stackoverflow():
    return render_template('stackoverflow.html', title='stackoverflow')

@app.route("/stackAnswer")
def stackAnswer():
    return render_template('stackAnswer.html', title='How to approach a CTF when you\'re clueless')

# Related answers (from /stackAnswer)
@app.route("/related1")
def related1():
	return render_template('related1.html', title = 'Online CTF resources/competitions for beginners')

@app.route("/related2")
def related2():
	return render_template('related2.html', title = 'Which methods to use to find the flag in a question')

@app.route("/related3")
def related3():
	return render_template('related3.html', title = 'Any tips of commonly occuring/encountered logics or appraoches in CTF')

@app.route("/related4")
def related4():
	return render_template('related4.html', title = 'What is the relevance of info provided in each stage in a CTF? How do I know what is a waste and what isn\'t')

@app.route("/related5")
def related5():
	return render_template('related5.html', title = 'How to confirm if the pattern that you\'ve found is right')

@app.route("/related6")
def related6():
	return render_template('related6.html', title = 'Help for seemingly futile flag searches')

@app.route("/related7")
def related7():

	return render_template('related7.html', title = 'Does bruteforcing always work')

@app.route("/related8")
def related8():
	return render_template('related8.html', title = 'Dead End')


### PART 2: CODECHEF ### Yash
@app.route("/codechef")
def codechef():
	return render_template('flag1.html', title = 'Codechef')


### PART 3: YOUTUBE ### Nidhee 