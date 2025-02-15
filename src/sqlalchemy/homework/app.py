from datetime import datetime

from flask import Flask
from flask import request
from flask import redirect
from flask import render_template

from models import db, Genre, Book

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/postgres?client_encoding=utf8'

db.init_app(app)

with app.app_context():
  db.drop_all()
  db.create_all()

  genre1 = Genre(name="Fantastic")
  genre2 = Genre(name="Sci-Fi")

  db.session.add(genre1)
  db.session.add(genre2)

  db.session.commit()

  book1 = Book(
    title="Book1",
    author="Author1",
    issue_year="2025",
    genre_id=genre1.id
  )

  book10 = Book(title="Book10", author="Author10", issue_year="2025", genre_id=genre2.id)
  book2 = Book(title="Book2", author="Author2", issue_year="2025", genre_id=genre1.id)
  book3 = Book(title="Book3", author="Author3", issue_year="2025", genre_id=genre1.id)
  book4 = Book(title="Book4", author="Author4", issue_year="2025", genre_id=genre1.id)
  book5 = Book(title="Book5", author="Author5", issue_year="2025", genre_id=genre1.id)
  book6 = Book(title="Book6", author="Author6", issue_year="2025", genre_id=genre1.id)
  book7 = Book(title="Book7", author="Author7", issue_year="2025", genre_id=genre2.id)
  book8 = Book(title="Book8", author="Author8", issue_year="2025", genre_id=genre2.id)
  book9 = Book(title="Book9", author="Author9", issue_year="2025", genre_id=genre2.id)
  book11 = Book(title="Book11", author="Author10", issue_year="2025", genre_id=genre2.id)
  book12 = Book(title="Book12", author="Author10", issue_year="2025", genre_id=genre2.id)
  book13 = Book(title="Book13", author="Author10", issue_year="2025", genre_id=genre2.id)
  book14 = Book(title="Book14", author="Author10", issue_year="2025", genre_id=genre2.id)
  book15 = Book(title="Book15", author="Author10", issue_year="2025", genre_id=genre2.id)
  book16 = Book(title="Book16", author="Author10", issue_year="2025", genre_id=genre2.id)

  db.session.add(book10)
  db.session.add(book1)
  db.session.add(book2)
  db.session.add(book3)
  db.session.add(book4)
  db.session.add(book5)
  db.session.add(book6)
  db.session.add(book7)
  db.session.add(book8)
  db.session.add(book9)
  db.session.add(book11)
  db.session.add(book12)
  db.session.add(book13)
  db.session.add(book14)
  db.session.add(book15)
  db.session.add(book16)

  db.session.commit()

@app.route("/")
def list_books():
  books = db.session.execute(
    db.select(Book).order_by(Book.change_date.desc()).limit(15)
  ).scalars()
  return render_template("books.html", books=books)

@app.route("/genre/<int:genre_id>")
def get_books_by_genre(genre_id):
  genre = db.get_or_404(Genre, genre_id)
  return render_template(
    "genre_books.html",
    genre_name=genre.name,
    books=genre.books
  )

@app.route("/rest/book/update/<int:id>", methods=["POST"])
def update_book(id):
  book = db.get_or_404(Book, id)
  book.is_read = book.is_read = "is_read" in request.form
  book.change_date = datetime.now()

  db.session.commit()
  return redirect(
    "/"
  )

if __name__ == "__main__":
  app.run(debug=True)