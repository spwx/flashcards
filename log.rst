2017-11-13

Finally finished moving all my database functions in to a DB class. This way
they can all share the same database connection.

Now on to more testing

2017-11-11

Figured out that the setup.py needs to be in a parent directory of the
application.

So now i will structure the application like this:

.
├── flashcards/
│   ├── db/
│   │   ├── db.py
│   │   ├── flashcards.db
│   │   ├── flashcards.sql
│   │   └── __init__.py
│   └── __init__.py
├── ideas.rst
├── log.rst
├── Pipfile
├── Pipfile.lock
├── README.rst
├── setup.py
└── tests/
    └── test_first.py

Next I will figure out how to use pytest with a sqlite3 connection.

Well I figured that out, but i'm not going to implement it yet. Instead I am
going to create a DB object and share the cursor amongst my DB functions
(create_db, add_card, add_deck, ...).

This means I finally get to mess around with objects!
