import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def page():
    if request.method == 'POST':
        address = request.form.get('address')
        reply = subprocess.run(
            ["python", "script.py", address], stdout=subprocess.PIPE)
        parsedOutput = reply.stdout.decode()
        if request.form.get('second') == 'on':
            parsedOutput += subprocess.run(
                ["python", "script2.py", address], stdout=subprocess.PIPE).stdout.decode()
        if request.form.get('third') == 'on':
            parsedOutput += subprocess.run(
                ["python", "script3.py", address], stdout=subprocess.PIPE).stdout.decode()

        return render_template('page.html', message=parsedOutput)
    else:
        address = request.form.get('address')
        return render_template('page.html', message=address)


@app.route('/idk', methods=['post', 'get'])
def main():
    message = ''
    username = ''
    password = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

    if username == 'root' and password == 'pass':
        reply = subprocess.run(["python", "script.py"], stdout=subprocess.PIPE)
        print(reply.stdout)
        return render_template('login.html', message=reply.stdout)
    else:
        message = "Enter username or password"
        return render_template('login.html', message=message)
