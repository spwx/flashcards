import sqlite3


def create_db():
    conn = sqlite3.connect('flashcards.db')

    c = conn.cursor()

    with open('flashcards.sql') as f:
        sql = f.read()

    c.executescript(sql)

    c.execute("INSERT INTO Decks (deck_name) VALUES ('default')")

    conn.commit()
    conn.close()


def create_card(front, back):
    conn = sqlite3.connect('flashcards.db')
    c = conn.cursor()

    values = (front, back)

    c.execute('INSERT INTO Cards (front, back) VALUES (?, ?)', values)

    conn.commit()
    conn.close()


def create_deck(name, parent='default'):
    conn = sqlite3.connect('flashcards.db')
    c = conn.cursor()

    value = (parent,)

    # get the deck_id of the parent deck
    c.execute('SELECT deck_id FROM Decks WHERE deck_name = ?', value)
    parent_deck = c.fetchone()

    if parent_deck is None:
        print('Parent deck does not exist')
    else:
        parent_deck = parent_deck[0]
        values = (name, parent_deck)
        try:
            c.execute('''INSERT INTO Decks (deck_name, parent_deck)
                         VALUES (?, ?)''', values)
        except sqlite3.IntegrityError:
            print('There is already a deck by that name')

    conn.commit()
    conn.close()
