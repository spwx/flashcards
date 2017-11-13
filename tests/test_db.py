import pytest
from flashcards.db import DB


@pytest.fixture(scope="module")
def cursor():
    database = DB(':memory:')
    # use yield so that database.__del__ isn't invoked
    yield database._cursor


def test_create_db(cursor):
    result = cursor.execute('SELECT deck_id From Decks').fetchone()[0]
    assert result == 1
