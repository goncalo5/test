from flask import Flask, flash, render_template, request, make_response, session, redirect, url_for
import logging
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
log = app.logger.info

question_n = 0

questions = [
    {
        "question": "quantas pernas tem um frango?",
        "options": ["1", "2", "3", "5"],
        "solution": "2"
    },
    {
        "question": "quantas pernas tem um porco?",
        "options": ["1", "2", "4", "5"],
        "solution": "4"
    },
    {
        "question": "quantas luas tem a terra?",
        "options": ["1", "2", "4", "5"],
        "solution": "1"
    }
]


@app.route('/game', methods = ['GET', 'POST'])
def game():
    log("\n\n\ngame()")
    log("request.form: %s" % request.form)
    question_n = globals()["question_n"]
    log("question_n: %s" % question_n)
    if request.method == 'POST':
        if list(request.form)[0] == questions[question_n]["solution"]:
            log("right")
            globals()["question_n"] += 1
            question_n = globals()["question_n"]
            if question_n >= len(questions):
                globals()["question_n"] = 0
                question_n = globals()["question_n"]
    log("question_n: %s" % question_n)
    return render_template('game.html', question_n=question_n, question=questions[question_n])


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            log("else")
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error = error)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug = True)