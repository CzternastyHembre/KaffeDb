-- SQLite
PRAGMA FOREIGN_keys = ON;

DROP TABLE IF EXISTS Region;
CREATE TABLE Region (
    name TEXT NOT NULL,
    Country_PK TEXT NOT NULL,
    CONSTRAINT Region_PK PRIMARY KEY (name, Country_PK),
    CONSTRAINT name
    FOREIGN KEY (Country_PK)
        REFERENCES Country (name)
);

DROP TABLE IF EXISTS Country;
CREATE TABLE Country (
    name TEXT PRIMARY KEY
);

INSERT INTO Country VALUES ("Norge");
INSERT INTO Country VALUES ("Sverige");
INSERT INTO Country VALUES ("Afghanistan");
INSERT INTO Country VALUES ("Albania");
INSERT INTO Country VALUES ("Algeria");
INSERT INTO Country VALUES ("Andorra");
INSERT INTO Country VALUES ("Angola");
INSERT INTO Country VALUES ("Antigua and Barbuda");

INSERT INTO Region VALUES ("Stavanger", "Sverige");
INSERT INTO Region VALUES ("Stavanger", "Norge"); --This should work
--INSERT INTO Region VALUES ("Stavanger", "Norge"); --This should not work

INSERT INTO Region VALUES ("Region_1","Algeria");
INSERT INTO Region VALUES ("Region_1","Andorra");
INSERT INTO Region VALUES ("Region_1","Angola");
INSERT INTO Region VALUES ("Region_1","Antigua and Barbuda");


SELECT * FROM Region;
SELECT * FROM Country;

    