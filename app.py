from flask import Flask, render_template
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
    name = None
    email = None
    form = MainForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.uoft_email.data
        form.name.data = ''
        form.uoft_email.data = ''
    return render_template('index.html', name=name, current_time=datetime.utcnow(), form=form)
