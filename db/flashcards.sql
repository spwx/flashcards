CREATE TABLE IF NOT EXISTS Decks(
    deck_id INTEGER PRIMARY KEY,
    deck_name TEXT NOT NULL UNIQUE,
    parent_deck INTEGER,
    FOREIGN KEY(parent_deck) REFERENCES Decks(deck_id)
);

CREATE TABLE IF NOT EXISTS Cards(
    card_id INTEGER PRIMARY KEY,
    front TEXT NOT NULL,
    back TEXT NOT NULL,
    date_created INTEGER NOT NULL DEFAULT (strftime('%s', 'now')),
    date_edited INTEGER
);

CREATE TRIGGER [UpdateLastTime]
    AFTER
    UPDATE
    ON Cards
    FOR EACH ROW
BEGIN
    UPDATE Cards set date_edited=(strftime('%s', 'now')) where card_id=OLD.card_id;
END;

CREATE TABLE IF NOT EXISTS Decks_Cards(
    card_id INTEGER,
    deck_id INTEGER,
    FOREIGN KEY(card_id) REFERENCES Cards(card_id),
    FOREIGN KEY(deck_id) REFERENCES Decks(deck_id),
    PRIMARY KEY (card_id, deck_id)
);

CREATE TABLE IF NOT EXISTS Review(
    review_id INTEGER PRIMARY KEY,
    card_id INTEGER,
    time_studied INTEGER NOT NULL DEFAULT (strftime('%s', 'now')),
    score TEXT NOT NULL,
    CHECK (score IN ('passed', 'hard', 'failed')),
    FOREIGN KEY(card_id) REFERENCES Cards(card_id)
);

