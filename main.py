from flask import Flask, render_template, url_for, request, flash
import backend

app = Flask(__name__)

@app.route('/<name>', methods=['POST', 'GET'])
def index(name):
    if request.method == 'POST':
        text = request.form['command']
        response = backend.parse_command(text, name)
        if not response == True:
            return response
        backend.create_table(name)
        return render_template('index.html', name=name)
    else:
        backend.create_table(name)
        return render_template('index.html', name=name)

@app.route('/')
def splash():
    return render_template('splash.html')

if __name__ == '__main__':
    app.run(debug=True)
