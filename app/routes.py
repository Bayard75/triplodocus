from app import app
from flask import render_template, request

@app.route('/')
@app.route('/acceuil')
def acceuil():
    user_agent = request.headers.get('User-Agent')
    if 'Mobi' in user_agent:
        return render_template('acceuil_mobile.html')
    return render_template('acceuil.html')