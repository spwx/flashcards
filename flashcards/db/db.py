import sqlite3
import os


class DB(object):

    def __init__(self, dbstring='flashcards/db/flashcards.db'):
        # does the db exist?
        db_exists = os.path.exists(dbstring)

        self._conn = sqlite3.connect(dbstring)
        self._cursor = self._conn.cursor()

        # if the db didn't exist before load up the schema
        if (db_exists is False) or (dbstring is ':memory:'):
            self.create_db()
            self._conn.commit()

    def create_db(self):
        with open('flashcards/db/flashcards.sql') as f:
            sql = f.read()

        self._cursor.executescript(sql)

        self._cursor.execute('''
            INSERT INTO Decks (deck_name) VALUES ('default')
        ''')

        self._conn.commit()

    def create_card(self, front, back):
        values = (front, back)

        self._cursor.execute('INSERT INTO Cards (front, back) VALUES (?, ?)',
                             values)

        self._conn.commit()

    def create_deck(self, name, parent='default'):
        value = (parent,)

        # get the deck_id of the parent deck
        self.cursor.execute('SELECT deck_id FROM Decks WHERE deck_name = ?',
                            value)
        parent_deck = self.cursor.fetchone()

        if parent_deck is None:
            print('Parent deck does not exist')
        else:
            parent_deck = parent_deck[0]
            values = (name, parent_deck)
            try:
                self.cursor.execute('''
                    INSERT INTO Decks (deck_name, parent_deck)
                    VALUES (?, ?)''', values)
            except sqlite3.IntegrityError:
                print('There is already a deck by that name')

        self._conn.commit()

    def __del__(self):
        self._cursor.close()
        self._conn.close()
