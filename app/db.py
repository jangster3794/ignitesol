from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()

def init_db(app):
    SQLAlchemy(app)

class Books(db.Model):
    __tablename__ = 'books_book'

    id = db.Column(db.Integer, primary_key=True)
    download_count = db.Column(db.Integer())
    gutenberg_id = db.Column(db.Integer())
    media_type = db.Column(db.String())
    title = db.Column(db.String())

    # author = relationship("BookAuthors")

    def __init__(self, download_count, gutenberg_id, media_type, title):
        self.download_count = download_count
        self.gutenberg_id = gutenberg_id
        self.media_type = media_type
        self.title = title
        
    def to_json(self):
        return {
            'id': self.id,
            'download_count': self.download_count,
            'gutenberg_id': self.gutenberg_id,
            'media_type': self.media_type,
            'title': self.title
        }

    def __repr__(self):
        return f"<Book {self.title}>"

class Author(db.Model):
    __tablename__ = 'books_author'

    id = db.Column(db.Integer, primary_key=True)
    birth_year = db.Column(db.Integer())
    death_year = db.Column(db.Integer())
    name = db.Column(db.String())

    # bookauthor = relationship('BookAuthors', backref=("Author"))

    def __init__(self, birth_year, death_year, name):
        self.birth_year = birth_year
        self.death_year = death_year
        self.name = name
        
    def to_json(self):
        return {
            'id': self.id,
            'birth_year': self.birth_year,
            'death_year': self.death_year,
            'name': self.name
        }

    def __repr__(self):
        return f"<Author {self.name}>"


class BookAuthors(db.Model):
    __tablename__ = 'books_book_authors'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(
        db.Integer(),
        db.ForeignKey('books_book.id', ondelete='CASCADE')
    )
    author_id = db.Column(
        db.Integer(),
        db.ForeignKey('books_author.id', ondelete='CASCADE')
    )

    def __init__(self, book_id, author_id):
        self.book_id = book_id
        self.author_id = author_id

    def to_json(self):
        return {
            'id': self.id,
            'book_id': self.book_id,
            'author_id': self.author_id
        }

    def __repr__(self):
        return f"<Author ID {self.author_id}>"

class Bookshelves(db.Model):
    __tablename__ = 'books_book_bookshelves'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer(), db.ForeignKey('books_book.id'))
    bookshelf_id = db.Column(db.Integer(), db.ForeignKey('books_bookshelf.id'))

    def __init__(self, book_id, bookshelf_id):
        self.book_id = book_id
        self.bookshelf_id = bookshelf_id
        
    def to_json(self):
        return {
            'id': self.id,
            'book_id': self.book_id,
            'bookshelf_id': self.bookshelf_id
        }

    def __repr__(self):
        return f"<Bookshelves {self.bookshelf_id}>"

class BookLanguages(db.Model):
    __tablename__ = 'books_book_languages'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer(), db.ForeignKey('books_book.id'))
    language_id = db.Column(db.Integer(), db.ForeignKey('books_language.id'))

    def __init__(self, book_id, language_id):
        self.book_id = book_id
        self.language_id = language_id
        
    def to_json(self):
        return {
            'id': self.id,
            'book_id': self.book_id,
            'language_id': self.language_id
        }

    def __repr__(self):
        return f"<LanguageID {self.language_id}>"

class BookSubjects(db.Model):
    __tablename__ = 'books_book_subjects'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer(), db.ForeignKey('books_book.id'))
    subject_id = db.Column(db.Integer(), db.ForeignKey('books_subject.id'))

    def __init__(self, book_id, subject_id):
        self.book_id = book_id
        self.subject_id = subject_id
        
    def to_json(self):
        return {
            'id': self.id,
            'book_id': self.book_id,
            'subject_id': self.subject_id
        }

    def __repr__(self):
        return f"<SubjectID {self.subject_id}>"

class Bookshelf(db.Model):
    __tablename__ = 'books_bookshelf'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name
        
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __repr__(self):
        return f"<Bookshelf {self.name}>"

class BookFormat(db.Model):
    __tablename__ = 'books_format'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.String(), db.ForeignKey('books_book.id'))
    mime_type = db.Column(db.String())
    url = db.Column(db.String())

    def __init__(self, mime_type, url, book_id):
        self.book_id = book_id
        self.mime_type = mime_type
        self.url = url

    def to_json(self):
        return {
            'id': self.id,
            'book_id': self.book_id,
            'mime_type': self.mime_type,
            'url': self.url
        }

    def __repr__(self):
        return f"<BookFormatURL {self.url}>"


class Language(db.Model):
    __tablename__ = 'books_language'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String())

    # book_language = relationship('BookLanguages')

    def __init__(self, mime_type, url, book_id):
        self.code = code

    def to_json(self):
        return {
            'id': self.id,
            'code': self.code
        }

    def __repr__(self):
        return f"<Language {self.code}>"

class Subject(db.Model):
    __tablename__ = 'books_subject'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __repr__(self):
        return f"<Subject {self.name}>"