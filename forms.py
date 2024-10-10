from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, Length, EqualTo
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    """
    Form for creating a new blog post. It includes fields for the title, subtitle,
    image URL, and body content. The CKEditorField is used for the body to allow 
    rich-text input. 
    """
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# WTForm for user registration
class RegisterForm(FlaskForm):
    """
    Form for registering new users. It includes fields for email, password,
    password confirmation (using EqualTo to ensure they match), and the user's name.
    """
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("SIGN ME UP!")


# WTForm for user login
class LoginForm(FlaskForm):
    """
    Form for logging in existing users. It includes fields for email and password.
    """
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("LET ME IN!")


# WTForm for submitting comments on blog posts
class CommentForm(FlaskForm):
    """
    Form for users to leave comments on blog posts. The comment is submitted using 
    a CKEditorField to allow rich-text formatting.
    """
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("SUBMIT COMMENT")


