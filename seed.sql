
DROP TABLE if exists lytter;
CREATE TABLE volume (
    id INTEGER PRIMARY KEY,
    DATETIME DEFAULT (STRFTIME('%d-%m-%Y   %H:%M', 'NOW','localtime')),
	name TEXT NOT NULL,
	mountpoint TEXT NOT NULL,
	size INTEGER
);

INSERT INTO valume (name, mountpoint, size) VALUES ("gunnar","std/lol", "1000");