from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = EmailField('Enter your email', validators=[DataRequired(), Email(message='Please enter correct email')])
    psw = PasswordField('Enter your password', validators=[DataRequired()])
    name = StringField('Enter your name', validators=[DataRequired()])
    submit = SubmitField('Ok')


class CommentForm(FlaskForm):
    text = CKEditorField("Comment here", validators=[DataRequired()])
    submit = SubmitField("Submit comment")
