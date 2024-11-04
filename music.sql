CREATE TABLE artist (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE album (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES artist(id)
);

CREATE TABLE song (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    album_id INTEGER,
    track_number INTEGER,
    duration INTEGER, -- in seconds
    FOREIGN KEY (album_id) REFERENCES album(id)
);
