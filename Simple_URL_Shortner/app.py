from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class URL(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    long = db.Column("long", db.String(), nullable=False)
    short = db.Column("short", db.String(3), nullable=False)

    def __init__(self, long, short):
        self.long = long
        self.short = short

# Create the database tables By running the script in shell or terminal

# form app import app, db
# with app.app_context():
#     db.create_all()

def shorten_url():
    letters = string.ascii_uppercase + string.ascii_lowercase
    while True:
        rand_letters = random.choices(letters, k=3)
        rand_letters = ''.join(rand_letters)
        short_url = URL.query.filter_by(short=rand_letters).first()
        if not short_url:
            return rand_letters


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle form submission or other POST logic here
        url_received = request.form.get('url')
        found_url = URL.query.filter_by(long=url_received).first()
        if found_url:
            return redirect(url_for("display_short_url", url=found_url.short))
        else:
            # Here you would typically create a new short URL and save it to the database
            short_url = shorten_url()  # Assume this function generates a short URL
            new_url = URL(long=url_received, short=short_url)
            db.session.add(new_url)
            db.session.commit()
            return redirect(url_for("display_short_url", url=short_url))
    else:
        return render_template('index.html')

@app.route('/display/<url>')
def display_short_url(url):
    return render_template('shorturl.html', short_url_display=url)

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    complete_url = URL.query.filter_by(short=short_url).first()
    if complete_url:
        return redirect(complete_url.long)
    else:
        return f"<h1>URL not found</h1>", 404 
if __name__ == '__main__':
    app.run(debug=True)