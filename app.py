from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from dotenv import load_dotenv
from forms import MainForm
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY']= os.getenv("SECRET_KEY")
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MainForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        if (old_name is not None and old_name != form.name.data):
            flash('Looks like you have changed your name!')
        if (old_email is not None and old_email != form.uoft_email.data):
            flash('Looks like you have changed your email!')
        session['name'] = form.name.data
        session['email'] = form.uoft_email.data
        return redirect(url_for('index'))
    return render_template('index.html', name=session.get('name'), form=form)
