from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/add-dog')
def add_dog():
    return render_template('add_dog.html')

if __name__ == '__main__':
    app.run(debug=True)