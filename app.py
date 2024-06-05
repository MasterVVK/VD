from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Хранилище сообщений
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send():
    message = request.form['message']
    if message:
        messages.append(message)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
