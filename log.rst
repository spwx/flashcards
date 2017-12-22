2017-11-15

Ok need to refocus and actually get something done here.

First off, I need a better way to think about layout. I am going to try drawing
a map of how I want this app structured. I think it might also be a waste of
time. Because just implementing something might be easier.

I also want to start using TDD. Now that i know how to create tests, I would
like see how it feels to use them to lead my development.


2017-11-13

Finally finished moving all my database functions in to a DB class. This way
they can all share the same database connection.

Now on to more testing!

--

Ok, got some tests working. Figured out how to crate a pytest fixture and what
dependency injection was all about.

Also figured out yield must be used instead of return on a module scoped
fixture in order to keep the objects in the fixture 'alive.'

Now the problem is program organization. I went a little crazy with using OOP
and put all of my functions in one class. It had the effect of mixing up too
many things.

Now I'm thinking I should split the database creation/connection stuff from the
functions that work on the database (create_card, get_card). Maybe i should
list out how many methods im talking about:

create_card, get_card
create_deck, get_deck
get_cards_in_deck,
associate_card_and_deck,
count_num_decks_card_is_in,

And I am sure there are a lot more... Yea, I don't think im going to put them
all in a single class


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
