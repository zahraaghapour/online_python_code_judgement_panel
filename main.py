from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import threading
import unittest
import HtmlTest
from queue import Queue

BASE_DIR = os.path.dirname(__file__)
app = Flask(__name__)


f=open('password.txt', 'a')
@app.route('/entrance', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        log_sign = request.form['options']
        if log_sign == 'Login':
            return render_template('login.html')
        elif log_sign == 'SignUp':
            return render_template('signup.html')
    return render_template('entrance.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        f = open("password.txt", "r").read()
        Username = (request.form['user'])
        Password = (request.form['pass'])
        while Username not in f or ('%s:%s' % (Username, Password)) not in f:
            return render_template('login.html',  message='Wrong Username or Password !!')
        return render_template('home.html', Username=Username)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        f = open("password.txt", "r").read()
        Username = (request.form['user'])
        Password = (request.form['pass'])
        while Username in f:
            return render_template('signup.html',  message='Select Another One : Username Exists !!')
        f = open("password.txt", "a")
        f.write('%s:%s\n' % (Username, Password))
        f.close()
        return render_template('home.html', Username=Username)


@app.route('/upload', methods=['GET', 'POST'])
def uploading_file():
    if request.method == 'POST':
        f = request.files['uploadedData']
        f.save(BASE_DIR+ f'/{secure_filename(f.filename)}')
        que = Queue()
        x = threading.Thread(target=run_py, args=(que,))
        x.start()
        result = que.get()
        print(result)
        mess=None
        if result=='home.html':
            mess='Wrong file uploaded . Try again !! '
        return render_template(result,Message=mess)


def run_py(que):
    try:
        import test_tsp
        suite = unittest.TestLoader().loadTestsFromModule(test_tsp)
        runner=HtmlTest.HTMLTestRunner(output='templates')
        test_file_name=runner.run(suite).report_name
        que.put(test_file_name)
    except ModuleNotFoundError:
        que.put('home.html')




if __name__ == '__main__':
    app.run(debug=True,host='localhost', port=5003)
                                   
                                   
                                



