Drop table if EXISTS users;
CREATE TABLE Users (
    email TEXT PRIMARY KEY,
    firstName TEXT,
    lastName TEXT,
    password TEXT
);


DROP TABLE IF EXISTS Coffee;
CREATE TABLE Coffee (
    coffee_id INTEGER PRIMARY KEY,
    coffee_name TEXT,
    coffee_description TEXT,
    kg_price_kr DOUBLE
);

DROP TABLE IF EXISTS Evaluation;
CREATE TABLE Evaluation (
    eval_id INTEGER PRIMARY KEY,
    coffe_id INTEGER,
    user_email TEXT,
    points INTEGER,
    eval_date TEXT,
    user_notes TEXT,
    CONSTRAINT eval_id
        FOREIGN KEY (coffe_id) 
            REFERENCES Coffee (coffee_id),
    CONSTRAINT eval_id
        FOREIGN KEY (user_email) 
            REFERENCES Coffee (email)
);


INSERT INTO Users VALUES ("mattis.hembre@gmail.com", "Mattis", "Hembre", "1234");
INSERT INTO Users VALUES ("karan.sander@gmail.com", "Karan", "Sander", "1234");
INSERT INTO Users VALUES ("casper.amtrup@gmail.com", "Casper", "Amtrup", "1234");
INSERT INTO Users VALUES ("sofus.buskoven@gmail.com", "Sofus", "Buskoven", "1234");

INSERT INTO Coffee VALUES (0, "Mocca", "loremloremlorem", 25.4);
INSERT INTO Coffee VALUES (1, "Latte", "loremloremlorem", 12.4);

INSERT INTO Evaluation VALUES (0, 0, "mattis.hembre@gmail.com", 4, "11-11-2021", "Was to cold");
INSERT INTO Evaluation VALUES (1, 0, "mattis.hembre@gmail.com", 6, "11-11-2021", "Was to cold");

SELECT * FROM Users;
SELECT * FROM Coffee;
SELECT * FROM Evaluation;
