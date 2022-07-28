from flask import Flask, render_template, request
from model import *

app = Flask(__name__)
# edits = Edits(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def query_form():
    # text = (request.form['text'],request.form['text2'])
    # print(text)
    res = run_model(request.form['text'],request.form['text2'])
    return render_template('results.html',value=res)

if __name__ == '__main__':
    app.run()