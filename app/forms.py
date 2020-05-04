from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, DataRequired
from wtforms.fields.html5 import EmailField

images = ['png', 'jpg', 'jpeg', 'gif','jpe']


class UploadForm(FlaskForm):
    
    photo = FileField('Profile Picture', validators=[FileRequired(),FileAllowed(images, 'Images only!')])
    
    description = TextAreaField('Description', [
        DataRequired()
        ])
