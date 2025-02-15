from __future__ import annotations
from datetime import datetime
from typing import List

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

db = SQLAlchemy()

# Mapped[type] - транслирует тип данных Python в тип данных SQL
# (К примеру int в INTEGER, str в VARCHAR)

# mapped_colum - позволяет задать валидацию данных
# (к примеру, максимальная длина строки String(30)),
# определить первичный ключ...
class Book(db.Model):
  __tablename__ = "books"

  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str]
  author: Mapped[str]
  issue_year: Mapped[str]
  is_read: Mapped[bool] = mapped_column(default=False)
  create_date: Mapped[datetime] = mapped_column(server_default=func.now())
  change_date: Mapped[datetime] = mapped_column(default=func.now())

  genre_id: Mapped[int] = mapped_column(ForeignKey("genres.id"))
  genre: Mapped[Genre] = relationship(
      back_populates="books"
  )

  def __repr__(self):
      return f'Book(title={self.title}, author={self.author}, issue_year={self.issue_date}, is_read={self.is_read}, genre={self.genre.name})'

class Genre(db.Model):
  __tablename__ = "genres"

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(50))
  create_date: Mapped[datetime] = mapped_column(server_default=func.now())
  change_date: Mapped[datetime] = mapped_column(default=func.now())

  books: Mapped[List[Book]] = relationship(
      back_populates="genre"
  )

  def __repr__(self):
      return f'Genre(name={self.name})'
