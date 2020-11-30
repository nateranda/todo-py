from flask import Flask, render_template, url_for, request, flash, redirect
import backend
from datetime import datetime, date

app = Flask(__name__)

@app.route('/<name>', methods=['POST', 'GET'])
def index(name):
    # process post request
    if request.method == 'POST':
        if "command" in request.form:
            text = request.form['command']
            response = backend.parse_command(text, name)
            if not response == True:
                return response
        elif "remove" in request.form:
            text = "remove " + request.form['remove']
            response = backend.parse_command(text, name)
            if not response == True:
                return response
        elif "do" in request.form:
            text = "do " + request.form['do']
            response = backend.parse_command(text, name)
            if not response == True:
                return response
    # update tasks & return template
    backend.create_table(name)
    response = backend.update_tasks(name)
    if not response == True:
        return response
    layout = backend.get_layout(name)
    return render_template('index.html', name=name, layout=layout, today=date.today())

@app.route('/')
def splash():
    return render_template('splash.html')

@app.template_filter()
def weekday(value):
    week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    obj = datetime.strptime(value, '%Y-%m-%d').date()
    return week[obj.weekday()]

if __name__ == '__main__':
    app.run(debug=True)
