import os

from flask import Flask
from flask import render_template

from models import db, Genre, Book

app = Flask(__name__)


# dialect://username:password@host:port/database
# postgresql://postgres:postgres@localhost/project
# $Env:SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres\@localhost:5432/postgres'
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/postgres?client_encoding=utf8'
# initialize the app with the extension
db.init_app(app)

with app.app_context():
  db.drop_all()
  db.create_all()

  genre1 = Genre(name="Fantastic")
  genre2 = Genre(name="Sci-Fi")

  db.session.add(genre1)
  db.session.add(genre2)

  db.session.commit()

@app.route("/")
def list_books():
  books = Book.query.all()
  return render_template("layout.html", genres=books)

@app.route("/genres/")
def list_genres():
  genres = Genre.query.all()
  return render_template("genres.html", genres=genres)

if __name__ == "__main__":
  app.run(debug=True)