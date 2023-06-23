from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    form = ImcForm()
    return render_template('index.html', form=form)

@app.route('/<usrname>')
def about_page(usrname):
    return f'ERRO. A página {usrname} não existe !!!!'