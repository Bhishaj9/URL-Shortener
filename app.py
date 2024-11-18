from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import string
import random

# First make sure to install Flask using:
# pip install flask

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS urls
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         original_url TEXT NOT NULL,
         short_code TEXT NOT NULL UNIQUE,
         created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
    ''')
    conn.commit()
    conn.close()

# Generate a random short code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Create shortened URL
def create_short_url(original_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    
    while True:
        short_code = generate_short_code()
        try:
            c.execute('INSERT INTO urls (original_url, short_code) VALUES (?, ?)',
                     (original_url, short_code))
            conn.commit()
            break
        except sqlite3.IntegrityError:
            continue
    
    conn.close()
    return short_code

# Get original URL from short code
def get_original_url(short_code):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('SELECT original_url FROM urls WHERE short_code = ?', (short_code,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

# Routes
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']
        if not original_url:
            return render_template('index.html', error="Please enter a URL")
        
        short_code = create_short_url(original_url)
        short_url = request.host_url + short_code
        return render_template('index.html', short_url=short_url)
    
    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_url(short_code):
    original_url = get_original_url(short_code)
    if original_url:
        return redirect(original_url)
    return render_template('index.html', error="URL not found")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)