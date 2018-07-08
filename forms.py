from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class blogForm(Form):
  title = StringField('Title', validators=[DataRequired("please enter title")])
  blog = StringField('blog', validators=[DataRequired("please enter blog")])
  submit = SubmitField('submit')

class LoginForm(Form):
  loginid = StringField('Email', validators=[DataRequired("enter it")])
  password = PasswordField('Password', validators=[DataRequired("enter")])
  submit = SubmitField('LOGIN')
