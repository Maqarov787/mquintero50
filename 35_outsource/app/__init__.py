from flask import Flask, render_template, redirect, url_for, request, session, g
import sqlite3
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['DATABASE'] = 'blog.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        db.executescript('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS blogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            );

            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                blog_id INTEGER NOT NULL,
                FOREIGN KEY (blog_id) REFERENCES blogs (id)
            );
        ''')
        db.commit()

@app.route('/')
def index():
    db = get_db()
    cur = db.execute('SELECT id, title FROM blogs')
    blogs = cur.fetchall()
    return render_template('index.html', blogs=blogs)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        db = get_db()
        try:
            db.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            db.commit()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            return 'Username already exists'
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        if user:
            session['user_id'] = user[0]
            return redirect(url_for('index'))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/blog/new', methods=['GET', 'POST'])
def new_blog():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        db = get_db()
        db.execute('INSERT INTO blogs (title, user_id) VALUES (?, ?)', (title, session['user_id']))
        db.commit()
        return redirect(url_for('index'))
    return render_template('blog.html')

@app.route('/blog/<int:blog_id>/entry/new', methods=['GET', 'POST'])
def new_entry(blog_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        content = request.form['content']
        db = get_db()
        db.execute('INSERT INTO entries (content, blog_id) VALUES (?, ?)', (content, blog_id))
        db.commit()
        return redirect(url_for('view_blog', blog_id=blog_id))
    return render_template('entry.html')

@app.route('/blog/<int:blog_id>')
def view_blog(blog_id):
    db = get_db()
    blog = db.execute('SELECT * FROM blogs WHERE id = ?', (blog_id,)).fetchone()
    entries = db.execute('SELECT * FROM entries WHERE blog_id = ?', (blog_id,)).fetchall()
    return render_template('view_blog.html', blog=blog, entries=entries)

@app.route('/entry/<int:entry_id>/edit', methods=['GET', 'POST'])
def edit_entry(entry_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    db = get_db()
    entry = db.execute('SELECT * FROM entries WHERE id = ?', (entry_id,)).fetchone()
    if request.method == 'POST':
        content = request.form['content']
        db.execute('UPDATE entries SET content = ? WHERE id = ?', (content, entry_id))
        db.commit()
        return redirect(url_for('view_blog', blog_id=entry[2]))
    return render_template('edit_entry.html', entry=entry)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    init_db()
    app.run(debug=True)
