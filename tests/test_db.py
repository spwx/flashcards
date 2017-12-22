import pytest
from flashcards.db import DB


@pytest.fixture(scope="module")
def db():
    database = DB(':memory:')
    # use yield so that database.__del__ isn't invoked
    yield database


def test_create_db(db):
    result = db.query('SELECT deck_id From Decks').fetchone()[0]
    assert result == 1


def test_query_db(db):
    values = ('hello', 'world')
    db.query('INSERT INTO Cards (front, back) VALUES (?, ?)', values)
    query = db.query('''
            SELECT front, back
            FROM Cards
            WHERE front='hello' AND back='world'
            ''')
    assert query.fetchone() == ('hello', 'world')
