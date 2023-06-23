from flask_wtf import FlaskForm
from  wtforms import StringField

class ImcForm(FlaskForm):
    peso = StringField(label='peso')
    altura = StringField(label= 'altura')