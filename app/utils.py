from .db import *
from sqlalchemy import func, or_

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

def search_library(filters):
    query = db.session.query(
        Books,
        Author,
        Language,
        Subject,
        Bookshelf
        ).outerjoin(
            BookAuthors
            ).outerjoin(
                Author
                ).outerjoin(
                    BookLanguages
                    ).outerjoin(
                        Language
                        ).outerjoin(
                            BookSubjects
                            ).outerjoin(
                                Subject
                                ).outerjoin(
                                    Bookshelves
                                    ).outerjoin(
                                        Bookshelf
                                        )
    if filters.get('gutenberg_id'):
        query = query.filter(Books.gutenberg_id == int(filters['gutenberg_id']))

    if filters.get('book_id'):
        query = query.filter(Books.gutenberg_id == int(filters['book_id']))

    if filters.get('language'):
        query = query.filter(func.lower(Language.code) == func.lower(filters['language']))

    if filters.get('topic'):
        search = "%{}%".format(filters['topic'])
        query = query.filter(
            or_(
                func.lower(Subject.name).like(func.lower(search)),
                func.lower(Bookshelf.name).like(func.lower(search))
                )
            )

    if filters.get('author'):
        search = "%{}%".format(filters['author'])
        query = query.filter(func.lower(Author.name).like(func.lower(search)))

    if filters.get('title'):
        search = "%{}%".format(filters['title'])
        query = query.filter(func.lower(Books.title).like(func.lower(search)))

    data = query.order_by(Books.download_count.desc()).limit(5).all()
    final_data = []
    for book, author, language, subject, bookshelf in data:
        res = {
            'book': book.to_json(),
            'author': author.to_json() if author else {},
            'language': language.to_json() if language else {},
            'subject': subject.to_json() if subject else {} ,
            'bookshelf': bookshelf.to_json() if bookshelf else {}
        }
        final_data.append(res)
    return final_data