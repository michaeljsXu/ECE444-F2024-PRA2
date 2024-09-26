from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email

class MainForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    uoft_email = EmailField('What is your UofT Email address?', [DataRequired(), Email()])
    submit = SubmitField('Submit')