import os
import secrets
import requests
from hush import app, db
from sqlalchemy import or_, and_
from sqlalchemy.orm import Session
from flask import Flask, session, render_template, url_for, flash, redirect, request, send_from_directory, send_file

# imports removed, check again
# Please review routes

@app.before_request
def make_session_permanent():
	session.permanent = True

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
	return render_template('home.html', title='Home')

@app.route("/chicken")
def chicken():
	return render_template('chicken.html', title='Chicken')


############ MORSE: Atharva #################### Template remaining

@app.route("/start")
def start():
	return render_template('start.html', title='WTH is this')


############# HEXDUMP: Ali ################# Added 

@app.route("/MorseLzAwesum") 
def cat_ctf():
	return render_template('cat.html', title='So cute!')

@app.route("/morselzawesum")
def morseAlt2():
	return redirect('/MorseLzAwesum')

@app.route("/MORSELZAWESUM")
def morseAlt3():
	return redirect('/MorseLzAwesum')

@app.route("/catImage")
def cat_image_sender():
	return send_file(os.path.join('static', 'cat.png'), mimetype='image/png')


############ IMAGE BITS: Yash #################### Added
@app.route("/$tegAn0gr@phY")
def optimus():
	return render_template('optimus.html')


############ REDIR-REDIR: Ali and Harsh ################## Added 

@app.route("/scaryterry") 
def image_ctf():
	return render_template('network.html', title='Explore!')

@app.route("/image2")
def image_redirect2():
	return redirect("/image")

@app.route("/image")
def network_image_sender():
	return send_file(os.path.join('static', 'network.jpg'), mimetype='image/jpeg')

@app.route("/myImage")
def image_redirect1():
	# Next flag is c0mpUt3rN3tworK1ng
	return redirect("/image2?type=jpg&imageNo=2&name=myImage&jhanda=c0mpUt3rN3tworK1ng&size=1080x768")


######### FINALE BEGINS ############### 
@app.route("/c0mpUt3rN3tworK1ng")
def finaleBegins():
	return render_template('finaleBegins.html', title='Finale Begins')


#### PART 1: S/O ### Nidhee # Done
@app.route("/stackoverflow")
def stackoverflow():
	return render_template('stackoverflow.html', title='stackoverflow')

@app.route("/stackAnswer")
def stackAnswer():
	return render_template('stackAnswer.html', title='How to approach a CTF when you\'re clueless')

# Related answers (from /stackAnswer)
@app.route("/related1")
def related1():
	return render_template('related1.html', title = 'Online resources/competitions Related to CTF for beginners<')

@app.route("/related2")
def related2():
	return render_template('related2.html', title = 'Which methods to use to find the flag related to a question')

@app.route("/related3")
def related3():
	return render_template('related3.html', title = 'Any tips for commonly occuring/encountered Logic or Approaches Related to CTF')

@app.route("/related4")
def related4():
	return render_template('related4.html', title = 'What is the relevance of info provided in each stage in a CTF? How do I know what is a waste/not related and what isn\'t')

@app.route("/related5")
def related5():
	return render_template('related5.html', title = 'How to confirm if the pattern that you\'ve found is right')

@app.route("/related6")
def related6():
	return render_template('related6.html', title = 'Help for seemingly futile and unrelated flag searches')

@app.route("/related7")
def related7():

	return render_template('related7.html', title = 'Does  bruteforcing always work even for not related domains')

@app.route("/related8")
def related8():
	return render_template('related8.html', title = 'Dead End')


### PART 2: CODECHEF ### Yash # Done
@app.route("/codechef")
def codechef():
	return render_template('codechef.html', title = 'Codechef')

@app.route("/rankings/codechef")
def rankings_codechef():
	return redirect("/codechef")

@app.route("/codechef_404")
def codechef_404():
	return render_template('codechef_404.html', title = 'Codechef')

@app.route("/rankings/codechef_404")
def rankings_codechef_404():
	return redirect("/codechef_404")


### PART 3: YOUTUBE ### Nidhee # Done
@app.route("/abdul_bohot_bhari")
def abdul_bohot_bhari():
	return redirect('https://www.youtube.com/watch?v=wr0F14QidJU&feature=youtu.be')

@app.route("/fj8g4c")
def nesoacademy():
	return redirect('https://www.youtube.com/watch?v=cZMpPr5yDeY&feature=youtu.be')

@app.route("http://communityofcoders.pythonanywhere.com/fj8g4c")
def absolute1():
	return redirect('https://www.youtube.com/watch?v=cZMpPr5yDeY&feature=youtu.be')


@app.route("/2pu34m")
def abhishekUpmanyu():
	return redirect('https://www.youtube.com/watch?v=f-6DhT_39B0&feature=youtu.be')

@app.route("http://communityofcoders.pythonanywhere.com/2pu34m")
def absolute2():
	return redirect('https://www.youtube.com/watch?v=f-6DhT_39B0&feature=youtu.be')



####### FLAG #######
@app.route("/LAB3")
def lab3():
	return "No, kids. You thought by 'LAB 3', we were referring to a ROUTE?"

@app.route("/lab3")
def altLab3():
	return redirect('/LAB3')