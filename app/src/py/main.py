#!/usr/bin/env python

# Haoji liu
import json
# Third party module
import requests
from flask import Flask, render_template, request, redirect, url_for, abort, session
# from flask.ext.pymongo import PyMongo

# Instantiate a Flask app
app = Flask(__name__)

# Instantiate a MongoDB database
# mongo = PyMongo(app)
# Instantiate another db obj
# mongo2 = PyMongo(app)

# Homepage
@app.route('/')
def index():
  return render_template('index.html')

# Test page for google map javascript api
#@app.route('/map')
#def google_map():
#  return render_template('google_map.html')

@app.route('/noise/v1', methods=['GET','POST'])
def noise_v1():
  if request.method == 'POST':
    # TODO: Write the record to db
    # TODO: recaptcha auth
    #
    data = dict(request.form)
    data['User IP'] = request.environ['REMOTE_ADDR']
    data['User browser'] = request.headers['User-Agent']

    g_recaptcha_response = data['g-recaptcha-response']
    g_recaptcha_post_data = {
      'secret': '6LeWSQwUAAAAAM_1v-8rlFI5JxMaZrU3n9oJm0n-',
      'response': g_recaptcha_response}
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=g_recaptcha_post_data)
    data['is_g_recaptcha_verified'] = r.json().get('success', False)
    return render_template('thank_you.html', data=data)
  else:
    return render_template('noise_review_with_map.html')

@app.route('/data/v1', methods=['GET','POST'])
def data_v1():
  if request.method == 'POST':
    post_data = dict(request.form)
    return render_template('data_viewer.html')
  else:
    return render_template('data_viewer.html')


# GET with variable
@app.route('/user/<username>')
def show_user_profile(username):
  # show the user profile for that user
  return 'User %s' % username

# GET with variable
@app.route('/post/<int:post_id>')
def show_post(post_id):
  # show the post with the given id, the id is an integer
  return 'Post %d' % post_id

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=80)
