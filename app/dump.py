import click
from flask import current_app, g
from flask.cli import with_appcontext

import mysql.connector

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host='localhost',
            database='gutendex',
            user='rohan',
            password='password'
        )
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('set global max_allowed_packet=67108864')
    with current_app.open_resource('gutendex.sql', 'rb') as f:
        cursor.execute(f.read().decode('utf-8'), multi=True)

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')