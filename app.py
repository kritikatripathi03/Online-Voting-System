from flask import Flask, render_template, request
from save_data import save_comment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    return save_comment()

if __name__ == '__main__':
    app.run(debug=True)