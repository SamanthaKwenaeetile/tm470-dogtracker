from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create database table
def init_db():

    connection = sqlite3.connect('database/dogtracker.db')

    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            breed TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

# the home page
@app.route('/')
def home():
    return render_template('index.html')

# the login page
@app.route('/login')
def login():
    return render_template('login.html')

# Add dog page
@app.route('/add-dog', methods=['GET', 'POST'])
def add_dog():

    if request.method == 'POST':

        dog_name = request.form['name']
        dog_breed = request.form['breed']
        dog_age = request.form['age']

        connection = sqlite3.connect('database/dogtracker.db')

        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO dogs (name, breed, age)
            VALUES (?, ?, ?)
        ''', (dog_name, dog_breed, dog_age))

        connection.commit()
        connection.close()

    return render_template('add_dog.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)