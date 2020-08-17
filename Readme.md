Steps To Follow:

Create a local database named gutendex
- create DATABASE gutendex;

Create a virtual environment and activate
- python -m venv env
- source env/bin/activate

Install dependencies
- pip install -r requirements.txt

Initialize Dump DB
- Flask init-db

Run python application
- python wsgi.py

Accepted query params includes
- pg for page number default 1
- r for results count per page default is 25
- gutenberg_id
- book_id
- language
- topic
- author
- title

Deployed on EC2 instance using Supervisor
- Search API = http://15.207.87.22:5000/search?gutenberg_id=3