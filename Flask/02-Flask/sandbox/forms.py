from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from sandbox.models import User
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class RegisterForm(FlaskForm):

    def validate_username(self,username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('username is already in use')

    def validate_email_address(self,email_address_to_check):
        email = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email:
            raise ValidationError('email is already in use')

    username = StringField(label="Username:", validators=[Length(min=3,max=30),DataRequired()])
    email_address = StringField(label="Email:", validators=[Length(min=3,max=30),Email(),DataRequired()])
    password_one = PasswordField(label="enter password:", validators=[Length(min=6,max=60),DataRequired()])
    password_two = PasswordField(label="confirm password:", validators=[EqualTo("password_one"),DataRequired()])
    submit = SubmitField(label="Create Account")

class LoginForm(FlaskForm):

    username = StringField("Username:",validators=[DataRequired()])
    password = PasswordField("Password:",validators=[DataRequired()])
    submit = SubmitField(label="Sign in")
