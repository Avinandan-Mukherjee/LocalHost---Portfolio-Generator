from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, EmailField, FileField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length



class InputArea(FlaskForm):
    fullname = StringField('Full Name', validators=[DataRequired() ,  Length(min=3, max=30)])
    image = FileField('Upload your Image', validators=[
        DataRequired(),
        FileAllowed(['jpg', 'png', 'jpeg', '.webp'], 'Only Images r accepted')
    ])
    email = EmailField('Email', validators=[DataRequired()])
    education = StringField("Your Education", validators=[DataRequired()])
    company = StringField('Your Institution/ company', validators=[DataRequired()])
    skills = StringField('Your Skills' , validators=[DataRequired()])
    theme = RadioField('Preffered Theme', choices=[('dark','Dark'),('light','Light')])
    color = StringField('Preffered Colors')


    #socials
    github = StringField('Github Link')
    linkedin = StringField('Linkedin Profile Link')
    instagram = StringField('Instagram Profile Link')
    youtube = StringField('Youtube Channel Link')



    prompt = StringField('Anything Else you specifically want to add....')


    submit = SubmitField('Gererate Portfolio')