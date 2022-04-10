from flask import Flask, render_template, request

app = Flask(__name__)
# edits = Edits(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def query_form():
    text = (request.form['text'],request.form['text2'])
    print(text)
    return render_template('results.html',value=["test1","test2","test3","test4","test5"])

if __name__ == '__main__':
    app.run()