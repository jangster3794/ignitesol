from .db import *
from sqlalchemy import func, or_

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

def search_library(filters):
    pg = int(filters.get('pg', 1)) # For pagination
    limit = int(filters.get('r', 25)) # Result Count
    # Building Joins in query to fetch data from
    # Used Outerjoin because if in case data ! exists, query doesn't return empty dict
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
        # Creating List from ',' separated argument
        all_ids = [int(i) for i in filters['gutenberg_id'].split(',')]
        query = query.filter(Books.gutenberg_id.in_(all_ids))

    if filters.get('book_id'):
        # Creating List from ',' separated argument
        all_ids = [int(i) for i in filters['book_id'].split(',')]
        query = query.filter(Books.gutenberg_id.in_(all_ids))

    if filters.get('language'):
        # Creating List from ',' separated argument and matching in lowercase
        all_langs = [i.lower() for i in filters['language'].split(',')]
        query = query.filter(func.lower(Language.code).in_(all_langs))

    if filters.get('topic'):
        # Creating List from ',' separated argument and adding to or conditions
        search = ["%{}%".format(i) for i in filters['topic'].split(',')]
        for s in search:
            query = query.filter(
                or_(
                        func.lower(Subject.name).like(func.lower(s)),
                        func.lower(Bookshelf.name).like(func.lower(s))
                    )
                )

    if filters.get('author'):
        # Creating List from ',' separated argument and adding to or conditions
        search = ["%{}%".format(i) for i in filters['author'].split(',')]
        for s in search:
            query = query.filter(
                or_(
                        func.lower(Author.name).like(func.lower(search))
                    )
                )
    if filters.get('title'):
        # Creating List from ',' separated argument and adding to or conditions
        search = ["%{}%".format(i) for i in filters['title'].split(',')]
        for s in search:
            query = query.filter(
                or_(
                        func.lower(Books.title).like(func.lower(search))
                    )
                )

    # Executing our query that returns data cursors
    data = query.distinct(Books.id).order_by(Books.download_count.desc()).offset((pg-1)*limit).limit(limit).all()
    final_data = []
    # Looping through data to Jsonify all data instances.
    # Serializers can also be used for this.
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