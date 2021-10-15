from main import app
from flask import render_template, url_for



@app.route('/')
@app.route('/front_page', methods=['GET'])
def front_page():
    title= 'Social Melipona beecheii'
    return render_template('front_page.html', title = title)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    title= 'Dashboard'
    return render_template('dashboard.html', title = title)

@app.route('/login')
def login():
    title= 'Login'
    return render_template('login.html', title = title)

@app.route('/locacion')
def locacion():
    title= 'locacion'
    return render_template('locacion.html', title = title)

@app.route('/comentario')
def comentario():
    title= 'Comentario'
    return render_template('comentario.html', title = title)

@app.route('/ayuda')
def ayuda():
    title= 'Ayuda'
    return render_template('ayuda.html', title = title)

@app.route('/profile')
def profile():
    title= 'Perfil de Usuario'
    return render_template('profile.html', title = title)

@app.route('/publicacion')
def publicacion():
    title= 'Publicación'
    return render_template('publicacion.html', title = title)
