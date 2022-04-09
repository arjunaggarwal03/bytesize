from flask import Flask, render_template, request

app = Flask(__name__)
# edits = Edits(app)

@app.route('/')
def index():
    # print(Document.getElementById(Document, "input-text"))
    return render_template('index.html')

@app.route('/', methods=['POST'])
def query_form():
    text = (request.form['text'],request.form['text2'])
    print(text)
    return text

if __name__ == '__main__':
    app.run()