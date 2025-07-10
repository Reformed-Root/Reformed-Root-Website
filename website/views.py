from flask import Blueprint, render_template, request, redirect, url_for, session, send_from_directory, current_app
from .auth import authenticate_user
import os



views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html', user=session.get('user'))

@views.route('/challenge', methods=['GET', 'POST'])
def challenge():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user = authenticate_user(name, password)
        if user:
            session['user'] = user[0]
            return redirect(url_for('views.b4flag'))
        else:
            return redirect(url_for('views.access_denied'))
            #return "Invalid credentials", 401
    return render_template('challenge.html')


@views.route('/videos/<filename>')
def serve_video(filename):
    video_path = os.path.join(os.getcwd(), 'website', 'static')
    return send_from_directory(video_path, filename)


@views.route('/b4flag')
def b4flag():
    if 'user' in session:
        return render_template('b4flag.html', user=session.get('user'))
    return redirect(url_for('views.challenge'))


@views.route('/access-denied')
def access_denied():
    return render_template('access-denied.html')  # This is the video template


@views.route('/secret_flag')
def secret_flag():
    if 'user' in session:
        return render_template('secret_flag.html', user=session.get('user'))
    return redirect(url_for('views.challenge'))



@views.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"<h1>Welcome, {session['user']}!</h1><a href='/logout'>Logout</a>"
    return redirect(url_for('views.challenge'))

@views.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('views.home'))

@views.route('/about')
def about():
    return render_template('about.html', user=session.get('user'))

@views.route('/services')
def services():
    return render_template('services.html', user=session.get('user'))

@views.route('/contact')
def contact():
    return render_template('contact.html', user=session.get('user'))

@views.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(current_app.root_path, 'static/favicons'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
