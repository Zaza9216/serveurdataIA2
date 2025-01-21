from flask import Flask, request, render_template, Flask, redirect, url_for

app= Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Vous pouvez ajouter ici la logique de vérification du login et du mot de passe
        if username == 'admin' and password == 'password':  # Exemple de vérification simple
            return redirect(url_for('index'))
        else:
            error = 'Nom d\'utilisateur ou mot de passe incorrect'
            return render_template('login.html', error=error)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
