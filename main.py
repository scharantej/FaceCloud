
# Flask
from flask import Flask, render_template, redirect, url_for, request, session
from werkzeug.security import generate_password_hash, check_password_hash

# OpenCV and face manipulation
import cv2
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Secret key for session management
app.secret_key = "mysecretkey"

# Database (in-memory for simplicity)
users = {"alice": {"password": generate_password_hash("password"), "profile_pic": "alice.jpg"}}

# Login page
@app.route('/')
def login():
    return render_template('login.html')

# Login form submission
@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    if username in users and check_password_hash(users[username]['password'], password):
        session['username'] = username
        return redirect(url_for('profile'))
    return render_template('login.html', error="Invalid credentials")

# Profile page
@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('profile.html', username=session['username'], profile_pic=users[session['username']]['profile_pic'])

# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Livestreaming page
@app.route('/livestream')
def livestream():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('livestream.html')

# Start livestream
@app.route('/start_livestream')
def start_livestream():
    # Start video stream (pretend code)
    return redirect(url_for('livestream'))

# Stop livestream
@app.route('/stop_livestream')
def stop_livestream():
    # Stop video stream (pretend code)
    return redirect(url_for('profile'))

# Face detection and manipulation page
@app.route('/face_detection')
def face_detection():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('face_detection.html')

# Apply filter to face
@app.route('/apply_filter', methods=['POST'])
def apply_filter():
    # Receive image, apply filter (pretend code)
    return '{"filtered_image": "filtered_image.jpg"}'  # Return modified image as JSON

# Main driver
if __name__ == '__main__':
    app.run(debug=True)
