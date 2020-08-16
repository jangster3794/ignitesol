from .db import *
from sqlalchemy import func, or_

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

def search_library(filters):
    pg = int(filters.get('pg', 1))
    limit = int(filters.get('r', 25))
    query = db.session.query(
        Books,
        Author,
        Language,
        Subject,
        Bookshelf,
        BookFormat
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
                                        ).outerjoin(
                                            BookFormat
                                            )
    if filters.get('gutenberg_id'):
        all_ids = [int(i) for i in filters['gutenberg_id'].split(',')]
        query = query.filter(Books.gutenberg_id.in_(all_ids))

    if filters.get('book_id'):
        all_ids = [int(i) for i in filters['book_id'].split(',')]
        query = query.filter(Books.gutenberg_id.in_(all_ids))

    if filters.get('language'):
        all_langs = [i.lower() for i in filters['language'].split(',')]
        query = query.filter(func.lower(Language.code).in_(all_langs))

    if filters.get('topic'):
        search = ["%{}%".format(i) for i in filters['topic'].split(',')]
        for s in search:
            query = query.filter(
                or_(
                        func.lower(Subject.name).like(func.lower(s)),
                        func.lower(Bookshelf.name).like(func.lower(s))
                    )
                )

    if filters.get('author'):
        search = ["%{}%".format(i) for i in filters['author'].split(',')]
        for s in search:
            query = query.filter(
                or_(
                        func.lower(Author.name).like(func.lower(search))
                    )
                )
    if filters.get('title'):
        search = ["%{}%".format(i) for i in filters['title'].split(',')]
        for s in search:
            query = query.filter(
                or_(
                        func.lower(Books.title).like(func.lower(search))
                    )
                )

    data = query.distinct(Books.id).order_by(Books.download_count.desc()).offset((pg-1)*limit).limit(limit).all()
    final_data = []
    for book, author, language, subject, bookshelf, bookformat in data:
        res = {
            'book': book.to_json(),
            'author': author.to_json() if author else {},
            'language': language.to_json() if language else {},
            'subject': subject.to_json() if subject else {} ,
            'bookshelf': bookshelf.to_json() if bookshelf else {},
            'bookformat': bookformat.to_json() if bookformat else {}
        }
        final_data.append(res)
    return final_data