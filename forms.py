from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired

class MainForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    uoft_email = StringField('What is your UofT Email address?', [DataRequired()])
    submit = SubmitField('Submit')

    def validate_uoft_email(self, field):
        error_msg = ''
        at_err = False
        uoft_err = False
        if '@' not in field.data:
            error_msg += "Please include an '@' in the email address. "
            at_err = True
        if 'utoronto' not in field.data:
            error_msg += "Please use your uoft email address. "
            uoft_err = True
        if at_err or uoft_err:
            error_msg += f"'{field.data}' is missing "
            if at_err:
                error_msg += "an '@'"
            if at_err and uoft_err:
                error_msg += " and "
            if uoft_err:
                error_msg += "utoronto"
        error_msg += "."
        if at_err or uoft_err:
            raise ValidationError(error_msg)