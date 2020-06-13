from app import app
from flask import render_template, request

@app.route('/')
@app.route('/acceuil')
def acceuil():
    return render_template('acceuil.html')